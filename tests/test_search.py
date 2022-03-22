from playwright.sync_api import expect, Page

def test_basic_duckduckgo_search(page: Page) -> None:
    # Given the DuckDuckGo home page is displayed
    page.goto('https://duckduckgo.com', wait_until='load')

    # When the user searchesss for a phrase
    page.locator('#search_form_input_homepage').fill('panda')
    page.locator('#search_button_homepage').click()

    # Then the search result query is the phrase
    expect(page.locator('#search_form_input')).to_have_value('panda')

    # And the search result links pertain to the phrase
    page.locator('.result__title a.result__a').nth(4).wait_for()
    titles = page.locator('.result__title a.result__a').all_text_contents()
    matches = [t for t in titles if 'panda' in t.lower()]
    assert len(matches) > 0

    # And the search result title contains the phrase
    expect(page).to_have_title('panda at DuckDuckGo')
    pass