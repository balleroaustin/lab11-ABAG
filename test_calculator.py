import unittest
import calculator

class TestCalculator(unittest.TestCase):

    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(calculator.add(1, 4),  5)
        self.assertEqual(calculator.add(-2 , 2), 0)
        self.assertEqual(calculator.add(0, 0 ) ,0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(calculator.subtract(10, 5),5)
        self.assertEqual(calculator.subtract(2, 5), -3)
        self.assertEqual(calculator.subtract(0, 0), 0)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(calculator.mul(3,4),12)
        self.assertEqual(calculator.mul(-2, 5), -10)
        self.assertEqual(calculator.mul(0,10),0)


    def test_divide(self): # 3 assertions
        self.assertEqual(calculator.div(10,2),5)
        self.assertEqual(calculator.div(20,4),5)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(5,0)



    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            calculator.div(5, 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(calculator.logarithm(100,10),2)
        self.assertEqual(calculator.logarithm(9, 3), 2)
        self.assertEqual(calculator.logarithm(8, 2),3)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 20)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.logarithm(-1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(2,-5)
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 8)
    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(calculator.hypotenuse(3,4),5.0)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(calculator.square_root(9),3)
        self.assertAlmostEqual(calculator.square_root(2), 2**0.5)
        with self.assertRaises(ValueError):
            calculator.square_root(-4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()