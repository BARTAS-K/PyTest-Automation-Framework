import pytest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from pageObjects.homePage import HomePage


@pytest.mark.usefixtures("setup")
class BaseClass:

    popUp1 = "//*[@id='popmake-4406']/button"
    popUp2 = "//*[@id='popmake-4393']/button"

    def popUpClose(self, popUp): #should this be in a different file in utilities?
        button = self.driver.find_element(By.XPATH, popUp)
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(button, 50, 50)
        action.click()
        action.perform()

    def page(self, page):
        pageObject = page(self.driver)
        return pageObject
