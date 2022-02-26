from selenium.webdriver.common.by import By

class Login:
    email_id = 'email'
    password_id = 'password'
    sign_in_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, user_email):
        self.driver.find_element(By.ID, self.email_id).clear()
        self.driver.find_element(By.ID, self.email_id).send_keys(user_email)

    def set_password(self, user_password):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(user_password)

    def sign_in(self):
        self.driver.find_element(By.XPATH, self.sign_in_xpath).click()
