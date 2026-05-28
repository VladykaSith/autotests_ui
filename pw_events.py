from playwright.sync_api import sync_playwright, expect, Request, Response


def log_reqeust(request: Request):
    print(f'Request: {request.url}')

def log_response(response: Response):
    print(f'Response: {response.url}')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    page.on('request', log_reqeust)
    page.on('response', log_response)

    page.wait_for_timeout(2000)