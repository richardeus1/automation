import Agent
import Constants


def init(webdriver):
    Constants.init()

def update(webdriver):
    #first we will check emails on "Remind me of new shoes" field 
    print("Testing 'Remind me of new shoes' field")
    Agent.register_email(webdriver)
    print("\n")
    print("\n")
    print("\n")
    #Then we will check promo codes on "Promotional Codes" field
    print("Testing 'Promotional Code' field")
    Agent.check_promo_code(webdriver)
    print("\n")
    print("\n")
    print("\n")
    #Then we will check main menu buttons
    print("Testing main menu buttons")
    Agent.check_buttons_main_menu(webdriver)
    print("\n")
    print("\n")
    print("\n")
    #Then we will check the brands on dropdown box
    print("Testing brands on dropdown box")
    Agent.check_brands(webdriver)



