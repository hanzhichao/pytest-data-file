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
    basedir = request.config.basedir
    data_file = request.config.getoption('--data-file') or request.config.getini('data_file')
    if data_file is None:
        pytest.skip('Not given --data-file or data_file ')
        return
    if not data_file.startswith('/') or ':' not in data_file:
        data_file = os.path.join(basedir, data_file)
    if not os.path.isfile(data_file):
        logging.warning('%s not a valid file' % data_file)
        return
    try:
        with open(data_file, encoding='utf-8') as f:
            if data_file.endswith('.json'):
                data = json.load(f)
            elif data_file.endswith('.yaml'):
                data = yaml.safe_load(f)
            else:
                raise ValueError('Only support .json and .yaml file')
    except Exception as ex:
        logging.exception(ex)
        pytest.skip(str(ex))
    else:
        return data


@pytest.fixture
def case_data(request, data):
    case_name = request.function.__name__
    return data.get(case_name)
