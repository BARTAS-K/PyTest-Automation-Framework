from selenium.webdriver.common.by import By


class ProductsPage:

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
        return self.driver.find_element(*ProductsPage.shoesImage)

    def greyJeansImageButton(self):
        return self.driver.find_element(*ProductsPage.greyJeansImage)

    def blueTshirtButton(self):
        return self.driver.find_element(*ProductsPage.blueTshirt)

    def addToCartButton(self):
        return self.driver.find_element(*ProductsPage.addToCart)

    def viewCartButton(self):
        return self.driver.find_element(*ProductsPage.viewCart)

    def professionalSuitImageButton(self):
        return self.driver.find_element(*ProductsPage.professionalSuitImage)

    def numberOfResultsButton(self):
        return self.driver.find_element(*ProductsPage.numberOfResults)

    def denimCoatImageButton(self):
        return self.driver.find_element(*ProductsPage.denimCoat)