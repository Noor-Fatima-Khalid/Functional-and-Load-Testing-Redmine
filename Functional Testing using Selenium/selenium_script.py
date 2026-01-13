from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# CONFIG
URL = "http://localhost:3000"
USERNAME = "admin"
PASSWORD = "redminesqe"
NEW_PROJECT_NAME = "Selenium Test Project 4"
NEW_GROUP_NAME = "Test Group 1"
NEW_ENUM_NAME = "Activity 2"

# Initialize Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # Open Redmine homepage
    driver.get(URL)
    time.sleep(2)

    # Click "Sign in" link
    login_link = driver.find_element(By.LINK_TEXT, "Sign in")
    login_link.click()
    time.sleep(2)

    # Enter username and password
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys(USERNAME)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(PASSWORD)

    # Click login button
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()
    time.sleep(3)

    print("Login successful!")

    # Navigate to Projects page
    projects_link = driver.find_element(By.LINK_TEXT, "Projects")
    projects_link.click()
    time.sleep(2)
    print("Projects page opened!")

    # Create a new project
    try:
        new_project_btn = driver.find_element(By.LINK_TEXT, "New project")
        new_project_btn.click()
        time.sleep(2)

        # Enter project name
        name_input = driver.find_element(By.ID, "project_name")
        name_input.send_keys(NEW_PROJECT_NAME)

        # Click Create button
        create_btn = driver.find_element(By.NAME, "commit")
        create_btn.click()
        time.sleep(2)
        print(f"New project '{NEW_PROJECT_NAME}' created successfully!")

    except Exception as e:
        print("Could not create new project:", e)

    # Re-open Projects page
    try: 
        projects_link = driver.find_element(By.LINK_TEXT, "Projects")
        projects_link.click()
        time.sleep(2)
        print("Projects page opened successfully!")
    except Exception as e:
        print("Could not open projects page:", e)

    # ------------- Admin Section -----------------
    driver.find_element(By.LINK_TEXT, "Administration").click()
    time.sleep(2)

    # Users
    driver.find_element(By.LINK_TEXT, "Users").click()
    time.sleep(2)
    print("Users page opened!")

    # Groups
    driver.find_element(By.LINK_TEXT, "Groups").click()
    time.sleep(2)
    try:
        driver.find_element(By.ID, "group_name").send_keys(NEW_GROUP_NAME)
        driver.find_element(By.NAME, "commit").click()
        time.sleep(2)
        print(f"Group '{NEW_GROUP_NAME}' created successfully!")
    except Exception as e:
        print("Could not create new group:", e)

    # Roles and Permissions
    driver.find_element(By.LINK_TEXT, "Roles and permissions").click()
    time.sleep(2)
    try:
        driver.find_element(By.LINK_TEXT, "Permissions report").click()
        time.sleep(2)
        print("Permissions report opened!")
    except Exception as e:
        print("Could not open Permissions report:", e)

    # Workflow
    driver.find_element(By.LINK_TEXT, "Workflow").click()
    time.sleep(2)
    print("Workflow page opened!")

    # Custom fields
    driver.find_element(By.LINK_TEXT, "Custom fields").click()
    time.sleep(2)
    print("Custom fields page opened!")

    # Enumerations
    driver.find_element(By.LINK_TEXT, "Enumerations").click()
    time.sleep(2)
    try:
        driver.find_element(By.LINK_TEXT, "New value").click()
        time.sleep(2)
        driver.find_element(By.ID, "enumeration_name").send_keys(NEW_ENUM_NAME)
        driver.find_element(By.NAME, "commit").click()
        time.sleep(2)
        print(f"Enumeration '{NEW_ENUM_NAME}' created successfully!")
    except Exception as e:
        print("Could not create new enumeration:", e)

    # Settings
    driver.find_element(By.LINK_TEXT, "Settings").click()
    time.sleep(2)
    print("Settings page opened!")

    # Information
    driver.find_element(By.LINK_TEXT, "Information").click()
    time.sleep(2)
    print("Information page opened!")

    # Navigate to "My page" before closing
    driver.find_element(By.LINK_TEXT, "My page").click()
    time.sleep(2)
    print("My page opened successfully!")

finally:
    # Close the browser
    driver.quit()
    print("Browser closed.")
