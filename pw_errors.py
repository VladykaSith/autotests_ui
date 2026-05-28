from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login", wait_until="networkidle")

    # unknown = page.locator("//div[contains(@class,'error')]")
    # expect(unknown).to_be_visible()

    # login_btn=page.get_by_test_id("login-page-login-button")
    # login_btn.fill('unknown')

    page.evaluate(
        f"""
            const title = document.getElementById('authentication-ui-course-title-text')
            title.textContent = 'text'
            """
    )