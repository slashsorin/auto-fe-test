#-*- coding: utf-8 -*-
'''
    
    @author: Sorin

    Copyright Issuu Aps Sep 11, 2012
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class TestCanvas:
    def setup_method(self, method):
        self.firefox = webdriver.Firefox()

    def teardown_method(self, method):
        self.firefox.quit()

    def test_that_we_can_draw_on_canvas(self):
        self.firefox.get('http://www.theautomatedtester.co.uk/demo1.html')
        canvas = self.firefox.find_element_by_id("tutorial")
        drawing = ActionChains(self.firefox)\
                    .click_and_hold(canvas)\
                    .move_by_offset(-40, -60)\
                    .move_by_offset(30, 20)\
                    .move_by_offset(100, 200)\
                    .release(canvas)
        #Now we know what we want to happen, let's perform the actions
        drawing.perform()
