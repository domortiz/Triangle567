"""this contains all unit tests"""
import unittest

from triangle import classify_triangle


# This code implements the unit test functionality


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    """runs all the test for the triangle """

    def test_right(self):
        """test if thr=e triangle is a right triangle"""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def test_equilateral(self):
        """test if the triangle is equilateral"""
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def test_scalene(self):
        """test if the triangle is scalene"""
        self.assertEqual(classify_triangle(1, 2, 3), 'Scalene', '1,2,3 should be Scalene')

    def tests_isosceles(self):
        """test if the triangle is isosceles"""
        self.assertEqual(classify_triangle(1, 2, 2), 'Isosceles', '1,2,2 should be Isosceles')

    # these are the new tests

    def test_invalid(self):
        """test for invalid inputs"""
        self.assertEqual(classify_triangle(0, 1, 2), 'InvalidInput', '0,1,2 is an invalid input')
        self.assertEqual(classify_triangle(10, 10, 10.5), 'InvalidInput', '0,1,2 is an invalid input')

    def test_not_triangle(self):
        """test for unreal triangles"""
        self.assertEqual(classify_triangle(1, 10, 12), 'NotATriangle', '1,10,12 is not a triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
