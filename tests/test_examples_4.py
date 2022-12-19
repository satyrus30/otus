#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
import requests


def get_status_code(params):
    return requests.get(params['url']).status_code


@pytest.mark.examples_4
def test_compare_status_code(params):
    response_status_code = str(get_status_code(params))

    assert response_status_code == params['status_code'], "the status code is not the same"
