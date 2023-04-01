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

class TestNullPassword():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_nullPassword(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1366, 728)
    self.driver.find_element(By.ID, "user-name").click()
    self.driver.find_element(By.ID, "user-name").send_keys("1")
    self.driver.find_element(By.ID, "login-button").click()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h3")))
    assert self.driver.find_element(By.XPATH, "//div[@id=\'login_button_container\']/div/form/div[3]/h3").text == "Epic sadface: Password is required"
  
