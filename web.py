from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time



def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Enable headless mode

    # Setup the Chrome WebDriver with headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": "/Users/ryanroth/Downloads/",  # Set download directory
        "download.prompt_for_download": False,  # Disable download prompt
        "download.directory_upgrade": True,  # Enable download directory upgrade
        "safebrowsing.enabled": True  # Enable safe browsing (optional)
    })
    return driver


def set_input_field(driver, selector, text):
    element = driver.find_element(By.CSS_SELECTOR, selector)
    element.clear()  
    element.send_keys(text)

# Function to click a button
def click_button(driver, selector):
    element = driver.find_element(By.CSS_SELECTOR, selector)
    element.click()

def click_button_xpath(driver, selector):
    element = driver.find_element(By.XPATH, selector)
    element.click()

def send_enter_to_input_field(driver, selector):
    element = driver.find_element(By.CSS_SELECTOR, selector)
    element.send_keys(Keys.ENTER)

def click_button_and_go_back(driver, button_selector):
    original_tab = driver.current_window_handle
    driver.find_element(By.CSS_SELECTOR, button_selector).click()
    time.sleep(1)  
    for window_handle in driver.window_handles:
        if window_handle != original_tab:
            driver.switch_to.window(window_handle)
            driver.close()
    
    driver.switch_to.window(original_tab)

def download(driver, link):
    navigate(driver)
    set_input_field(driver, "#gatsby-focus-wrapper > div > section.bg-white.p-4.border.border-solid.rounded.border-current.border-solid-clr.container.mx-auto > div > div > div > input", link)
    click_button_and_go_back(driver, "#gatsby-focus-wrapper > div > section.bg-white.p-4.border.border-solid.rounded.border-current.border-solid-clr.container.mx-auto > div > div > div > button")
    time.sleep(0.5)
    click_button_and_go_back(driver,"#gatsby-focus-wrapper > div > section > div > div > div.md\:ml-2 > div > div > table > tbody > tr:nth-child(1) > td.md\:p-\[10px\].p-2.text-center.border.border-gray-300.border-t-0.border-b-1.border-dcdfe4.leading-normal > button")
    click_button(driver, "#default-modal > div > div > div.p-4.md\:p-5.space-y-4 > div.text-center.mb-6 > a")
    time.sleep(2)
    
def navigate(driver):
    driver.get('https://y2meta.mobi/en2/youtube-to-mp3/')
    time.sleep(1)

