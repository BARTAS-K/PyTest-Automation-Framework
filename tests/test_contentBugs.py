import time
from pageObjects.myCartPage import MyCartPage
from pageObjects.productDetailsPage import ProductDetailsPage
from pageObjects.productsPage import ProductsPage
from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from utilities.baseClass import BaseClass

class Tests(BaseClass):

    def test_bug1(self):
        self.page(HomePage).closeTutorialButton().click()
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).signInButton().click()
        time.sleep(2)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.page(LoginPage).untranslatedLink().click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)

    def test_bug12(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).productDescription().click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)

    def test_bug16(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).addToCartButton().click()
        self.page(ProductsPage).viewCartButton().click()
        self.page(ProductDetailsPage).shoppingCartHover()
        time.sleep(5)
        self.page(ProductDetailsPage).shoppingCartPopUpButton()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)

    def test_bug19(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).professionalSuitImageButton().click()
        self.page(ProductDetailsPage).orangeColorButton().click()
        self.page(ProductDetailsPage).selectedColorButton().click()
        time.sleep(2)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)

    def test_bug20(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).shoppingCartHover()
        self.page(ProductDetailsPage).checkOutButton().click()
        self.page(MyCartPage).deleteItemButton().click()
        self.page(MyCartPage).returnToStoreButton().click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
