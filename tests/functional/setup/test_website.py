from pytest_bdd import scenario, given, when, then


@scenario('website.feature', 'I visit the website')
def test_website():
    pass


@given("The server is running")
def server():
    """ start server """
    return None


@when("I visit the site")
def visit_site(browser, server):
    """ load the site in the browser"""
    browser.visit(server.url)


@then("I see a webpage")
def page_visible(browser):
    assert not browser.find_by_tag('h1').is_empty()
