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

class TestLogout():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_logout(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.maximize_window()
    WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.ID, "user-name")))
    self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.ID, "password")))
    self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    self.driver.find_element(By.ID, "login-button").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
    self.driver.find_element(By.ID, "react-burger-menu-btn").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "logout_sidebar_link")))
    self.driver.find_element(By.ID, "logout_sidebar_link").click()
    assert self.driver.current_url=="https://www.saucedemo.com/"
