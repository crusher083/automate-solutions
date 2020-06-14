from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://play2048.co/')
game = driver.find_element_by_tag_name('body')
direction = {0: Keys.UP, 1: Keys.RIGHT, 2: Keys.DOWN, 3: Keys.LEFT}
count = 0
driver.find_element_by_class_name('grid-container').click()
while True:
    count += 1
    game.send_keys(direction[count % 4])
