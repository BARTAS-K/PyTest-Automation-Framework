import time
from pageObjects.myCartPage import MyCartPage
from pageObjects.productDetailsPage import ProductDetailsPage
from pageObjects.productsPage import ProductsPage
from pageObjects.homePage import HomePage
from pageObjects.registerPage import RegisterPage
from utilities.baseClass import BaseClass


class Tests(BaseClass):

    def test_bug3(self):
        self.page(HomePage).closeTutorialButton().click()
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).currencyButton().click()
        self.page(ProductDetailsPage).eurOptionButton().click()
        time.sleep(10)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)
        time.sleep(2)

    def test_bug4(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).numberOfResultsButton().click()
        time.sleep(10)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)
        time.sleep(2)

    def test_bug9(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).commentTextField().send_keys("This is a comment")
        self.page(ProductDetailsPage).commentNameField().send_keys("Bob")
        self.page(ProductDetailsPage).commentEmailField().send_keys("bob@bob.us")
        self.page(ProductDetailsPage).commentWebsiteField().send_keys("Bob.com")
        self.page(ProductDetailsPage).postCommentButton().click()
        time.sleep(10)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)
        time.sleep(2)

    def test_bug24(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).signUpButton().click()
        self.page(RegisterPage).forgotPasswordButton().click()
        self.page(RegisterPage).retrievePasswordEmailField().send_keys("bob@bob.us")
        self.page(RegisterPage).retrievePasswordButton().click()
        time.sleep(10)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)
        time.sleep(2)

    def test_bug25(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).denimCoatImageButton().click()
        self.page(ProductDetailsPage).greenColorButton().click()
        self.page(MyCartPage).addQuantityButton().click()
        time.sleep(10)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)
        time.sleep(2)