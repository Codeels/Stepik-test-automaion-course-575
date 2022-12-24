import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language of web site")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language != "":
        print("\nstart browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language must be filled")
    yield browser
    print("\nquit browser..")
    browser.quit()