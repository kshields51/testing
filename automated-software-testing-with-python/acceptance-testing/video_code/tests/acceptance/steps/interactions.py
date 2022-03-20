from behave import *

from acceptance.page_model.base_page import BasePage

use_step_matcher('re')

@when('I click on the "(.*)" link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.navigation

    matching_links = [l for l in links if l.text == link_text] # a list of objects found by selenium where the text of the link is equal to the text that I've passed in

    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError() # we can do something else here if we want like log something to the console then raise the error. Of course raising an exception on any of these tests is going to fail the test. It is going to happen if we use this step somewhere where there is no link or if we spell the link text incorrectly
