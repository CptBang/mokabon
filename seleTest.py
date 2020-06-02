import urllib.request, re

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

    
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

driver.get('https://mangadex.org/chapter/848134')
delay = 10
try:
    myElem = WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='noselect nodrag cursor-pointer']")))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

    

# get the image source

images = driver.find_elements_by_tag_name('img')
for image in images:
    src = image.get_attribute('src')
    checkPage = re.match(r".*[0-9].png", src)
    if checkPage:
        print(src)
        butts = urllib.request.urlretrieve(src, "shitworkedbreh.jpg")

# src = img.get_attribute('src')

    

# # download the image



driver.quit()