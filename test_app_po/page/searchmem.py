#查询联系人页面
from appium.webdriver.common.mobileby import MobileBy

from test_app_po.page.basepage import BasePage
from test_app_po.page.detailmem import DetailMem


class SearchMem(BasePage):
    def search_shuru(self):
        ele2=self.find(MobileBy.ID, 'com.tencent.wework:id/gpg')
        return ele2
    def seach_mems(self,name):
        self.search_shuru().send_keys(name)
        elem1 =self.finds(MobileBy.XPATH,f'//*[contains(@class,"android.widget.TextView") and contains(@text,"{name}")]')
        return elem1
    def goto_detail_mem(self,name):
        self.seach_mems(name)[0].click()
        return DetailMem(self.driver)

