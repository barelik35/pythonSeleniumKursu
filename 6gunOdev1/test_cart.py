# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCart():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cart(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.maximize_window()
    WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.ID, "user-name")))
    self.driver.find_element(By.CSS_SELECTOR, ".login_credentials_wrap-inner").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.ID, "user-name")))
    self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.ID, "password")))
    self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    self.driver.find_element(By.ID, "login-button").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_link")))
    self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "continue-shopping")))
    assert self.driver.current_url=="https://www.saucedemo.com/cart.html"