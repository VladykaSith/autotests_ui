import pytest

@pytest.mark.skip(reason="Фича в разарботке")
def test_feature_in_development():
    pass

@pytest.mark.skip(reason="Фича в разарботке")
class TestSuiteSkip:
    def test_feature_in_development1(self):
        pass

    def test_feature_in_development2(self):
        pass


