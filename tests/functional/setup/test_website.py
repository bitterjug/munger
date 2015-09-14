import pytest

from pytest_bdd import scenario, given, when, then


@scenario('website.feature', 'I visit the website')
def test_website():
    pass


@given("The server is running")
def server():
    """ start server """
    pass


@when("I visit the site")
def visit_site(browser):
    """ load the site in the browser"""
    pass


@then("I see a webpage")
def test_page_visible(browser):
    assert False, "Write the test"
