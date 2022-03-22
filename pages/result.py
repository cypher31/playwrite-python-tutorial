from turtle import title
from playwright.sync_api import Page
from typing import List

class DuckDuckGoResultPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.result_link = page.locator('.result__title a.result__a')
        self.search_input = page.locator('#search_form_input')

    def result_link_titles(self) -> List[str]:
        self.result_link.nth(4).wait_for()
        return self.result_link.all_text_contents()

    def result_link_titles_contain_phrase(self, phrase: str, minimum: int = 1) -> bool:
        titles = self.result_link_titles()
        matches = [t for t in titles if phrase.lower() in t.lower()]
        return len(matches) >= minimum