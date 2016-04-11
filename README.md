numparser
=========

Python library for parsing numbers from strings.

Originally meant to be used to process results from Named Entity Recognizer.

Here's a sample strings which library can handle:

Input                                          | Output
-----------------------------------------------|-------------------------------:
six million four hundred thousand five         | 6,400,005
$410 million                                   | 410,000,000
50,000,001 to $100,000,000                     | 100,000,000
Fifty-two Million Five HundredThousand Dollars | 52,500,000
less than $5,000,000.00 (five million dollars  | 5,000,000
$50 million   $160,000                         | 50,160,000

Note that [short scale](https://en.wikipedia.org/wiki/Long_and_short_scales) is used and currently there's no support for [long scale](https://en.wikipedia.org/wiki/Long_and_short_scales).


Installation
============
```bash
pip install numparser
```


Quick Start
-----------
```python
>>> import numparser
>>> numparser.numparser('one quadrillion two hundred thousands three')
1000000000200003.0
```


Unit tests
==========

Clone the repository and run:
```bash
python tests.py
```
