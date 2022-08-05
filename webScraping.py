from playwright.sync_api import Playwright, sync_playwright, expect
from datetime import date

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=false)
    context = browser.new_context()
    page = context.new_page()
    
    data_atual = date.today()
    print(data_atual)
    data = str(data_atual)
    
    page.goto("https://www.youtube.com/feed/trending?bp=4gINGgt5dG1hX2NoYXJOcw%3D%3D")
    time.sleep(10)
    
    a = page.locator("title-wrapper > h3").all_text_contents()
    d = page.locator('div#text > a').all_inner_texts()
    b = page.locator('#metadata-line > span:nth-child(2)').all_text_contents()
    c = page.locator('#metadata-line > span:nth-child(1)').all_text_contents()
    
    print(len(a))
    for i in range(len(a)):
        ids = data + a[i].strip()
        aa = a[i].strip()
        print(a[i].strip())
        print(b[i])
        print(c[i])