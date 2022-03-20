from behave import *
from selenium import webdriver

from acceptance.page_model.blog_page import BlogPage
from acceptance.page_model.home_page import HomePage
from acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
   context.driver = webdriver.Chrome(r"C:\Users\kshie\Documents\testing\selenium-drivers\chromedriver.exe")
   page = HomePage(context.driver)
   # context.driver.get('http://127.0.0.1:5000/')
   context.driver.get(page.url) # this is the same thing as the commented out above

@given('I am on the blog page')
def step_impl(context):
   context.driver = webdriver.Chrome(r"C:\Users\kshie\Documents\testing\selenium-drivers\chromedriver.exe")
   page = BlogPage(context.driver)
   context.driver.get(page.url)

@given('I am on the new post page')
def step_impl(context):
   context.driver = webdriver.Chrome(r"C:\Users\kshie\Documents\testing\selenium-drivers\chromedriver.exe")
   page = NewPostPage(context.driver)
   context.driver.get(page.url)


@then('I am on the blog page')
def step_impl(context):
   expected_url = BlogPage(context.driver).url
   assert context.driver.current_url == expected_url

@then('I am on the homepage')
def step_impl(context):
   expected_url = HomePage(context.driver).url
   assert context.driver.current_url == expected_url

