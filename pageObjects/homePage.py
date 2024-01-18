from selenium.webdriver.common.by import By


class HomePage:
    closeTutorial = (By.XPATH, "//*[@id='TourTip0']/button")
    findBugs = (By.XPATH, "//*[@id='menu-item-561']/a")

    def __init__(self, driver):
        self.driver = driver

    def closeTutorialButton(self):
        return self.driver.find_element(*HomePage.closeTutorial)
    def findBugsButton(self):
        return self.driver.find_element(*HomePage.findBugs)