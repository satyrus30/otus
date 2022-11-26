#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.heirs.circle import *
import array
import pytest


TYPE_VALUE = (int, float)
All_NEED_TYPES_OBJ = [['0', 60, 50], [None, 60, 50], [(123,), 60, 50], [{123, 'a'}, 60, 50], [True, 60, 50],
                      [{'a': 22}, 60, 50], array.array('i', [1, 2, 3])]


@pytest.mark.positive_circle
def test_correct_value_type():
    value_type = Circle(2, 4.5)
    radius, diameter = value_type.check_value_type()
    message = "The value of the data type passed in the object does not correspond to"
    assert radius in TYPE_VALUE, message


@pytest.mark.negative_circle
@pytest.mark.parametrize('radius', All_NEED_TYPES_OBJ)
@pytest.mark.parametrize('diameter', All_NEED_TYPES_OBJ)
def test_incorrect_value_type(radius, diameter):
    incorrect_value_type = Circle(radius, diameter)
    radius, diameter = incorrect_value_type.check_value_type()
    message = "In the values of the data types passed in the object the correct values are"

    assert type(radius) not in TYPE_VALUE or type(diameter) not in TYPE_VALUE, message


@pytest.mark.negative_circle
@pytest.mark.parametrize('radius', [0, -1])
@pytest.mark.parametrize('diameter', [0, -1])
def test_check_value_less_than_or_equal_zero(radius, diameter):
    incorrect_value_type = Circle(radius, diameter)
    radius, diameter = incorrect_value_type.get_value()
    message = "In the values of the data types passed in the object the correct values are"
    assert radius <= 0 or diameter <= 0, message


@pytest.mark.positive_circle
def test_check_diameter():
    check_diameter = Circle(2, 4)
    calculate_diameter = 2 * check_diameter.size_radius
    message = "The calculated diameter from the radius, does not correspond to the transferred in the object"
    assert calculate_diameter == check_diameter.diameter, message


@pytest.mark.negative_circle
@pytest.mark.parametrize('radius', [2])
@pytest.mark.parametrize('diameter', All_NEED_TYPES_OBJ)
def test_check_diameter(radius, diameter):
    check_diameter = Circle(radius, diameter)
    calculate_diameter = 2 * check_diameter.size_radius
    message = "The calculated diameter from the radius, does not correspond to the transferred in the object"
    assert calculate_diameter != check_diameter.diameter, message
