import os
import logging
import json
import yaml
import pytest


def pytest_addoption(parser):
    parser.addoption('--data-file', help='yaml data file path in which test function name as top key')
    parser.addini('data_file', help='yaml data file path in which test function name as top key')


@pytest.fixture(scope='session')
def data(request):
    basedir = request.config.rootdir
    data_file = request.config.getoption('--data-file') or request.config.getini('data_file')
    if not data_file:
        pytest.skip('--data-file or data_file not given')
    if not data_file.startswith('/') or ':' not in data_file:
        data_file = os.path.join(basedir, data_file)
    if not os.path.isfile(data_file):
        pytest.skip('%s not a valid file' % data_file)
    try:
        with open(data_file, encoding='utf-8') as f:
            if data_file.endswith('.json'):
                data = json.load(f)
            elif data_file.endswith('.yaml'):
                data = yaml.safe_load(f)
            else:
                pytest.skip('Only support .json and .yaml file')
    except Exception as ex:
        logging.exception(ex)
        pytest.skip(str(ex))
    else:
        return data


@pytest.fixture
def case_data(request, data):
    case_name = request.function.__name__
    return data.get(case_name)
