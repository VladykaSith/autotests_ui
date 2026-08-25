import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize("number",[1,2,3,-1])
def test_number(number: int):
    assert number > 0

@pytest.mark.parametrize("number,exp_result", [(1,1),(2,4),(3,9)])
def test_number(number: int, exp_result: int):
    assert number**2 == exp_result

@pytest.mark.parametrize("os",["macos","windows","linux","debian"])
@pytest.mark.parametrize("browser",["chromium","webkit","firefox"])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os+browser) > 0

# Параметризированная фикстура
@pytest.fixture(params=["chromium","webkit","firefox"])
def browser(request: SubRequest):
    return request.param

def test_open_browser(browser: str):
    print(f'Running test on {browser}')

@pytest.mark.parametrize("user", ["Alice","Zara"])
class TestOperations:
    @pytest.mark.parametrize("account",["Credit card","Debit card"])
    def test_user_with_operations(self, user: str, account: str):
        print("Running user operations")

    def test_user_without_operations(self, user: str):
        print("Running user without operations")



users={
    "+70001": "user with money",
    "+70002": "user without money",
    "+70003": "user without money2"
}
@pytest.mark.parametrize(
    "phone_number",users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
    )
def test_identifiers(phone_number: str):
    pass

