from playwright.sync_api import sync_playwright, Playwright, Page, Locator, APIRequestContext, APIRequest
from typing import List, Dict
from rich import print
import time
from random import randint
import login
import solvedProblems

if __name__ == "__main__":
	payload = {
		'username' : '',
		'password' : ''
	}
	starting_url = 'https://leetcode.com/accounts/login/'
	problemset_url = 'https://leetcode.com/problemset/'
	with sync_playwright() as playwright:
		# 1. go to starting_url and first login with the given payload
		login_instance = login.Login(payload, starting_url)
		browser, main_page = login_instance.start(playwright)

		# 2. Same session as #1: problemset page -> status -> solved -> get that full graphql qry resp
		solved_problems_instance = solvedProblems.SolvedProblems()
		solved_problems_instance.navigateToSolvedProblems(main_page, problemset_url)

		browser.close()

