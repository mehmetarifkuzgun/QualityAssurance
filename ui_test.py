from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select


# Please enter your email and password to test the login functionality
user_email = ""
user_pass = ""

PATH = "chromedriver"
driver = webdriver.Chrome()

driver.get("https://openchargemap.org")

def login_test(email, password):
    try:
    # Wait until the element is present and clickable
        profile_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.nav-link[href*="/site/profile/signin"]'))
        )

        # Click the profile link
        profile_link.click()

        # Wait until the email input field is present
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'EmailAddress'))
        )
        # Input text into the email field
        email_input.send_keys(email)


        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'Password'))
        )
        password_input.send_keys(password)

        time.sleep(2)

        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.btn.btn-primary[type="submit"]'))
        )
        # Click the sign-in button
        sign_in_button.click()

        try:
            error_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'p.alert.alert-danger'))
        )
            print("Login test failed: Invalid email address or password.")
        except:
            print("Login test passed")

        time.sleep(1)

    except:
        print("Login test failed")

def browse_test():
    try:
        # Wait until the element is present and clickable
        poi_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.nav-link[href="/site/poi"]'))
        )
        # Click the link
        poi_link.click()
        print("Navigation to POI page successful")

        # Wait until the "all locations" button is present and clickable
        all_locations_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.dropdown-item[href="/site/poi"]'))
        )
        # Click the "all locations" button
        all_locations_button.click()
        print("Clicked 'all locations' button successfully")

        country_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'countryids'))
        )
        # Select "Turkey" from the dropdown
        select = Select(country_dropdown)
        select.select_by_value("229")
        print("Selected 'Turkey' from the dropdown successfully")

        level_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'levelids'))
        )
        select = Select(level_dropdown)
        select.select_by_value("2")
        print("Selected 'Level 2 : Medium (Over 2kW)' from the dropdown successfully")

        connectiontype_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'connectiontypeids'))
        )
        select = Select(connectiontype_dropdown)
        select.select_by_value("25")
        print("Selected 'Level 2 : Type 2 (Socket Only)' from the dropdown successfully")

        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.btn.btn-primary[type="submit"]'))
        )

        search_button.click()
        print("Clicked 'Search' button successfully")

    except Exception as e:
        print(f"Navigation to POI page or clicking 'all locations' button failed: {e}")

def nearest_pois():
    try:
        # Wait until the element is present and clickable
        poi_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.nav-link[href="/site/poi"]'))
        )
        # Click the link
        poi_link.click()

        # Wait until the "all locations" button is present and clickable
        all_locations_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.dropdown-item[href="/site/poi"]'))
        )
        # Click the "all locations" button
        all_locations_button.click()

        # Wait until the "Search Near Me" button is present and clickable
        search_near_me_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search-nearme'))
        )
        # Click the "Search Near Me" button
        search_near_me_button.click()
        print("Clicked 'Search Near Me' button successfully")
        

        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.btn.btn-primary[type="submit"]'))
        )

        search_button.click()
        print("Clicked 'Search' button successfully")

    except Exception as e:
        print(f"Navigation to POI page or clicking 'Search Near Me' button failed: {e}")

def test_map():
    try:
        # Wait until the element is present and clickable
        poi_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.nav-link[href="/site/poi"]'))
        )
        # Click the link
        poi_link.click()
        print("Navigation to POI page successful")

        # Wait until the "map" button is present and clickable
        map_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.dropdown-item[href="https://map.openchargemap.io"]'))
        )
        # Click the "map" button
        map_button.click()
        print("Clicked 'map' button successfully")

        # Switch to the new window/tab
        driver.switch_to.window(driver.window_handles[-1])

        # Wait until the map is present
        map_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'app-root'))  # Replace with the actual ID or CSS selector of the map element
        )
        print("Map is present")

        time.sleep(2)  # Wait for the map to load

        # Zoom in the map using the zoom in button
        zoom_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.mapboxgl-ctrl-zoom-in'))
        )
        zoom_in_button.click()
        print("Zoomed in the map")

        time.sleep(2)  # Wait for the zoom action to complete

        # Zoom out the map using the zoom out button
        zoom_out_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.mapboxgl-ctrl-zoom-out'))
        )
        zoom_out_button.click()
        print("Zoomed out the map")

        time.sleep(2)  # Wait for the zoom action to complete

        # Verify the presence of map markers
        markers = driver.find_elements(By.CSS_SELECTOR, '.mapboxgl-marker')  # Updated CSS selector for map markers
        if markers:
            print(f"Found {len(markers)} map markers")
        else:
            print("No map markers found")

    except Exception as e:
        print(f"Map test failed: {e}")

# invalid credentials
login_test("example@example.com", "password")   

# valid credentials

login_test(user_email, user_pass)

driver.get("https://openchargemap.org") 

browse_test()

nearest_pois()

time.sleep(3)

test_map()

driver.quit()