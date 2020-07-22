# Abishrant Panday 2020
# Using Selenium to automate browser and access Instagram
# Make sure to install the proper chromedriver file!
# You'll need to turn off 2FA on Instagram or submit 2FA manually

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import TimeoutException
import chromedriver_binary
from bs4 import BeautifulSoup


def getHTML(username, password, target):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://www.instagram.com/accounts/login/")

    uInput = driver.find_element_by_css_selector("input[name='username']")
    pInput = driver.find_element_by_css_selector("input[name='password']")

    uInput.send_keys(username)
    pInput.send_keys(password)

    login = driver.find_element_by_xpath("//button[@type='submit']")
    login.click()

    sleep(3)

    noSave = driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']")
    noSave.click()

    sleep(1)

    noNotif = driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
    noNotif.click()

    sleep(3)

    driver.get("https://www.instagram.com/" + target)
    followerTarget = "//a[@href='/{0}/followers/']/span[1]".format(target)
    followingTarget = "//a[@href='/{0}/following/']/span[1]".format(target)
    numFollowers = driver.find_element_by_xpath(followerTarget).text
    numFollowing = driver.find_element_by_xpath(followingTarget).text

    numFollowers1 = int(numFollowers.replace(',', ''))
    numFollowing1 = int(numFollowing.replace(',', ''))

    followers = driver.find_element_by_css_selector("a[href='/a.trash.bin/followers/']")
    followers.click()

    sleep(2)

    followerDialog = driver.find_element_by_xpath("//div[@class='isgrP']")
    scroll = 0
    while scroll < 135:
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', followerDialog)
        sleep(1)
        scroll += 1

    # dialog = driver.find_element_by_xpath("//div[@class='PZuss']")
    # numFollowers = int(driver.find_element_by_css_selector("span[class='g47SY ']").text)
    #
    # for i in range(int(numFollowers / 2)):
    #     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
    #     sleep(1)

    # currRows1 = len(driver.find_elements_by_css_selector("a[class='FPmhX notranslate  _0imsa ']"))
    # while True:
    #     driver.find_element_by_css_selector("a[class='FPmhX notranslate  _0imsa ']").send_keys(Keys.END)
    #     try:
    #         wait(driver, 5).until(
    #             lambda: len(driver.find_elements_by_css_selector("a[class='FPmhX notranslate  _0imsa ']")) > currRows1)
    #         currRows1 = len(driver.find_elements_by_css_selector("a[class='FPmhX notranslate  _0imsa ']"))
    #     except TimeoutException:
    #         break
    #
    # sleep(2)

    sleep(2)

    htmlFollowers = driver.page_source

    close = driver.find_element_by_css_selector("svg[aria-label='Close']")
    close.click()
    sleep(1)

    following = driver.find_element_by_css_selector("a[href='/a.trash.bin/following/']")
    following.click()

    sleep(2)

    htmlFollowing = driver.page_source

    sleep(10)
    driver.close()

    return numFollowing1, numFollowers1, htmlFollowing, htmlFollowers


print(getHTML('a.trash.bin', 'Animorphs2550#', "a.trash.bin"))
