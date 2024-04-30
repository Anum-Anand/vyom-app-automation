import time
from appium import webdriver
import traceback
from appium.webdriver.common.touch_action import TouchAction
import sys

import Resources.add_contacts_objects as ac
sys.path.append(r"C:\Users\anuma\Documents\LambdaTest\sw-lambdatest-automation\vymo_application_test")

    
def check_cards_present_on_screen(desired_caps,command_executor):
    try:
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor=command_executor)
        print(driver)
        cards = ["Friends", "Family", "Work", "Emergency", "Clients", "Vendors"]
        for card in cards: 
            msg = card , "is not present"
            card_value = ac.get_cards(driver,card)
            if (card_value == msg):
                print(card,"card is not present on the screen")
            else:
                print(card," card is present on the screen")      
            
        driver.quit()
    except Exception as e:
        traceback.print_exc()
        driver.quit()

def error_check(driver):
    error_msg = ac.get_error_message(driver)
    print("getting error message after clicking on save btn by providing only first name",error_msg.text)

    click_ok = ac.get_ok_btn(driver)
    click_ok.click()

def add_contacts_with_mandatory_fields(desired_caps,command_executor,contact_name,phone):
    try:
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor=command_executor)
        print(driver)
        contacts_available = ac.get_contacts_available_in_friends(driver)
        contact_count = contacts_available.text
        print("contact_count present in Friends in beginning =",contact_count,type(contact_count))
        plus_icon = ac.get_plus_button(driver)
        plus_icon.click()

        add_btn = ac.get_add_contacts(driver)
        add_btn.click()

        first_name = ac.get_first_name(driver)
        first_name.click()
        time.sleep(2)
        first_name.send_keys(contact_name)
        print("first name added")

        save_btn = ac.get_save(driver)
        save_btn.click()
        print("trying to save without all mandatory fields")
        error_check(driver)

        phone_1 = ac.get_phone_1(driver)
        phone_1.click()
        phone_1.send_keys(phone)
        print("phone 1 has been provided")

        save_btn = ac.get_save(driver)
        save_btn.click()
        print("trying to save without all mandatory fields")
        error_check(driver)

        select_types = ac.get_select_types(driver)
        select_types.click()
        choose_friends = ac.get_friends_accessibility_id(driver)
        choose_friends.click()

        close = ac.get_close(driver)
        close.click()
        save_btn = ac.get_save(driver)
        save_btn.click()

        contacts_available = ac.get_contacts_available_in_friends(driver)
        contact_count_after_adding_new_contact = contacts_available.text
        print("contact count present after adding a new contact = ",contact_count_after_adding_new_contact)
        if int(contact_count_after_adding_new_contact) == (int(contact_count)+1):
            print("contact added")
            print("contact count before adding new contact = ",contact_count, " and contact count after adding new contact = ",contact_count_after_adding_new_contact)
            print("count has been increased by 1")
        friends_view_all = ac.get_friends_view_all(driver)
        friends_view_all.click()
        contact_saved = ac.get_contact_saved(driver,contact_name)
        contact_saved_verify = contact_name, "is not present"
        if contact_saved == contact_saved_verify:
            print("new contact added not found in the list")
        else:
            print("new contact added founded in the list")
        driver.quit()
    except Exception as e:
        traceback.print_exc()
        driver.quit()


def add_contact_with_all_fields(desired_caps,command_executor,first_name,last_name,phone1,phone2,email):
    try:
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor=command_executor)
        print(driver)
        contacts_available = ac.get_contacts_available_in_friends(driver)
        contact_count = contacts_available.text
        print("contact_count present in Friends in beginning =",contact_count,type(contact_count))
        plus_icon = ac.get_plus_button(driver)
        plus_icon.click()

        add_btn = ac.get_add_contacts(driver)
        add_btn.click()

        f_name = ac.get_first_name(driver)
        f_name.click()
        f_name.send_keys(first_name)
        print("first name added")

        l_name = ac.get_last_name(driver)
        l_name.click()
        l_name.send_keys(last_name)
        print("last name added")

        phone_1 = ac.get_phone_1(driver)
        phone_1.click()
        phone_1.send_keys(phone1)
        print("phone 1 has been provided")  

        phone_2 = ac.get_phone_2(driver)
        phone_2.click()
        phone_2.send_keys(phone2)
        print("phone 2 has been provided") 

        email_address = ac.get_email(driver)
        email_address.click()
        email_address.send_keys(email)
        print("email has been provided")  

        select_types = ac.get_select_types(driver)
        select_types.click()
        choose_friends = ac.get_friends_accessibility_id(driver)
        choose_friends.click()

        close = ac.get_close(driver)
        close.click()
        save_btn = ac.get_save(driver)
        save_btn.click()

        contacts_available = ac.get_contacts_available_in_friends(driver)
        contact_count_after_adding_new_contact = contacts_available.text
        print("contact count present after adding a new contact = ",contact_count_after_adding_new_contact)
        if int(contact_count_after_adding_new_contact) == (int(contact_count)+1):
            print("contact added")
            print("contact count before adding new contact = ",contact_count, " and contact count after adding new contact = ",contact_count_after_adding_new_contact)
            print("count has been increased by 1")
            
        driver.quit()
    except Exception as e:
        traceback.print_exc()
        driver.quit()


def cancel_saving_contact(desired_caps,command_executor,contact_name,phone):
    try:
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor=command_executor)
        print(driver)
        contacts_available = ac.get_contacts_available_in_friends(driver)
        contact_count = contacts_available.text
        print("contact_count present in Friends in beginning =",contact_count,type(contact_count))
        plus_icon = ac.get_plus_button(driver)
        plus_icon.click()

        add_btn = ac.get_add_contacts(driver)
        add_btn.click()

        first_name = ac.get_first_name(driver)
        first_name.click()
        time.sleep(2)
        first_name.send_keys(contact_name)
        print("first name added")

        phone_1 = ac.get_phone_1(driver)
        phone_1.click()
        phone_1.send_keys(phone)
        print("phone 1 has been provided")

        select_types = ac.get_select_types(driver)
        select_types.click()
        choose_friends = ac.get_friends_accessibility_id(driver)
        choose_friends.click()

        close = ac.get_close(driver)
        close.click()
        cancel_btn = ac.get_cancel(driver)
        cancel_btn.click()

        cancel_btn_text = ac.get_cancel_btn_text(driver)
        print("cancel button pop up is present", cancel_btn_text.text)
        cancel_submit = ac.get_ok_btn(driver)
        cancel_submit.click()

        contacts_available = ac.get_contacts_available_in_friends(driver)
        contact_count_after_cancelling_contact = contacts_available.text
        print("contact count present after adding a new contact = ",contact_count_after_cancelling_contact)
        if int(contact_count_after_cancelling_contact) == (int(contact_count)):
            print("contact is not added")
            print("contact count before adding new contact = ",contact_count, " and contact count after adding new contact = ",contact_count_after_cancelling_contact)
            print("count has not been changed")
            driver.quit()
    except Exception as e:
        traceback.print_exc()
        driver.quit()
