from selenium import webdriver
import os 
import time

# Arguments to ignore the repeated SSL error. Copy of error below
# 'ERROR:ssl_client_socket_impl.cc(963)] handshake failed; returned -1, SSL error code 1, net_error -101' error
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=options)

class InstagramBot: 

    def __init__(self, username, password):
        """"
        Function which initialises ChromeDriver and logs into Instagram using the login function.

        Args:
            username:str: the Instagram username 
            password:str: the Instagram password 

        Attributes:
            driver:Seleniun.webdriver.Chrome: ChromeDriver that's used to automate browser actions
        
        """

        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome('chromedriver.exe')

        self.login()


    def login(self):
        """
        Function which opens an Instagram instance, logs in, and gets through all the popups.

        Args:
            self: referenced in the __init__ function. I still don't 100% know what this does. 

        """

        self.driver.get('{}/accounts/login'.format(self.base_url))
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
        time.sleep(1)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]   ').click()


    def nav_user(self, user):
        """
        Function which navigates to a specified Instagram user. 
        """

        self.driver.get('{}/{}'.format(self.base_url, user))


    def follow_user (self, user):
        """
        Functions which follows a user. 
        """

        self.nav_user(user)

        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0].click()


# Specifies what username and password to use (based on the InstagramBot class)
# If the code is run using 'python3 bot.py' 
if __name__ == '__main__':
    ig_bot = InstagramBot('<ENTER_USERNAME','ENTER_PASSWORD')

    # ig_bot.nav_user('shahkaar.co.uk')

    ig_bot.follow_user('shahkaar.co.uk')