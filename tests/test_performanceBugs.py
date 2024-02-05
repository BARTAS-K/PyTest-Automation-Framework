import time
from pageObjects.productDetailsPage import ProductDetailsPage
from pageObjects.productsPage import ProductsPage
from pageObjects.homePage import HomePage
from pageObjects.myAccountPage import MyAccountPage
from utilities.baseClass import BaseClass


class Tests(BaseClass):

    def test_bug6(self):
        self.page(HomePage).closeTutorialButton().click()
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).hotItemImageButton().click()
        self.page(ProductDetailsPage).loadingIconButton(ProductDetailsPage.loadingIcon1).click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)
        time.sleep(2)

    def test_bug11(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).mySpaceButton().click()
        self.page(ProductDetailsPage).loadingIconButton(ProductDetailsPage.loadingIcon2).click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)
        time.sleep(2)

    def test_bug15(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).emailField().send_keys("bob@bob.us")
        self.page(ProductDetailsPage).passwordField().send_keys("Thisisbob")
        self.page(ProductDetailsPage).signInButton().click()
        time.sleep(2)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.page(MyAccountPage).loadingIcon3Button().click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)
        time.sleep(2)
        self.page(MyAccountPage).signOut1Button().click()

    def test_bug17(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).emailField().send_keys("bob@bob.us")
        self.page(ProductDetailsPage).passwordField().send_keys("Thisisbob")
        self.page(ProductDetailsPage).signInButton().click()
        time.sleep(2)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).orderHistoryButton().click()
        self.page(MyAccountPage).loadingIcon4Button().click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.popUpClose(self.popUp2)
        time.sleep(2)
        self.page(MyAccountPage).signOut2Button().click()

    def test_bug18(self):
        self.page(HomePage).findBugsButton().click()
        self.page(ProductsPage).shoesImageButton().click()
        self.page(ProductDetailsPage).emailField().send_keys("bob@bob.us")
        self.page(ProductDetailsPage).passwordField().send_keys("Thisisbob")
        self.page(ProductDetailsPage).signInButton().click()
        time.sleep(2)
        self.popUpClose(self.popUp1)
        time.sleep(2)
        self.page(MyAccountPage).billingInformationButton().click()
        self.page(MyAccountPage).countryMenu().click()
        self.page(MyAccountPage).australiaOption().click()
        self.page(MyAccountPage).firstNameField().send_keys("Bob")
        self.page(MyAccountPage).lastNameField().send_keys("McBooba")
        self.page(MyAccountPage).addressField().send_keys("High Street")
        self.page(MyAccountPage).cityField().send_keys("Sydney")
        self.page(MyAccountPage).stateMenu().click()
        self.page(MyAccountPage).tasmaniaOption().click()
        self.page(MyAccountPage).zipCodeField().send_keys("1234")
        self.page(MyAccountPage).phoneField().send_keys("7777777777")
        self.page(MyAccountPage).updateButton().click()
        self.page(MyAccountPage).loadingIcon5Button().click()
        time.sleep(5)
        self.popUpClose(self.popUp1)
        time.sleep(2)