from appium.webdriver.common.mobileby import MobileBy

from test_app_po.page.addmem import AddMem

#通讯录页面
from test_app_po.page.basepage import BasePage


class ContactPage(BasePage):
    #添加方法
    def goto_addmem(self):
        self.find(MobileBy.XPATH,'//*[@text="添加成员"]').click()
        return AddMem(self.driver)
    #查询方法
    def serach_mem(self):
        from test_app_po.page.searchmem import SearchMem
        self.find(MobileBy.ID,'com.tencent.wework:id/i6n').click()
        return SearchMem(self.driver)