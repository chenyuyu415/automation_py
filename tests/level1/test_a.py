import pytest
from lib.logger import log


@pytest.mark.model('CODA-5519')
# @pytest.mark.topology('gw', 'client')
@pytest.mark.usefixtures("driver")
class Test_A:

    def test_aone(self):
        self.driver.open("https://www.baidu.com")

    def test_awo(self):
        self.driver.input('id=kw', 123)


@pytest.mark.model('CODA-5519')
# @pytest.mark.topology('gw', 'client')
# @pytest.mark.usefixtures("driver", 'b')
class Test_AA:
    def test_aaone(self):
        log.info(self.config_name)

