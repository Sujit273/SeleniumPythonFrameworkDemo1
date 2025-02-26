from selenium.webdriver.common.by import By

from PageObject.Checkoutpage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop= (By.CSS_SELECTOR, "a[href*='shop']")          #  //a[contains(@href,'shop')]    a[href*='shop']

    def shopItem(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)    #homepage.shopItem().click() #checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

