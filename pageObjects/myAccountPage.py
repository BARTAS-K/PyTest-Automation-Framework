from selenium.webdriver.common.by import By
from utilities.logger import Logger


class MyAccountPage(Logger):

    loadingIcon3 = (By.XPATH, "//*[@id='ec_account_dashboard']/div[2]/div[6]/span")
    loadingIcon4 = (By.XPATH, "//*[@id='ec_account_orders']/div[2]/div[2]/span")
    billingInformation = (By.XPATH, "//*[@id='ec_account_dashboard']/div[3]/div[2]/a")
    country = (By.XPATH, "//*[@id='ec_account_billing_information_country']")
    australia = (By.XPATH, "//*[@id='ec_account_billing_information_country']/option[4]")
    firstName = (By.XPATH, "//*[@id='ec_account_billing_information_first_name']")
    lastName = (By.XPATH, "//*[@id='ec_account_billing_information_last_name']")
    address = (By.XPATH, "//*[@id='ec_account_billing_information_address']")
    city = (By.XPATH, "//*[@id='ec_account_billing_information_city']")
    state = (By.XPATH, "//*[@id='ec_account_billing_information_state_AU']")
    tasmania = (By.XPATH, "//*[@id='ec_account_billing_information_state_AU']/option[11]")
    zipCode = (By.XPATH, "//*[@id='ec_account_billing_information_zip']")
    phone = (By.XPATH, "//*[@id='ec_account_billing_information_phone']")
    update = (By.XPATH, "//*[@id='ec_account_billing_information']/div[1]/form/div[12]/input")
    loadingIcon5 = (By.XPATH, "//*[@id='ec_account_billing_information']/div[1]/form/div[12]/span")
    signOut1 = (By.XPATH, "//*[@id='ec_account_dashboard']/div[3]/div[6]/a")
    signOut2 = (By.XPATH, "//*[@id='ec_account_orders']/div[3]/div[6]/a")

    def __init__(self, driver):
        self.driver = driver

    def loadingIcon3Button(self):
        self.getLogger().info("Clicking on the loading icon #3.")
        return self.driver.find_element(*MyAccountPage.loadingIcon3)

    def loadingIcon4Button(self):
        self.getLogger().info("Clicking on the loading icon #4.")
        return self.driver.find_element(*MyAccountPage.loadingIcon4)

    def billingInformationButton(self):
        self.getLogger().info("Clicking on the \"BILLING INFORMATION\" button.")
        return self.driver.find_element(*MyAccountPage.billingInformation)

    def countryMenu(self):
        self.getLogger().info("Clicking on the \"COUNTRY\" dropdown menu.")
        return self.driver.find_element(*MyAccountPage.country)

    def australiaOption(self):
        self.getLogger().info("Clicking on the \"AUSTRALIA\" option.")
        return self.driver.find_element(*MyAccountPage.australia)

    def firstNameField(self):
        self.getLogger().info("Entering data in the \"FIRST NAME\" field.")
        return self.driver.find_element(*MyAccountPage.firstName)

    def lastNameField(self):
        self.getLogger().info("Entering data in the \"LAST NAME\" field.")
        return self.driver.find_element(*MyAccountPage.lastName)

    def addressField(self):
        self.getLogger().info("Entering data in the \"ADDRESS\" field.")
        return self.driver.find_element(*MyAccountPage.address)

    def cityField(self):
        self.getLogger().info("Entering data in the \"CITY\" field.")
        return self.driver.find_element(*MyAccountPage.city)

    def stateMenu(self):
        self.getLogger().info("Clicking on the \"STATE\" dropdown menu.")
        return self.driver.find_element(*MyAccountPage.state)

    def tasmaniaOption(self):
        self.getLogger().info("Clicking on the \"TASMANIA\" option.")
        return self.driver.find_element(*MyAccountPage.tasmania)

    def zipCodeField(self):
        self.getLogger().info("Entering data in the \"ZIP CODE\" field.")
        return self.driver.find_element(*MyAccountPage.zipCode)

    def phoneField(self):
        self.getLogger().info("Entering data in the \"PHONE\" field.")
        return self.driver.find_element(*MyAccountPage.phone)

    def updateButton(self):
        self.getLogger().info("Clicking on the \"UPDATE\" button.")
        return self.driver.find_element(*MyAccountPage.update)

    def loadingIcon5Button(self):
        self.getLogger().info("Clicking on the loading icon #5.")
        return self.driver.find_element(*MyAccountPage.loadingIcon5)

    def signOut1Button(self):
        self.getLogger().info("Clicking on the \"SIGN OUT\" button.")
        return self.driver.find_element(*MyAccountPage.signOut1)

    def signOut2Button(self):
        self.getLogger().info("Clicking on the \"SIGN OUT\" button.")
        return self.driver.find_element(*MyAccountPage.signOut2)