from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    login_email_input = page.get_by_test_id('login-form-email-input').locator('input')
    expect(login_email_input).to_be_visible()
    login_email_input.focus()

    for char in 'user@mail.com':
        page.keyboard.type(char, delay=100)

    page.keyboard.press('ControlOrMeta+A', delay=300)


    page.wait_for_timeout(2000)