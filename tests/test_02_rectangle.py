#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.heirs.rectangle import *
import pytest

MAX_COUNT_RECTANGLE = 4
SUM_ANGLES = 360


@pytest.mark.positive_rectangle
def test_correct_count_side():
    correct_count_side = Rectangle(4, [10.5, 40, 10.5, 40], [90, 90, 90, 90])
    message = f"""Number of sides - {correct_count_side.count_side}, the figure is not a rectangle"""
    assert correct_count_side.count_side == MAX_COUNT_RECTANGLE, message


@pytest.mark.negative_rectangle
@pytest.mark.parametrize('incorrect_count_side, max_count', [
    (Rectangle(2, [10.5, 40, 10.5, 40], [90, 90, 90, 90]), MAX_COUNT_RECTANGLE),
    (Rectangle('4', [10.5, 40, 10.5, 40], [90, 90, 90, 90]), MAX_COUNT_RECTANGLE)])
def test_incorrect_count_side(incorrect_count_side, max_count):
    message = f"""Number of sides - {incorrect_count_side.count_side}, the figure is not a rectangle"""
    assert incorrect_count_side.count_side != max_count, message


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


@pytest.mark.negative_rectangle
def test_size_side_is_zero():
    """
    Метод check_is_not_zero() возвращает не пустой [] если сторона == 0
    """
    size_side_is_zero = Rectangle(4, [10, 60, 10, 0], [90, 90, 90, 90])
    message = "No sides equal 0"
    result = size_side_is_zero.check_is_not_zero(size_side_is_zero.size_side)
    assert result != [], message


@pytest.mark.negative_rectangle
@pytest.mark.parametrize('size_side_not_num', [
    Rectangle(4, [10, 60, 10, '60'], [90, 90, 90, 90]),
    Rectangle(4, [None, 60, 10, 60], [90, 90, 90, 90])])
def test_size_side_is_not_num(size_side_not_num):
    message = "All of the sides is numbers"
    result = size_side_not_num.check_is_num(size_side_not_num.size_side)
    assert result != [], message


@pytest.mark.negative_rectangle
def test_size_side_less_than_zero():
    less_than_zero = Rectangle(4, [-10, 60, 10, 60], [90, 90, 90, 90])
    message_side = "All sides of the rectangle are greater than 0"
    result_side = less_than_zero.check_less_than_zero(less_than_zero.size_side)
    assert result_side != [], message_side


@pytest.mark.positive_rectangle
def test_correct_angles():
    correct_angles = Rectangle(4, [10, 60, 10, 60], [90, 90, 90, 90])
    message = "The size of the angles in the rectangle is not correct"
    result = correct_angles.sum_angles_triangle()
    assert result == SUM_ANGLES, message


@pytest.mark.negative_rectangle
def test_angle_is_zero():
    angle_is_zero = Rectangle(4, [10, 60, 10, 60], [90, 0, 90, 90])
    message = "No angle equal 0"
    result = angle_is_zero.check_is_not_zero(angle_is_zero.angles)
    assert result != [], message


@pytest.mark.negative_rectangle
def test_angle_is_not_num():
    angle_is_not_num = Rectangle(4, [10, 60, 10, 60], [90, '90', 90, 90])
    message = "All of the angles is numbers"
    result = angle_is_not_num.check_is_num(angle_is_not_num.angles)
    assert result != [], message


@pytest.mark.negative_rectangle
def test_angles_less_than_zero():
    less_than_zero = Rectangle(4, [10, 60, 10, 60], [90, -90, 90, 90])
    message_angles = "All angles of the rectangle are greater than 0"
    result_angles = less_than_zero.check_less_than_zero(less_than_zero.angles)
    assert result_angles != [], message_angles


@pytest.mark.negative_rectangle
@pytest.mark.parametrize('count_angle, max_count', [
    (Rectangle(4, [10, 60, 10, 60], [90, 90, 90]), MAX_COUNT_RECTANGLE),
    (Rectangle(4, [10, 60, 10, 60], [90, 90, 90, 90, 90]), MAX_COUNT_RECTANGLE)])
def test_count_elem_angle(count_angle, max_count):
    message = f"The number of angles is equal to {max_count}"
    result = count_angle.check_count_elem(count_angle.angles)
    assert result != max_count, message


@pytest.mark.positive_square
def test_square_check_by_sides():
    equilateral_square = Rectangle(4, [60, 60, 60, 60], [90, 90, 90, 90])
    result_len, result_sum = equilateral_square.check_repeating_elem(equilateral_square.size_side)
    message = 'There are pairs of different sizes of sides in the square'
    assert result_len == 1, message
    message_1 = 'Does not match the number of elem in pairs'
    assert result_sum == 4, message_1
