import pytest
from lib.logger import log


@pytest.mark.usefixtures("driver", 'b')
class Test_A:

    def test_aone(self):
        self.driver.open("https://www.baidu.com")
        log.info(self.b)

    def test_awo(self):
        self.driver.input('id=kw', 123)


@pytest.mark.usefixtures("driver")
class Test_AA:
    def test_aone(self):
        self.driver.open("https://www.baidu.com")
        log.info(self.driver)

    def test_awo(self):
        self.driver.input('id=kw', 123)
