#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.heirs.triangle import *
import array
import pytest

MAX_COUNT_TRIANGLE = 3
All_NEED_TYPES_OBJ = [['0', 60, 50], [None, 60, 50], [(123,), 60, 50], [{123, 'a'}, 60, 50], [True, 60, 50],
                      [{'a': 22}, 60, 50], array.array('i', [1, 2, 3])]
TYPE_VALUE = (int, float)
SUM_ANGLES = 180


@pytest.mark.positive_triangle
def test_correct_count_side():
    correct_count_side = Triangle(3, [10.5, 40, 50], [121, 30, 30])
    message = f"""Number of sides - {correct_count_side.count_side}, the figure is not a triangle"""
    assert correct_count_side.count_side == MAX_COUNT_TRIANGLE, message


@pytest.mark.positive_triangle
@pytest.mark.parametrize('count_side', [3])
@pytest.mark.parametrize('count_size_side', [[10, 55, 60]])
@pytest.mark.parametrize('count_angle', [[120, 33, 27]])
def test_correct_count_elem(count_side, count_size_side, count_angle):
    count_elem = Triangle(count_side, count_size_side, count_angle)
    message = f"The number of elements is not equal to {MAX_COUNT_TRIANGLE}"
    count_side, size_side, angles = count_elem.check_value()
    assert count_side == MAX_COUNT_TRIANGLE or len(size_side) == MAX_COUNT_TRIANGLE or len(angles) == MAX_COUNT_TRIANGLE, message


@pytest.mark.positive_triangle
def test_correct_size_side():
    correct_size_side = Triangle(3, [10, 60, 65], [120, 30, 33])
    max_size = max(correct_size_side.size_side)
    other_parties = sum(correct_size_side.size_side) - max_size
    message = 'The sum of the lengths of the two sides of the triangle is less than the length of the remaining side'
    assert other_parties > max_size, message


@pytest.mark.negative_triangle
@pytest.mark.parametrize('count_side', [0, -3])
@pytest.mark.parametrize('size_side', [[-10, 60, 50], [0, 60, 50], [10, -60, 50]])
@pytest.mark.parametrize('angles', [[10, 60, 50], [0, 60, 50], [10, 60, -50]])
def test_check_value_less_than_or_equal_zero(count_side, size_side, angles):
    incorrect_value_type = Triangle(count_side, size_side, angles)
    size_side = incorrect_value_type.check_less_than_zero(incorrect_value_type.size_side)
    angles = incorrect_value_type.check_less_than_zero(incorrect_value_type.angles)
    message = "In the values of the data types passed in the object the correct values are"
    assert count_side != [] or size_side != [] or angles != [], message


@pytest.mark.negative_triangle
@pytest.mark.parametrize('count_side', All_NEED_TYPES_OBJ)
@pytest.mark.parametrize('size_side', All_NEED_TYPES_OBJ)
@pytest.mark.parametrize('angles', All_NEED_TYPES_OBJ)
def test_incorrect_value_type(count_side, size_side, angles):
    incorrect_value_type = Triangle(count_side, size_side, angles)
    count_side, size_side, angles = incorrect_value_type.check_value()
    message = "In the values of the data types passed in the object the correct values are"
    assert type(count_side) not in TYPE_VALUE or type(size_side) not in TYPE_VALUE or type(angles) not in TYPE_VALUE, message


@pytest.mark.positive_triangle
def test_correct_angles():
    correct_angles = Triangle(3, [10, 20, 50], [80, 40, 60])
    message = "The size of the angles in the triangle is not correct"
    assert correct_angles.sum_angles_triangle() == SUM_ANGLES, message


@pytest.mark.negative_triangle
@pytest.mark.parametrize('count_side', [2, 4])
@pytest.mark.parametrize('count_size_side', [[10, 60], [10, 60, 20, 40]])
@pytest.mark.parametrize('count_angle', [[120, 30], [120, 30, 33, 44]])
def test_incorrect_count_elem(count_side, count_size_side, count_angle):
    count_elem = Triangle(count_side, count_size_side, count_angle)
    message = f"The count elems is equal to {MAX_COUNT_TRIANGLE}"
    count_side, size_side, angles = count_elem.check_value()
    assert count_side != MAX_COUNT_TRIANGLE or len(size_side) != MAX_COUNT_TRIANGLE or len(angles) != MAX_COUNT_TRIANGLE, message


@pytest.mark.positive_triangle
def test_isosceles_triangle_by_sides():
    isosceles_triangle = Triangle(3, [60, 60, 10], [85.22, 85.22, 9.66])
    message = "The number of sides in an isosceles triangle is less than or greater than 2"
    result = isosceles_triangle.check_repeating_elem(isosceles_triangle.size_side)
    assert result == 2, message


@pytest.mark.positive_triangle
def test_isosceles_triangle_by_angles():
    isosceles_triangle = Triangle(3, [60, 60, 10], [85.22, 85.22, 9.66])
    message = "The number of angles in an isosceles triangle is less than or greater than 2"
    result = isosceles_triangle.check_repeating_elem(isosceles_triangle.angles)
    assert result == 2, message


@pytest.mark.positive_triangle
def test_equilateral_triangle_by_sides():
    equilateral_triangle = Triangle(3, [60, 60, 60], [60, 60, 60])
    message = "Sides of an isosceles triangle are not equal"
    result = equilateral_triangle.check_repeating_elem(equilateral_triangle.size_side)
    assert result == 1, message


@pytest.mark.positive_triangle
def test_equilateral_triangle_by_angles():
    equilateral_triangle = Triangle(3, [60, 60, 60], [60, 60, 60])
    message = "Angles of an isosceles triangle are not equal"
    result = equilateral_triangle.check_repeating_elem(equilateral_triangle.angles)
    assert result == 1, message
