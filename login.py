from playwright.sync_api import sync_playwright, Playwright, Page, Locator, APIRequestContext, APIRequest, Browser
from typing import List, Dict, Tuple
from rich import print
import time
from random import randint

class Login:
	def __init__(self, payload: Dict[str, str], starting_url: str):
		self._payload = payload
		self._starting_url = starting_url

	def random_sleep(self, start: int, end: int):
		value = randint(start, end)
		return value

	def login(self, page: Page) -> Page:
		# locate & insert the username
		loc1 = page.locator('input#id_login')
		time.sleep(self.random_sleep(2, 5))
		loc1.fill(self._payload['username'])

		# locate & insert the password
		loc2 = page.locator('input#id_password')
		time.sleep(self.random_sleep(0, 2))
		loc2.fill(self._payload['password'])

		# locate & click the password
		page.locator('button#signin_btn').click()

		page.wait_for_url('https://leetcode.com/')
		return page

	def start(self, playwright: Playwright) -> Tuple[Browser, Page]:
		# start a chromium instace, run it with the UI, and slow, launch a new page, go to login page
		chrome = playwright.chromium
		browser = chrome.launch(headless=False, slow_mo=50)
		context = browser.new_context()
		page = browser.new_page()
		page.goto(self._starting_url)
		initial_url = page.url
		main_page = self.login(page)

		# make sure that we land on the new page after the login page
		assert initial_url != main_page.url, "URL didn't change it should have."

		return browser, main_page 		

	
