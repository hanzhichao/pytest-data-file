import yaml
import pytest
import logging


def pytest_addoption(parser):
    parser.addoption('--data-file', help='yaml data file path in which test function name as top key')
    parser.addini('data_file', help='yaml data file path in which test function name as top key')


@pytest.fixture(scope='session')
def data(request):
    data_file = request.config.getoption('--data-file') or request.config.getini('data_file')
    try:
        with open(data_file, encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except Exception as ex:
        logging.exception(ex)
        pytest.skip(str(ex))
    else:
        return data


@pytest.fixture
def test_data(request, data):
    case_name = request.function.__name__
    return data.get(case_name)
