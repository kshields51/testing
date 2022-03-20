from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from acceptance.locators.blog_page import BlogPageLocators

use_step_matcher('re')

@given('I wait for the posts to load') # why is this not and hmmmm
def step_impl(context):
    try:
        WebDriverWait(context.driver, 5).until(
            expected_conditions.visibility_of_element_located(BlogPageLocators.POSTS_SECTION)
        )
    except:
        print('there is nothing here')
        raise
        # log something



