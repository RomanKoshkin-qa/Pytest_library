import pytest

#ФИКСТУРЫ ПРЕДУСЛОВИЯ
@pytest.fixture(scope='session')
def browser():
    print('Браузер!')

    yield

    print('Закрываем Браузер!')