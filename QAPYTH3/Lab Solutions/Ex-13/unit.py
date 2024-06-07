import unittest
from vat_calc import vat_Calc

class Testvat_Calc(unittest.TestCase):
    def test_vat_Calc(self):
        self.assertEquals(vat_Calc(100,20), 20, "Should be 20.0")


if __name__ == '__main__':
    unittest.main()
