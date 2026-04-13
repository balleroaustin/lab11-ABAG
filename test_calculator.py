import unittest
import calculator

class TestCalculator(unittest.TestCase):

    ######### Partner 2
    def test_add(self): # 3 assertions
        assert add(1, 4) == 5
        assert add (-2 , 2) == 0
        assert add (0, 0 ) == 0

    def test_subtract(self): # 3 assertions
        assert subtract (10, 5) == 5
        assert subtract (2, 5) == -3
        assert subtract (0, 0) == 0

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(calculator.mul(3,4),12)
        self.assertEqual(calculator.mul(-2, 5), -10)
        self.assertEqual(calculator.mul(0,10),0)


    def test_divide(self): # 3 assertions
        self.assertEqual(calculator.div(2,10),5)
        self.assertEqual(calculator.div(4,20),5)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0,5)



    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10,100),2)
        self.assertEqual(logarithm(3, 9), 2)
        self.assertEqual(logarithm(2, 8),3)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 20)
    
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