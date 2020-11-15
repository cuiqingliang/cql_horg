#主页面消息页
from appium.webdriver.common.mobileby import MobileBy

from test_app_po.page.basepage import BasePage
from test_app_po.page.contactpage import ContactPage


class MainPage(BasePage):
    def goto_contact(self):
        self.find(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        return ContactPage(self.driver)