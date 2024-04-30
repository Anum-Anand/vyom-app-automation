import sys
sys.path.append(r"C:\Users\anuma\Documents\LambdaTest\sw-lambdatest-automation\vymo_application_test")
import add_contact as acs


desired_caps = {
    "deviceName": "RZCW219MCQA",
    "platformName": "Android",
    "platformVersion": "14",
    "app": "C:\\Users\\anuma\\Downloads\\app-debug (1).apk",
    "autoGrantPermissions": 'true'
}

command_executor="http://127.0.0.1:4723/wd/hub"
print("test started")

# acs.check_cards_present_on_screen(desired_caps=desired_caps,command_executor=command_executor)
# acs.add_contacts_with_mandatory_fields(desired_caps=desired_caps,command_executor=command_executor,contact_name="test_123",phone="1122334455")
# acs.add_contact_with_all_fields(desired_caps=desired_caps,command_executor=command_executor,first_name="test",last_name="test2",phone1="123456",phone2="56789",email="test@test.com")
acs.cancel_saving_contact(desired_caps=desired_caps,command_executor=command_executor,contact_name="test",phone="12345")