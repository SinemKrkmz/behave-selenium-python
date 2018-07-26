from features.steps.browser import Browser
from features.steps.DataModel.page_object import HomePage, SearchPage
import json
import time



class Actionwords:
    ConfigData = []
    def __init__(self):
        self.browser = Browser()
        data = open("C:/Users/Admin/Project/test_case/features/steps/Data/config.json", 'r')
        self.ConfigData = json.load(data)

    def got_web_site_p1(self, p1=""):
        self.browser.open()
        self.browser.driver.get(p1)

    def get_page_title(self):
        HomePage.home_page_title = self.browser.driver.title


    def title_is_shown(self,p1=""):
        return HomePage.home_page_title


    def i_click_link_giris_yap(self):
        self.browser.find_by_element("//*[@class=\"btnSignIn\"]").click()


    def i_enter_email(self):
        self.browser.find_by_id("email").send_keys(self.ConfigData["Base"]["email"])


    def i_enter_valid_password(self):
        self.browser.find_by_id("password").send_keys(self.ConfigData["Base"]["password"])


    def i_click_button_uye_girisi(self):
        self.browser.find_by_id("loginButton").click()


    def i_enter_search_text_samsung(self, samsung="Samsung"):
        self.browser.find_by_id("searchData").send_keys(samsung)


    def i_click_button_search(self):
        self.browser.find_by_class("searchBtn").click()


    def p1_search_is_shown(self, p1=""):
       return  self.browser.find_by_element("//*[@id='breadCrumb']/ul/li[2]/a/span").text


    def i_click_page_button_p1(self, p1=""):
        self.browser.find_by_element("//*[@class='pagination']/a["+p1+"]").click()


    def second_page_is_shown(self, p1=""):
       time.sleep(5)
       return self.browser.get_page_title().split("/", 1)[0]

    def add_third_product_to_favorites(self, third="3"):
        SearchPage.favori_product_name =self.browser.find_by_element("//*[@id=\"view\"]/ul/li["+third+"]/div/div/a/h3").text
        self.browser.find_by_element("//*[@id='view']/ul/li["+third+"]/div/div[2]/span[2]").click()


    def i_click_link_favorites(self):
        self.browser.find_script('document.getElementsByClassName("myAccountMenu hOpenMenu")[0].getElementsByTagName("div")[0].getElementsByTagName("a")[1].click();')

    def i_click_favorites_product(self):
        self.browser.find_by_element("//*[@id='myAccount']/div[3]/ul/li[1]/div/a/h4").click()
        time.sleep(5)
        SearchPage.selected_product_name = self.browser.find_by_element(
            "//*[@class=\"columnContent adBg\"]/div[1]/a/h3").text

    def shown_favorites_product(self):
        assert  SearchPage.selected_product_name == SearchPage.favori_product_name



    def delete_favorites_product(self):
        self.browser.find_by_element("//*[@class=\"columnContent adBg\"]/div[3]/span").click()

    def i_click_delete_tamam_button(self):
        self.browser.find_by_element("/html/body/div[5]/div/div/span").click()

    def product_deleted(self, p1=""):
        time.sleep(5)
        controlValue = False

        if p1 in self.browser.find_by_element("//*[@id='watchList']/div").text:
            return True
        return controlValue


