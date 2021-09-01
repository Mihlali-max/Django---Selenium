from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PlayerFormTest(LiveServerTestCase):
    selenium = webdriver.Chrome()
    selenium.get('http://127.0.0.1:8000/')