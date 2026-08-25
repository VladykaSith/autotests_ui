import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("AUTOUSE")

@pytest.fixture(scope="session")
def settings():
    print("SETTINGS")

@pytest.fixture(scope="class")
def user():
    print("USER")

@pytest.fixture(scope="function")
def browser():
    print("FUNCTION")



class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        print("USER CAN_LOGIN")

    def test_user_can_create_course(self,settings, user, browser):
        print("USER CAN_CREATE_COURSE")

class TestAccountFlow:
    def test_user_account(self):
        print("USER ACCOUNT")

