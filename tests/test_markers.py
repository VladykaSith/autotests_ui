import pytest

@pytest.mark.smoke
def test_some_case1():
    pass

@pytest.mark.regression
def test_some_case2():
    pass

@pytest.mark.smoke
class TestSuit1:
    def test_some_case3(self):
        pass

@pytest.mark.ui
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):
        pass

    def test_logout(self):
        pass

@pytest.mark.smoke
@pytest.mark.slow
@pytest.mark.regression
def test_critical_login():
    pass