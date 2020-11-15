#联系人详情页面
from appium.webdriver.common.mobileby import MobileBy

from test_app_po.page.basepage import BasePage
from test_app_po.page.editmempage import EditMempage


class DetailMem(BasePage):
    def dele_mem(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/i6d').click()
        return EditMempage(self.driver)