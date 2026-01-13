## Overview

This repository contains the **deployment and testing of the Redmine open-source project management tool (https://www.redmine.org/)**. It covers:
- Deployment using **Docker Desktop** on Windows with WSL2
- Functional and UI testing using **Python Selenium**
- Performance/load testing using **JMeter**
- Functional issues reporting and test case documentation
  
## Load/Performance Testing (JMeter)
JMeter test plan: jmeter/redmine_load_test.jmx
Tests multiple concurrent users on:
- Login
- Project creation
- Issue creation
- Enumeration creation
  
### Run JMeter test plan:
- Open Apache JMeter
- Load redmine_load_test.jmx
- Execute test and analyze results

## Functional/UI Testing (Selenium)

Dependencies:
  pip install selenium webdriver-manager

The Selenium script covers:
- Login to Redmine
- Navigate to Projects and create a new project
- Administration sections: Users, Groups, Roles & Permissions, Workflow, Custom Fields, Enumerations, Settings, Information
- Navigate to "My page"

### Run script:
  python selenium/selenium_script.py
  
Test case table and functional issues are documented in docs.docx.

## Observed Functional Issues
Creating project without login	Allows project creation without authentication
Tracker creation	Default status cannot be blank; prevents creating tracker for issues

Full functional issues table is available in "Functional Testing using Selenium/docs.docx".

### Notes

- Redmine is deployed locally using Docker with SQLite database.
- Selenium scripts include proper waits (time.sleep) for simplicity; can be replaced with explicit waits in production.
