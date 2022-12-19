#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PATH_TO_DRIVER = ChromeDriverManager().install()


def pytest_addoption(parser):
    """
    argparse-style options and ini-style config values, called once at the beginning of a test run.
    @param parser: to add command line options.
    """
    parser.addoption("--url", action="store", default="https://ya.ru", help='input ip address')
    parser.addoption("--status_code", action="store", default="200", help='status_code value')


@pytest.fixture
def params(request) -> dict:
    """
    :param request: request fixture is a special fixture providing information of the requesting test function
    :return: dictionary with data
    """
    params = {
              'url': request.config.getoption('--url'),
              'status_code': request.config.getoption('--status_code'),
              # 'showbrowser': request.config.getoption('--showbrowser')
    }


    return params


@pytest.fixture
def browser(params: dict):
    """
    :param params: dictionary with data (fixture)
    :type params: dict
    """
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--force-device-scale-factor=1")
    options.add_argument('--disable-dev-shm-usage')

    if not params['showbrowser']:
        options.add_argument('headless')

    driver = webdriver.Chrome(PATH_TO_DRIVER, options=options)
    driver.maximize_window()

    yield driver

    driver.close()
    driver.quit()
