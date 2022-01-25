import email
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import datetime
import  Constants
import traceback
import random
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys




def register_email(webdriver):
    '''
    This is the first function,
    it loads the main page of shoe store
    and starts testing with different emails 
    on "Remind me of new shoes" field
    '''
    
    webdriver.get('https://rb-shoe-store.herokuapp.com')

    for emails in Constants.EMAIL:

        try:
            email = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
            email.send_keys(emails)

        except:
            print("Unable to find 'Remind me of new shoes' field")

        try:
            submit_button = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="remind_email_submit"]')))
        except:
            print("Unable to find 'Submit' button")
        submit_button.click()

        try:
            elementAssert = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="flash"]/div')))
            if emails is "":
                assert elementAssert.text == "Please enter an email address"
                print("Assert Passed with empty data")
            elif emails is not "":
                assert elementAssert.text == 'Thanks! We will notify you of our new shoes at this email: '+''.join(emails)
                print("Email " +''.join(emails) +" registered for notifications successfully on 'Remind me of new shoes' field")
                print("Assert Passed")
        except:
            print("Failed to register email " +''.join(emails) + " on 'Remind me of new shoes'")
            print("Assert Failed")

def check_promo_code(webdriver):
    '''
    On this function, we will check some
    promo codes
    I dont have the pattern to determine how is 
    a valid code. So, at the moment, this function
    only checks empty data or invalid data
    '''

    for pcodes in Constants.PROMO_CODES:

        try:
            codes = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.NAME, "promo_code")))
            codes.send_keys(pcodes)

        except:
            print("Unable to find 'Promotional Code' field")

        try:
            send_button = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="promo_code_submit"]')))
        except:
            print("Unable to find 'Submit' button")
        send_button.click()

        try:
            elementAssert = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="flash"]/div')))
            if pcodes is "":
                assert elementAssert.text == "Please enter a promotional code"
                print("Assert Passed with empty data")
            elif pcodes is not "":
                assert elementAssert.text == 'Invalid code format'
                print("Assert Passed "  + ''.join(pcodes))
        except:
            print("Assert Failed on promotional codes with " + ''.join(pcodes))


def check_buttons_main_menu(webdriver):
    '''
    On this function, we will check all
    the buttons on the main menu are 
    working, just the correct navigation
    '''

    for tabs in Constants.TABS:

        try:
            tab = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, tabs)))
        except:
            print("Unable to find button " + ''.join(tabs))

        tab.click()

        try:
            elementAssert = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/h2')))
            if tabs == "All Shoes":
                assert elementAssert.text == "All Shoes"
                print("Assert Passed on "+''.join(tabs) + " button")
            else:
                assert elementAssert.text == ''.join(tabs)+"'s Shoes"
                print("Assert Passed on "+''.join(tabs) + " button")
        except:
            print("Assert Failed on main menu with " + ''.join(tabs))

def check_brands(webdriver):
    '''
    On this function, we will check all
    the brands on the dropdown box, 
    just the correct navigation
    '''
    webdriver.get('https://rb-shoe-store.herokuapp.com')
    for brand in Constants.BRANDS:

        try:
            WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.ID,   "brand")))
            brandbox = Select(webdriver.find_element_by_id('brand'))
            
        except:
            print("Unable to find dropdown box for brands")

        try:
            brandbox.select_by_value(brand)
        except:
            print("Unable to find brand " +''.join(brand))

        try:
            search_button = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="search_button"]')))
        except:
            print("Unable to find 'Search' button")
        search_button.click()

        try:
            elementAssert = WebDriverWait(webdriver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/h2')))
            assert elementAssert.text == ''.join(brand)+"'s Shoes"
            print("Assert Passed on "+''.join(brand) + " brand")
        except:
            print("Assert Failed on dropdown box for brand " + ''.join(brand))
        webdriver.get('https://rb-shoe-store.herokuapp.com')