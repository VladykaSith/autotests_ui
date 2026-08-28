import time, pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import sync_playwright, Page, Playwright
from fixtures.pages import registration_page
from pages.authentication.registration_page import RegistrationPage
from allure_commons.types import AttachmentType
from tools.playwright.pages import initialize_playwright_page
from config import settings


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright):
    yield from initialize_playwright_page(playwright=playwright, test_name=request.node.name, storage_state=None)

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email=settings.test_user.email, username=settings.test_user.username, password=settings.test_user.password)
    registration_page.click_registration_button()
    time.sleep(0.5)
    context.storage_state(path="browser-state.json")
    browser.close()

@pytest.fixture
def chromium_page_with_state(request:SubRequest, initialize_browser_state, playwright: Playwright):
    yield from initialize_playwright_page(playwright=playwright, test_name=request.node.name, storage_state=settings.browser_state_file)
