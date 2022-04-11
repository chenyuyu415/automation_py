import pytest


@pytest.mark.usefixtures('b')
class Test_C:
    def test_cone(self):
        x = 'this'
        assert self.b in x

    def test_cwo(self):
        x = 'check'
        assert x
