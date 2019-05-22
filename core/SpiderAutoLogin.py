# -*- encoding: utf-8 -*-
"""
@File    : SpiderAutoLogin.py
@Time    : 2019/5/22 7:39
@Author  : jiaxing liu
@Email   : 1260968291@qq.com
@Software: PyCharm
"""
from selenium import webdriver
import time
import random
class SpiderAutoLogin(object):

    urlSportExam = "http://www.fdty.fudan.edu.cn/sportexam/"
    urlExam = "http://www.fdty.fudan.edu.cn/sportexam/stexamV1.aspx"

    def __init__(self):
        """
        Initialize the chrome driver.
        """
        self.driver = webdriver.Chrome(executable_path=(r'../resource/chromedriver.exe'))

    def __toLogin(self):
        """
        To login page
        :return:
        """
        self.driver.get(self.urlSportExam)
        submit = self.driver.find_element_by_name("Button1")
        submit.click()
        time.sleep(2 + random.randint(0,5))

    def __login(self, id, password):
        name = self.driver.find_element_by_id("IDToken1")
        pwd = self.driver.find_element_by_id("IDToken2")
        name.send_keys(id)
        pwd.send_keys(password)
        submit = self.driver.find_element_by_css_selector("table tr td a img")
        submit.click()
        time.sleep(2 + random.randint(0,5))

    def __exam(self):
        # start = self.driver.find_element_by_id("btnExam")
        # start.click()
        # time.sleep(2 + random.randint(0,5))
        cookies = self.driver.get_cookies()
        self.driver.get(self.urlExam)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        problems = self.driver.find_element_by_css_selector("div#Panel3").text.split(".")
        print(problems)

    def autoLogin(self,id,password):
        self.__toLogin()
        self.__login(id=id,password=password)
        self.__exam()






