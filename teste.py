from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://quotes.toscrape.com/')
        
        heading = page.query_selector('//h1/a')
        #print(heading.inner_text())
        login = page.query_selector('[href="/login"]')
        login.click()
        
        user_input = page.query_selector('[id="username"]')
        user_input.type("user")
        
        pass_input = page.query_selector('//*[text()="Password"]/following-sibling::*')
        pass_input.type('text')
        
        page.query_selector('type="submit"').click()
        
        selector = '//*[@href="/logout"]'
        try: 
          logout = page.wait_for_selector(selector, timeout=5000)
        except:
            print('the login failed')
        print(logout.inner_text())
        #page.wait_for_timeout(5000)
        
        browser.close()
        
if __name__ == '__main__':
    main()