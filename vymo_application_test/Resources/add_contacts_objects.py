from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


contacts_available_in_friends = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[2]"

friends = "//android.widget.TextView[@text='Friends']"
family = "//android.widget.TextView[@text='Family']"
work = "//android.widget.TextView[@text='Work']"
emergency = "//android.widget.TextView[@text='Emergency']"
clients = "//android.widget.TextView[@text='Clients']"
vendors = "//android.widget.TextView[@text='Vendors']"
friends_view_all = '(//android.view.ViewGroup[@content-desc="VIEW ALL"])[1]/android.widget.TextView'
family_view_all = '(//android.view.ViewGroup[@content-desc="VIEW ALL"])[2]/android.widget.TextView'

plus_button = "+"
add_contacts = "Add Contact"

first_name = '//android.widget.EditText[@text="First Name *"]'
last_name = '//android.widget.EditText[@text="Last Name"]'
phone_1 = '//android.widget.EditText[@text="Phone 1 *"]'
phone_2 = '//android.widget.EditText[@text="Phone 2"]'
email= '//android.widget.EditText[@text="Email"]'
select_types = '//android.widget.TextView[@text="Select Types"]'
friends_accessibility_id = "Friends"
close = 'Close'

save = "SAVE"
cancel = "CANCEL"

error_message = "//android.widget.TextView[@text='First Name, Phone 1, and Type cannot be empty.']"
ok_btn = "android:id/button1"
second_element_in_contact = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup"
back_btn = "Back"
cancel_btn_text = "//android.widget.TextView[@text='Cancelling will discard any changes.']"

def get_cards(driver,card_value):
    try:
        ans = '//android.widget.TextView[@text="'
        answer = ans + card_value + '"]'
        return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.XPATH,answer)))
    except:
        msg = card_value, "is not present"
        return msg

def get_contacts_available_in_friends(driver):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.XPATH, contacts_available_in_friends)))


def get_friends(driver):
    try:
        return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.XPATH, friends)))
    except:
        return "friends card not found"

def get_family(driver):
    try:
        return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.XPATH, family)))
    except:
        return "family card not found"

def get_work(driver):
    try:
        return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.XPATH, work)))
    except:
        return "work card not found"

def get_emergency(driver):
    try:
        return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.XPATH, emergency)))
    except:
        return "emerrgency card not found"

def get_clients(driver):
    try:
        return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.XPATH, clients)))
    except:
        return "clients card not found"


def get_vendors(driver):
    try:
       return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.XPATH, vendors)))
    except:
        return "vendors card not found"

def get_friends_view_all(driver):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.XPATH, friends_view_all)))


def get_family_view_all(driver):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.XPATH, family_view_all)))


def get_plus_button(driver):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, plus_button)))


def get_add_contacts(driver):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, add_contacts)))


def get_first_name(driver):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.XPATH, first_name)))


def get_last_name(driver):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.XPATH, last_name)))


def get_phone_1(driver):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.XPATH, phone_1)))


def get_phone_2(driver):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.XPATH, phone_2)))


def get_email(driver):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.XPATH, email)))


def get_select_types(driver):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.XPATH, select_types)))


def get_friends_accessibility_id(driver):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, friends_accessibility_id)))


def get_close(driver):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, close)))


def get_save(driver):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, save)))


def get_cancel(driver):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, cancel)))


def get_error_message(driver):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.XPATH, error_message)))


def get_ok_btn(driver):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.ID, ok_btn)))

    
def get_contact_saved(driver,contact):
    try:
        return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.XPATH,second_element_in_contact)))
    except:
        msg = contact, "is not present"
        return msg


def get_cancel_btn_text(driver):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((MobileBy.XPATH, cancel_btn_text)))

    