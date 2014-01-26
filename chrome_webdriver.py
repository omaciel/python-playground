from selenium import webdriver

capabilities = webdriver.chrome.options.DesiredCapabilities.CHROME
capabilities["intl.accept_languages"] = "fr"

options = webdriver.chrome.options.Options()
options.add_experimental_option("intl.accept_languages", "fr")

driver = webdriver.Chrome(desired_capabilities=capabilities)
driver = webdriver.Chrome(chrome_options=options)
