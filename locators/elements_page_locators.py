from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    #form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "input[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "input[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "input[id='submit']")

    #created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURREND_ADRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADRESS = (By.CSS_SELECTOR, "#output #permanentAddress")
