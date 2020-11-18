import logging

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

def load_date():
    with open('date.yaml',encoding='utf-8') as f:
        date=yaml.safe_load(f)
        date1=date['date']
        date2=date['steps']
        print(date1,date2)
        return date

class TestWX:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "True"
        # 最重要的代码，建立客户端与服务端的连接
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
    @pytest.mark.parametrize('name,gender,phonenum',load_date()['date'])
    #[{'name': ['cc', 'ee']}, {'gender': ['男', '男']}, {'phonenum': ['11211111111', '11211111112']}]
    def test_contact(self,name,gender,phonenum):
        # logging.basicConfig(level=logging.INFO)
        # name = "hogwarts_00003"
        # gender = "男"
        # phonenum = "13812121214"
        steps=load_date()['steps']
        # 点击【通讯录】
        for step in steps:
            if 'find_element' in step:
                by=str(step['find_element'][0])
                locator=str(step['find_element'][1])
                action=str(step['find_element'][2])
                if 'xpath' in by:
                    ele1=self.driver.find_element(MobileBy.XPATH,f'{locator}')
                if action=='click':
                    ele1.click()
                elif action=='send':
                    if '姓名' in locator:
                        ele1.send_keys(name['name'])
                    elif '手机号' in locator:
                        ele1.send_keys(phonenum['phonenum'])

                # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
                # # 点击【添加成员】
                #
                # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                #                          'new UiScrollable(new UiSelector()'
                #                          '.scrollable(true).instance(0))'
                #                          '.scrollIntoView(new UiSelector()'
                #                          '.text("添加成员").instance(0));').click()
                # # 点击【手动输入添加】
                # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
                # self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(
                #     name)
                # self.driver.find_element(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
                # if gender == "男":
                #     self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
                # else:
                #     self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
                #
                # self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phonenum)
                # self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
                # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']").click()
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert result == "添加成功"