#个人信息删除页面
from appium.webdriver.common.mobileby import MobileBy

from test_app_po.page.basepage import BasePage


class EditDelepage(BasePage):
    def delemem(self):
        from test_app_po.page.searchmem import SearchMem
        self.find(MobileBy.ID, 'com.tencent.wework:id/elh').click()
        self.find(MobileBy.ID,'com.tencent.wework:id/blx').click()
        return SearchMem(self.driver)
