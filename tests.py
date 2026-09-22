import unittest

from rectangle import *
from circle import *
from triangle import *
from square import *

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        """Проверка площади, если одна сторона равна 0"""
        res = rectangle_area(10, 0)
        self.assertEqual(res, 0)
       
    def test_square_mul(self):
        """Обычный расчет площади прямоугольника"""
        res = rectangle_area(10, 10)
        self.assertEqual(res, 100)

    def test_float_area(self):
        """Проверка площади прямоугольника с вещественными числами (дробными)"""
        res = rectangle_area(2.5, 4.0)
        self.assertEqual(res, 10.0)

    def test_normal_perimeter(self):
        """Обычный расчет периметра прямоугольника"""
        res = rectangle_perimeter(5, 4)
        self.assertEqual(res, 18)

    def test_zero_perimeter(self):
        """Частный случай: одна из сторон равна 0 (вырожденный прямоугольник)"""
        res = rectangle_perimeter(10, 0)
        self.assertEqual(res, 20)


class CircleTestCase(unittest.TestCase):
    def test_circle_area(self):
        """Обычный расчет площади круга"""
        res = circle_area(3)
        self.assertEqual(res, 28.274333882308138)

    def test_zero_radius_area(self):
        """Частный случай: площадь круга с радиусом 0 должна быть 0"""
        res = circle_area(0)
        self.assertEqual(res, 0)

    def test_circle_perimeter(self):
        """Проверка периметра (длины окружности) для обычного радиуса"""
        res = circle_perimeter(3)
        self.assertEqual(res, 18.84955592153876)

    def test_zero_radius_perimeter(self):
        """Частный случай: длина окружности с радиусом 0 равна 0"""
        res = circle_perimeter(0)
        self.assertEqual(res, 0)


class TriangleTestCase(unittest.TestCase):

    def test_triangle_area(self):
        """Обычный расчет площади треугольника"""
        res = triangle_area(2, 4)
        self.assertEqual(res, 4)

    def test_float_triangle_area(self):
        """Проверка площади треугольника с дробной высотой и основанием"""
        res = triangle_area(3.5, 2.0)
        self.assertEqual(res, 3.5)

    def test_triangle_perimeter(self):
        """Проверка периметра треугольника по трем сторонам"""
        res = triangle_perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_float_triangle_perimeter(self):
        """Проверка периметра треугольника с дробными сторонами"""
        res = triangle_perimeter(1.5, 2.5, 3.0)
        self.assertEqual(res, 7.0)


class SquareTestCase(unittest.TestCase):
    def test_square_area(self):
        """Обычный расчет площади квадрата"""
        res = square_area(4)
        self.assertEqual(res, 16)

    def test_large_square_area(self):
        """Проверка площади квадрата с очень большой стороной"""
        res = square_area(1000000)
        self.assertEqual(res, 1000000000000)

    def test_square_perimeter(self):
        """Обычный расчет периметра квадрата"""
        res = square_perimeter(5)
        self.assertEqual(res, 20)

    def test_zero_square_perimeter(self):
        """Частный случай: периметр квадрата со стороной 0 равен 0"""
        res = square_perimeter(0)
        self.assertEqual(res, 0)

    def test_diagonal(self):
        """Обычный расчет диагонали у прямоугольника"""
        res = rectangle_diagonal(3,4)
        self.assertEqual(res, 5.0)

    def test_irrational_diagonall(self):
        """Расчет диагонали с иррациональной длинной"""
        res = rectangle_diagonal(1,3)
        self.assertEqual(res, 10**(0.5))

