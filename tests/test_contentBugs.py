import time
from utilities.baseClass import BaseClass
from pageObjects.productDetailsPage import ProductDetailsPage
from pageObjects.productsPage import ProductsPage
from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage

class Tests(BaseClass):

    def test_bug1(self):
        homePage = HomePage(self.driver)
        productsPage = ProductsPage(self.driver)
        productDetailsPage = ProductDetailsPage(self.driver)
        loginPage = LoginPage(self.driver)
        homePage.closeTutorialButton().click()
        homePage.findBugsButton().click()
        productsPage.shoesImageButton().click()
        productDetailsPage.signInButton().click()
        time.sleep(2)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        loginPage.untranslatedLink().click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)

    def test_bug12(self):
        homePage = HomePage(self.driver)
        productsPage = ProductsPage(self.driver)
        productDetailsPage = ProductDetailsPage(self.driver)
        homePage.findBugsButton().click()
        productsPage.shoesImageButton().click()
        productDetailsPage.productDescription().click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)

    def test_bug16(self):
        homePage = HomePage(self.driver)
        productsPage = ProductsPage(self.driver)
        productDetailsPage = ProductDetailsPage(self.driver)
        homePage.closeTutorialButton().click()
        homePage.findBugsButton().click()
        productsPage.addToCartButton().click()
        productsPage.viewCartButton().click()
        productDetailsPage.shoppingCartHover()
        time.sleep(5)
        #productDetailsPage.checkOutButton().click()
        productDetailsPage.shoppingCartPopUpButton().click() #doesnt work yet, need to find a solution
        time.sleep(5)
