import time
from pageObjects.productDetailsPage import ProductDetailsPage
from pageObjects.productsPage import ProductsPage
from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from utilities.baseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class Tests(BaseClass):

    def test_bug2(self):
        homePage = HomePage(self.driver)
        productsPage = ProductsPage(self.driver)
        productDetailsPage = ProductDetailsPage(self.driver)
        loginPage = LoginPage(self.driver)
        homePage.closeTutorialButton().click()
        homePage.findBugsButton().click()
        productsPage.shoesImageButton().click()
        productDetailsPage.emailField().send_keys("testLogin")
        productDetailsPage.passwordField().send_keys("testPassword")
        productDetailsPage.signInButton().click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        loginPage.singInButton().click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)

    def test_bug7(self):
        homePage = HomePage(self.driver)
        productsPage = ProductsPage(self.driver)
        loginPage = LoginPage(self.driver)
        homePage.findBugsButton().click()
        productsPage.greyJeansImageButton().click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)
        time.sleep(2)

    def test_bug14(self):
        homePage = HomePage(self.driver)
        productsPage = ProductsPage(self.driver)
        productDetailsPage = ProductDetailsPage(self.driver)
        #homePage.closeTutorialButton().click()
        homePage.findBugsButton().click()
        productsPage.shoesImageButton().click()
        productDetailsPage.signInButton().click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(5)

    def test_bug21(self):
        homePage = HomePage(self.driver)
        productsPage = ProductsPage(self.driver)
        productDetailsPage = ProductDetailsPage(self.driver)
        loginPage = LoginPage(self.driver)
        #homePage.closeTutorialButton().click()
        homePage.findBugsButton().click()
        productsPage.shoesImageButton().click()
        productDetailsPage.signInButton().click()
        time.sleep(2)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        loginPage.passwordMarkButton().click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)

    def test_bug23(self):
        homePage = HomePage(self.driver)
        productsPage = ProductsPage(self.driver)
        productDetailsPage = ProductDetailsPage(self.driver)
        #homePage.closeTutorialButton().click()
        homePage.findBugsButton().click()
        productsPage.shoesImageButton().click()
        productDetailsPage.allItemsButton().click()
        productsPage.blueTshirtButton().click()
        time.sleep(3)

