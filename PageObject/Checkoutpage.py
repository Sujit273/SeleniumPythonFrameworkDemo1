from selenium.webdriver.common.by import By

from PageObject.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver


    cardtitle = (By.XPATH,"//div[@class='card h-100']")         # products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    cardFooter = (By.XPATH,"div/button")                       # product.find_element(By.XPATH, "div/button").click()
    checkOut = (By.XPATH,"//button[@class='btn btn-success']")  #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardtitle)

    def getCardFooter(self,product_element):                                # The method getCardFooter(product_element) accepts the product element and uses it as the starting point for the
                                                                            # search. This ensures that the locator is relative to the specific product and returns the correct button element.
        return product_element.find_element(*CheckOutPage.cardFooter)       ## product.find_element(By.XPATH, "div/button").click()
                                                                            # return self.driver.find_elements(*CheckOutPage.cardFooter)
    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

    def pullrequesttest(self):
        pass


