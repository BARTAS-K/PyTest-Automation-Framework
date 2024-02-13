from selenium.webdriver.common.by import By
from utilities.logger import Logger


class HomePage(Logger):

    closeTutorial = (By.XPATH, "//*[@id='TourTip0']/button")
    findBugs = (By.XPATH, "//*[@id='menu-item-561']/a")

    def __init__(self, driver):
        self.driver = driver

    def closeTutorialButton(self):
        self.getLogger().info("Closing tutorial button")
        return self.driver.find_element(*HomePage.closeTutorial)
    def findBugsButton(self):
        self.getLogger().info("Clicking on \"Find Bugs\" button")
        return self.driver.find_element(*HomePage.findBugs)