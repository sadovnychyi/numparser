import re

NUMBERS = {n: i for i, n in enumerate([
  'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
  'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
  'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', ])}
NUMBERS.update({n: i * 10 for i, n in enumerate([
  'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'], 3)})

MAGNITUDE = dict(zip([
  'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion',
  'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion',
  'undecillion', 'duodecillion', 'tredecillion', 'quattuordecillion',
  'quinquadecillion', 'sedecillion', 'septendecillion', 'octodecillion',
  'novendecillion', 'vigintillion', 'unvigintillion', 'duovigintillion',
  'tresvigintillion', 'quattuorvigintillion', 'quinquavigintillion',
  'sesvigintillion', 'septemvigintillion', 'octovigintillion',
  'novemvigintillion', 'trigintillion', 'untrigintillion', 'duotrigintillion',
  'trestrigintillion', 'quattuortrigintillion', 'quinquatrigintillion',
  'sestrigintillion', 'septentrigintillion', 'octotrigintillion',
  'noventrigintillion', 'quadragintillion'],
  [10 ** i for i in range(3, 124, 3)]))

HUNDRED = 'hundred'

NUMBER_WITH_MAGNITUDE_RE = re.compile(
  r'([0-9,.]+)\W+(%s)(?:\W+([0-9,.]+))?' % '|'.join(MAGNITUDE.keys()))
NOT_NUMBER_RE = re.compile(r'[^0-9,.]+')


def text_to_number(text):
  """Accepts only limited words and converts them into a number.

  Args:
    text: String with words to convert. E.g. 'one billion'

  Returns:
    Integer number.

  Raises:
    ValueError: If unknown word were found or no number could be returned.
  """
  n = 0
  g = 0
  number_used = False
  for word in re.split(r'[\s-]+', text):
    number = NUMBERS.get(word, None)
    if number is not None:
      g += number
      number_used = True
    elif word == HUNDRED:
      g *= 100
    else:
      magnitude = MAGNITUDE.get(word, None)
      if magnitude is not None:
        n += g * magnitude
        g = 0
      else:
        raise ValueError('Unknown number: %s' % word)
  if not number_used:
    raise ValueError('No numbers found: %s' % text)
  return n + g


def numparser(string):
  """Accepts string which possible contains numbers and trying to convert them.

  It's possible that string will contain both number representations:
  string (one thousand) and integer (1,000) -- then only one value will be used.
  If string contains two numbers ($50,000,001 to $100,000,000) -- only
  the last one will be used.

  Args:
    string: String which likely to contain numbers.

  Returns:
    Float with parsed value or None if nothing found.
  """
  string = string.lower()

  try:
    number = float(text_to_number(' '.join(re.findall('(%s)' % '|'.join(
      NUMBERS.keys() + MAGNITUDE.keys() + [HUNDRED]), string))))
  except ValueError:
    number = None

  if number is None and any([c.isdigit() for c in string]):
    match = NUMBER_WITH_MAGNITUDE_RE.search(string)
    if match:
      number1, magnitude, number2 = match.groups()
      number = float(re.sub(r'[^0-9.]', '', number1).strip('.'))
      if magnitude:
        number *= MAGNITUDE.get(magnitude, 1)
      if number2:
        number += float(re.sub(r'[^0-9.]', '', number2).strip('.'))
    else:
      digits = [n for n in NOT_NUMBER_RE.split(string) if n]
      digits = digits[-1]
      digits = re.sub(r'[^0-9.]', '', digits).strip('.')
      if digits:
        number = float(digits)

  return number
