from playwright.sync_api import sync_playwright, expect

with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    email_input=page.locator('//label[contains(text(), "Email")]/following-sibling::div/input')
    email_input.fill("user.mail@gmail.com")
    password_input=page.locator('//input[@type="password"]')
    password_input.fill("1234")
    btn_login=page.locator('// button[contains(text(), "Login")]')
    btn_login.click()
    alert=page.locator('//div[@class="MuiAlert-icon css-1l54tgj"]/following-sibling::div[contains(text(),"Wrong email or password")]')
    text=alert.text_content()
    expect(alert).to_be_visible()
    expect(alert).to_have_text("Wrong email or password")
    print("I'm not surprised, motherfuckers!")
    page.wait_for_timeout(3000)

