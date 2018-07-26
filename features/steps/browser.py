from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import platform
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class drivers(object):
    Chrome = 'Chrome'
    Firefox = 'Firefox'
    PhantomJS = 'PhantomJS'


class Browser(object):
    base_url = ""

    def open(self, driver=drivers.Chrome):

        self.driver = webdriver.Chrome(executable_path="C:/Users/Admin/Project/test_case/venv/chromedriver_win32/chromedriver.exe")
        self.driver.set_window_size(1280, 800)
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)

    def close(self):
        self.driver.quit()

    def visit(self, location=''):
        url = 'https://www.n11.com'

        self.driver.get(str(url))

    def visit_other(self, location):
        self.driver.get(location)

    def find_by_id(self, selector):
        return self.driver.find_element_by_id(selector)

    def find_by_class(self, selector):
        return self.driver.find_element_by_class_name(selector)

    def find_by_element(self, selector):
        return self.driver.find_element(By.XPATH, selector)

    def find_script(self, selector):
        return self.driver.execute_script(selector)

    def find_get_url(self):
        return self.driver.current_url

    def get_save_screenshot(self, selector):
        return self.driver.save_screenshot(selector)


    def find_by_name(self, selector):
        Browser.page_reflesh(self)
        return self.driver.find_element_by_name(selector)

    def find_css_selector(self, selector):
        return self.driver.find_elements(By.CSS_SELECTOR, selector)

    def find_link(self, selector):
        return self.driver.find_element_by_link_text(selector)

    def find_double_click(self, selector):
        actionChains = ActionChains(self.driver)
        actionChains.double_click(self.driver.execute_script(selector)).perform()

    def find_css(self, selector):
        return self.driver.find_element_by_css_selector(selector)

    def find_xpath(self, selector):
        return self.driver.find_element_by_xpath(selector)

    def find_link(self, selector):
        Browser.page_reflesh(self)
        return self.driver.find_element_by_link_text(selector)

    def submmit_click(self):
        return self.driver.find_elements(By.XPATH, '//button[@type="submit"]')[0].click()

    def page_reflesh(self):
        announcement = self.driver.execute_script("return  document.getElementsByTagName('w-div')[0];")
        if announcement:
            return self.driver.execute_script("document.getElementsByTagName('w-div')[0].style.visibility = 'hidden';")
        else:
            pass

    def page_wait(self):
        return self.driver.implicitly_wait(00)

    def alert_accept(self):
        alert = self.driver.switch_to_alert()
        return alert.accept()

    def iframe(self, iframe):
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe)

    def switch_window(self):
        main_window = self.driver.current_window_handle
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

        # Put focus on current window which will, in fact, put focus on the current visible tab
        self.driver.switch_to_window(main_window)

        # do whatever you have to do on this page, we will just got to sleep for now
        time.sleep(2)

        # Close current tab
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')

        # Put focus on current window which will be the window opener
        self.driver.switch_to_window(main_window)
        self.driver.close()

    def get_page_title(self):
        return self.driver.title

    def double_click_id(self, selector):
        actionChains = ActionChains(self.driver)
        actionChains.double_click(self.find_by_id(selector)).perform()

    def find_tag_name(self,selector):
        return self.driver.find_elements_by_tag_name()
    def text_match(self,selector):
        return  self.driver.lin
