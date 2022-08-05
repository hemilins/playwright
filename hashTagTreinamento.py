from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False) #headless
    pagina = navegador.new_page()
    pagina.goto("https://www.hashtagtreinamentos.com/curso-python")
    pagina.fill('xpath=//*[@id="_form_1919_"]/div[1]/div[1]/div/input', 'Hemili');
    pagina.fill('xpath=//*[@id="_form_1919_"]/div[1]/div[2]/div/input', 'hemilins@hotmail.com');    
    pagina.locator('xpath=//*[@id="_form_1919_submit"]').click();    
    time.sleep(15)
    
    
     