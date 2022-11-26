#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.heirs.rectangle import *
import array
import pytest

All_NEED_TYPES_OBJ = [['0', 60, 50], [None, 60, 50], [(123,), 60, 50], [{123, 'a'}, 60, 50], [True, 60, 50],
                      [{'a': 22}, 60, 50], array.array('i', [1, 2, 3])]
TYPE_VALUE = (int, float)

MAX_COUNT_RECTANGLE = 4
ANGLE_VALUE = 90


@pytest.mark.positive_rectangle
@pytest.mark.parametrize('count_side', [4])
@pytest.mark.parametrize('count_size_side', [[10.5, 40, 10.5, 40]])
@pytest.mark.parametrize('count_angle', [[90, 90, 90, 90]])
def test_correct_count_elem(count_side, count_size_side, count_angle):
    count_elem = Rectangle(count_side, count_size_side, count_angle)
    message = f"The number of elements is not equal to {MAX_COUNT_RECTANGLE}"
    count_side, size_side, angles = count_elem.check_value()
    assert count_side == MAX_COUNT_RECTANGLE or len(size_side) == MAX_COUNT_RECTANGLE or \
           len(angles) == MAX_COUNT_RECTANGLE, message


@pytest.mark.negative_rectangle
@pytest.mark.parametrize('count_side', [3, 5])
@pytest.mark.parametrize('count_size_side', [[10, 60, 10], [10, 60, 10, 60, 50]])
@pytest.mark.parametrize('count_angle', [[120, 30, 120], [120, 30, 120, 30, 40]])
def test_incorrect_count_elem(count_side, count_size_side, count_angle):
    count_elem = Rectangle(count_side, count_size_side, count_angle)
    message = f"The count elems is equal to {MAX_COUNT_RECTANGLE}"
    count_side, size_side, angles = count_elem.check_value()
    assert count_side != MAX_COUNT_RECTANGLE or len(size_side) != MAX_COUNT_RECTANGLE or \
           len(angles) != MAX_COUNT_RECTANGLE, message


@pytest.mark.negative_rectangle
@pytest.mark.parametrize('count_side', All_NEED_TYPES_OBJ)
@pytest.mark.parametrize('size_side', All_NEED_TYPES_OBJ)
@pytest.mark.parametrize('angles', All_NEED_TYPES_OBJ)
def test_incorrect_value_type(count_side, size_side, angles):
    incorrect_value_type = Rectangle(count_side, size_side, angles)
    count_side, size_side, angles = incorrect_value_type.check_value()
    message = "In the values of the data types passed in the object the correct values are"
    assert type(count_side) not in TYPE_VALUE or type(size_side) not in TYPE_VALUE or \
           type(angles) not in TYPE_VALUE, message


@pytest.mark.negative_triangle
@pytest.mark.parametrize('count_side', [0, -3])
@pytest.mark.parametrize('size_side', [[60, -50, 60, 50], [60 , 0, 60, 50], [60, 10, -60, 10]])
@pytest.mark.parametrize('angles', [[60, 10, 60, 10], [60, 0, 60, 50], [60, 10, 60, -10]])
def test_check_value_less_than_or_equal_zero(count_side, size_side, angles):
    incorrect_value_type = Rectangle(count_side, size_side, angles)
    size_side = incorrect_value_type.check_less_than_zero(incorrect_value_type.size_side)
    angles = incorrect_value_type.check_less_than_zero(incorrect_value_type.angles)
    message = "In the values of the data types passed in the object the correct values are"
    assert count_side != [] or size_side != [] or angles != [], message


@pytest.mark.positive_rectangle
def test_correct_size_side():
    correct_size_side = Rectangle(4, [10.5, 40, 10.5, 40], [90, 90, 90, 90])
    result_len, result_sum = correct_size_side.check_repeating_elem(correct_size_side.size_side)
    message = 'A rectangle lacks two pairs with the same side dimensions'
    assert result_len == 2, message
    message_1 = 'Does not match the number of items in pairs'
    assert result_sum == 4, message_1


@pytest.mark.negative_rectangle
@pytest.mark.parametrize('incorrect_size_site', [
    Rectangle(4, [10, 60, 10, 50], [90, 90, 90, 90]),
    Rectangle(4, [10, 60, 20, 60], [90, 90, 90, 90])])
def test_incorrect_size_site(incorrect_size_site):
    result_len, result_sum = incorrect_size_site.check_repeating_elem(incorrect_size_site.size_side)
    message = 'A rectangle lacks two pairs with the same side dimensions'
    assert result_len != 2, message
    message_1 = 'Does not match the number of items in pairs'
    assert result_sum == 4, message_1


@pytest.mark.positive_rectangle
def test_correct_angles():
    correct_angles = Rectangle(4, [10, 60, 10, 60], [90, 90, 90, 90])
    message = "The size of the angles in the rectangle is not correct"
    result = correct_angles.sum_angles_triangle()
    assert result / 4 == ANGLE_VALUE, message


@pytest.mark.positive_square
def test_square_check_by_sides():
    equilateral_square = Rectangle(4, [60, 60, 60, 60], [90, 90, 90, 90])
    result_len, result_sum = equilateral_square.check_repeating_elem(equilateral_square.size_side)
    message = 'There are pairs of different sizes of sides in the square'
    assert result_len == 1, message
    message_1 = 'Does not match the number of elem in pairs'
    assert result_sum == 4, message_1
