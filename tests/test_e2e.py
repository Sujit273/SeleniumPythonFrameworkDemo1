from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Testone(BaseClass):
    def test_e2e(self):
        homepage = HomePage(self.driver)
        checkoutpage =homepage.shopItem()
        products = checkoutpage.getCardTitle()

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                checkoutpage.getCardFooter(product).click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        confirmPage = checkoutpage.checkOutItems()

        ##  Below code are not added to POM
        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in successText


