from views import home
import unittest


class BasicTestCase(unittest.TestCase):

  def test_roman_to_arabic(self):
    self.assertEqual(home.roman_to_arabic('XL'), 40)
    self.assertEqual(home.roman_to_arabic('XC'), 90)
    self.assertEqual(home.roman_to_arabic('MD'), 1500)
    self.assertEqual(home.roman_to_arabic('CCCXXXIII'), 333)
  def test_roman_to_arabic2(self):
    self.assertEqual(home.roman_to_arabic('XLIX'), 49)
    self.assertEqual(home.roman_to_arabic('XXX'), 30)
    self.assertEqual(home.roman_to_arabic('CL'), 150)
    self.assertEqual(home.roman_to_arabic('CMXCIX'), 999)
    self.assertEqual(home.roman_to_arabic('CDLXXXIX'), 489)
  def test_is_roman_number(self):
    self.assertTrue(home.is_roman_number('XL'))
    self.assertTrue(home.is_roman_number('XXX'))
    self.assertFalse(home.is_roman_number('XXXX'))
    self.assertFalse(home.is_roman_number('IIX'))
    self.assertFalse(home.is_roman_number('IXI'))
  def test_arabic_to_roman(self):
    self.assertEqual(home.arabic_to_roman('49'), 'XLIX')
    

if __name__ == '__main__':
    unittest.main()