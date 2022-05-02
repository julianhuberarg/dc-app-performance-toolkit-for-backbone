import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_issues']:
        issue_key = datasets['custom_issue_key']

    # To run action as specific user uncomment code bellow.
    # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
    # just before test_2_selenium_z_log_out action
    #
    @print_timing("selenium_app_specific_user_login")
    def measure():
        def app_specific_user_login(username='admin', password='admin'):
            login_page = Login(webdriver)
            login_page.delete_all_cookies()
            login_page.go_to()
            login_page.set_credentials(username=username, password=password)
            if login_page.is_first_login():
                login_page.first_login_setup()
            if login_page.is_first_login_second_page():
                login_page.first_login_second_page_setup()
            login_page.wait_for_page_loaded()
        app_specific_user_login(username='admin', password='admin')
    measure()


    @print_timing("Open_Settings_UI_for_Backbone")
    def measure_1():
        @print_timing("Backbone_Global_Settings:Open_Settings_UI_for_Backbone")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/backbone-issue-sync/ui/?settings=true")
            #page.wait_until_visible((By.ID, "admin-nav-heading"))  # Wait for upper panel opening
            page.wait_until_visible((By.CLASS_NAME, "BackboneLogoComponent_logoDesc__28AIo"))  # Wait for Backbone Open Settings page
        sub_measure()
    measure_1()


    @print_timing("Open_Administration_UI_for_Backbone")
    def measure_2():
        @print_timing("Backbone_administration:Open_Administration_UI_for_Backbone")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/backbone-issue-sync/ui/")
            #page.wait_until_visible((By.ID, "admin-nav-heading"))  # Wait for upper panel opening
            page.wait_until_visible((By.CLASS_NAME, "App_PageWrapper__1tTt7"))  # Wait for Backbone Open Administration page
        sub_measure()
    measure_2()


    @print_timing("Open_get_started_page")
    def measure_3():
        @print_timing("BackboneGetStarted:Open_get_started_page")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/BackboneGetStarted.jspa")
            #page.wait_until_visible((By.ID, "admin-nav-heading"))  # Wait for upper panel opening
            page.wait_until_visible((By.CLASS_NAME, "aui-page-panel-content"))  # Wait for Backbone Open Get_Started page
        sub_measure()
    measure_3()