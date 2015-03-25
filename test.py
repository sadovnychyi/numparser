import unittest
import numparser


class TestNumParser(unittest.TestCase):
  def test_text_to_number(self):
    self.assertEqual(1, numparser.text_to_number('one'))
    self.assertEqual(12, numparser.text_to_number('twelve'))
    self.assertEqual(42, numparser.text_to_number('forty two'))
    self.assertEqual(300, numparser.text_to_number('three hundred'))
    self.assertEqual(1200, numparser.text_to_number('twelve hundred'))
    self.assertEqual(
      12304,
      numparser.text_to_number('twelve thousand three hundred four'))
    self.assertEqual(6000000, numparser.text_to_number('six million'))
    self.assertEqual(
      6400005,
      numparser.text_to_number('six million four hundred thousand five'))
    self.assertEqual(
      123456789012,
      numparser.text_to_number('one hundred twenty three billion four hundred '
                               'fifty six million seven hundred eighty nine '
                               'thousand twelve'))
    self.assertEqual(4 * 10 ** 33,
                     numparser.text_to_number('four decillion'))
    self.assertEqual(10 ** 123,
                     numparser.text_to_number('one quadragintillion'))

  def test_exception_raised_for_wrong_word(self):
    self.assertRaises(ValueError, numparser.text_to_number, '')
    self.assertRaises(ValueError, numparser.text_to_number, '10 thousand')
    self.assertRaises(ValueError, numparser.text_to_number, '$10 million')

  def test_numparser(self):
    self.assertEqual(410 * 10 ** 6, numparser.numparser('$410 million'))
    self.assertEqual(100 * 10 ** 6,
                     numparser.numparser('50,000,001 to $100,000,000'))
    self.assertEqual(100 * 10 ** 6, numparser.numparser('$100,000,000.0'))
    self.assertEqual(
      52500000,
      numparser.numparser('Fifty-two Million Five HundredThousand Dollars'))
    self.assertEqual(
      5 * 10 ** 6,
      numparser.numparser('less than     $5,000,000.00 (five million dollars'))
    self.assertEqual(
      50 * 10 ** 6 + 160000,
      numparser.numparser('$50 million   $160,000'))


if __name__ == '__main__':
  unittest.main()
