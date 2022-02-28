import pytest

from constants import URL, BROWSER
from driver.driver import Driver


@pytest.fixture(autouse=False)
def setup():
    try:
        driver = Driver(BROWSER)
        driver.get_driver().maximize_window()
        driver.get_driver().get(URL)
        yield driver.get_driver()
        driver.get_driver().close()
    except Exception as e:
        pytest.exit("Exception in fixture 'setup' : " + str(e))
