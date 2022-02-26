from Pages.login_page import Login


class TestLogin:
    base_url = 'https://dev.abraplatform.com/'
    user_email = 'suriya.disha@brainstation-23.com'
    user_password = 'Abra@2023'

    def test_home_page(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        if actual_title == 'Abra':
            assert True
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_home_page.png")
            self.driver.quit()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = Login(self.driver)
        self.login_page.set_email(self.user_email)
        self.login_page.set_password(self.user_password)
        self.login_page.sign_in()
        actual_title = self.driver.title
        self.driver.quit()
        if actual_title == 'Abra':
            assert True
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.quit()
            assert False
