from appium.webdriver.common.mobileby import MobileBy

from test_app_po.page.basepage import BasePage
from test_app_po.page.mualaddmem import MualAddmem

#添加成员页面，点击手工添加
class AddMem(BasePage):
    def goto_mualaddmem(self):
        self.find(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        return MualAddmem(self.driver)