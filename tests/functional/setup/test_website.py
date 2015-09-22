import pytest
from pytest_bdd import scenario, given, when, then
from webapp.apprunner import start, stop


@pytest.yield_fixture
def app():
    yield start()
    stop()


@scenario('website.feature', 'I visit the website')
def test_website():
    pass


@given("The server is running")
def server(app):
    """ start server """
    pass


@when("I visit the site")
def visit_site(browser, app):
    """ load the site in the browser"""
    browser.visit(app)


@then("I see a webpage")
def page_visible(browser):
    assert browser.status_code.is_success()
    assert not browser.find_by_tag('h1').is_empty()
