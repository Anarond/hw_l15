import pytest
from selene import browser, have

@pytest.mark.parametrize(
    "window_size",
    [(1366, 768), (1600, 900)],
    indirect=True
)
@pytest.mark.parametrize(
    "browser_name",
    [pytest.param('chrome'), pytest.param('firefox', marks=pytest.mark.skip)],
    indirect=True
)
def test_override_window_size_indirectly(desktop_browser, browser_name):
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.should(have.url_containing("/login"))