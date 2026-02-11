from selene import have, by


def test_github_desktop(desktop_browser):
    browser = desktop_browser
    browser.open("https://github.com/")

    browser.element(".HeaderMenu-link--sign-in").click()
    browser.should(have.url_containing("/login"))


def test_github_mobile(mobile_browser):
    browser = mobile_browser
    browser.open("https://github.com/")

    browser.element(".flex-lg-row.flex-items-center button[type='button']").click()
    browser.element(by.text("Sign in")).click()
    browser.should(have.url_containing("/login"))