from selenium.webdriver.common.by import By
from utilities.logger import Logger


class ProductsPage(Logger):

    shoesImage = (By.XPATH, "//*[@id='ec_product_image_effect_4481370']")
    greyJeansImage = (By.XPATH, "//*[@id='ec_product_image_effect_4281370']/a")
    blueTshirt = (By.XPATH, "//*[@id='ec_product_image_effect_3481370']/a")
    addToCart = (By.XPATH, "//*[@id='ec_add_to_cart_27']")
    viewCart = (By.XPATH, "//*[@id='ec_product_page']/div[2]/a")
    professionalSuitImage = (By.XPATH, "//*[@id='ec_product_image_effect_3981370']/a")
    numberOfResults = (By.XPATH, "//*[@id='ec_product_page']/div[1]/span[1]/a[3]")
    denimCoat = (By.XPATH, "//*[@id='ec_product_image_effect_4381370']/a")

    def __init__(self, driver):
        self.driver = driver

    def shoesImageButton(self):
        self.getLogger().info("Clicking on \"DNK YELLOW SHOES\" image button")
        return self.driver.find_element(*ProductsPage.shoesImage)

    def greyJeansImageButton(self):
        self.getLogger().info("Clicking on \"DARK GREY JEANS\" image button")
        return self.driver.find_element(*ProductsPage.greyJeansImage)

    def blueTshirtButton(self):
        self.getLogger().info("Clicking on \"BLUE TSHIRT\" image button")
        return self.driver.find_element(*ProductsPage.blueTshirt)

    def addToCartButton(self):
        self.getLogger().info("Clicking on \"ADD TO CART\" button")
        return self.driver.find_element(*ProductsPage.addToCart)

    def viewCartButton(self):
        self.getLogger().info("Clicking on \"VIEW CART\" button")
        return self.driver.find_element(*ProductsPage.viewCart)

    def professionalSuitImageButton(self):
        self.getLogger().info("Clicking on \"PROFESSIONAL SUIT\" image button")
        return self.driver.find_element(*ProductsPage.professionalSuitImage)

    def numberOfResultsButton(self):
        self.getLogger().info("Clicking on different number of results")
        return self.driver.find_element(*ProductsPage.numberOfResults)

    def denimCoatImageButton(self):
        self.getLogger().info("Clicking on \"DENIM COAT\" image button")
        return self.driver.find_element(*ProductsPage.denimCoat)