from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_btn=page.locator('//button[@data-testid="login-page-login-button"]')
    expect(login_btn).to_be_disabled()
    page.wait_for_timeout(2000)