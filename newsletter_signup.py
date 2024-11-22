from selenium import webdriver
from selenium.webdriver.common.by import By
from decouple import Config

user_first_name: str = Config("USER_FIRST_NAME")
user_last_name: str = Config("USER_LAST_NAME")
user_email: str = Config("USER_EMAIL")
website_signup: str = Config("WEBSITE_SIGNUP")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)
driver.get(website_signup)

try:
    user_input_fields = driver.find_elements(
        By.CSS_SELECTOR,
        value = "input"
    )
    if len(user_input_fields) < 3:
        raise ValueError("The number of valid fields was too few.")

except Exception as e:
    print(f"An error occured extracting the user input fields: {e}")

data_entry = [user_first_name, user_last_name, user_email]

try:
    for field, data in zip(user_input_fields, data_entry):
        if len(data) >= 3:
            field.send_keys(f"{data.capitalize()}")
        else:
            raise ValueError("The number of characters is too few.")
    
except ValueError as e:
    print(f"An value error occurred: {e}")

except Exception as e:
    print(f"An error occurred: {e}")

else:
    sign_up_button = driver.find_element(
        By.CSS_SELECTOR,
        value = "button"
    )
    sign_up_button.click()

driver.quit()