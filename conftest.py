import pytest
from selene import browser


@pytest.fixture(params=[(1920, 1080), (1536, 864), (375, 667), (390, 844)])
def window_size(request):
    return request.param


@pytest.fixture(params=['chrome', 'firefox'])
def browser_name(request):
    return request.param


@pytest.fixture
def desktop_browser(window_size, browser_name):
    width, height = window_size
    if width <= 1011:
        pytest.skip(f"Разрешение {width}x{height} — это мобилка, пропускаем десктопный тест")

    browser.config.driver_name = browser_name
    browser.config.window_width = width
    browser.config.window_height = height

    yield browser

    browser.quit()


@pytest.fixture
def mobile_browser(window_size, browser_name):
    width, height = window_size
    if width >= 1012:
        pytest.skip(f"Разрешение {width}x{height} — это десктоп, пропускаем мобильный тест")

    browser.config.driver_name = browser_name
    browser.config.window_width = width
    browser.config.window_height = height

    yield browser

    browser.quit()