from playwright.sync_api import sync_playwright, Playwright, Page, Locator, APIRequestContext, APIRequest, Request
from typing import List, Dict
from rich import print
import time
from random import randint

class SolvedProblems():

	def networkTracker(self, context):
		

	def navigateToSolvedProblems(self, page: Page, problemset_url: str):
		# go to the problemset page and wait for it to completely load
		page.goto(problemset_url)
		page.wait_for_url(problemset_url)

		selector = 'button#headlessui-menu-button-\\:r4\\:'
		button = page.locator(selector)
		button.click()
		print("Navigated to the status dropdown and clicked it.")

		page.get_by_role("menuitem", name="Solved").locator("div").first.click()
		print("Clicked on the solved so now lets access the network tab")



	# graphql_requests = []

	# 	def log_graphql_request(request):
	# 		if 'graphql' in request.url:
	# 			graphql_requests.append({
	# 				'headers' : request.all_headers()
	# 			})
    
	# 	# Set up network request logging
	# 	page.on('request', log_graphql_request)

	# # Wait for a short time to ensure all network requests are captured
	# 	page.wait_for_timeout(5000)

	# 	print("\nGraphQL Requests:")
	# 	for request in graphql_requests:
	# 		print(f"Headers: {request['headers']}")
	# 		# print(f"Post Data: {request['post_data']}")
	# 		# print("-" * 80)




		











