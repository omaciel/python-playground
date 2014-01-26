from selenium import webdriver

profile = webdriver.firefox.firefox_profile.FirefoxProfile()
profile.set_preference("intl.accept_languages", "fr")

browser = webdriver.Firefox(profile)

browser.get("http://google.com")
