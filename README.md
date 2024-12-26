# OpenChargeMap API Testing

This repository contains Python code snippets for testing the OpenChargeMap web application and its API using Selenium and Requests libraries.

## Requirements

* Python 3
* Selenium library (`pip install selenium`)
* Requests library (`pip install requests`)

## Web Automation with Selenium

The first code snippet demonstrates how to automate web browsing interactions with OpenChargeMap using Selenium. It performs the following actions:

1. **Login Test:**
    - Attempts to log in using provided credentials (replace `user_email` and `user_pass` with your actual credentials).
    - Validates the login attempt by checking for error messages.
2. **Browse Test:**
    - Navigates to the "Points of Interest" (POI) page.
    - Selects specific filters for the POI search (e.g., Turkey, Level 2 chargers, Type 2 connection).
    - Clicks the "Search" button.
3. **Nearest POIs Test:**
    - Navigates to the "Points of Interest" page.
    - Clicks the "Search Near Me" button to find nearby charging stations.
    - Clicks the "Search" button.
4. **Map Test:**
    - Navigates to the map view of charging stations.
    - Zooms in and out of the map.
    - Verifies the presence of map markers.

## API Testing with Requests

The second code snippet showcases how to interact with the OpenChargeMap API using the Requests library. It defines a set of test cases covering various API endpoints and functionalities:

1. **Valid GET Requests:**
    - Tests successful retrieval of data from `/poi` and `/referencedata` endpoints with a valid API key.
2. **Invalid GET Request:**
    - Simulates an invalid GET request to `/poi/{countryid}` (assuming this endpoint does not exist).
3. **Login with POST Request:**
    - Sends a POST request to `/profile/authenticate` with valid user credentials to obtain an access token.
    - Stores the access token in a variable for subsequent API requests requiring authentication.
4. **Invalid Login:**
    - Sends a POST request to `/profile/authenticate` with incorrect credentials to test the error handling.
5. **Create Comment:**
    - Sends a POST request to `/comment` to create a new comment on a charging station (requires a valid access token).
6. **Upload Media:**
    - Sends a POST request to `/mediaitem` to upload an image for a charging station (requires a valid access token).

## Running the Tests

1. Replace the placeholder values for `user_email`, `user_pass`, and `API_KEY` with your actual OpenChargeMap credentials.
2. Save the code snippets as Python files (e.g., `openchargemap_test.py` and `openchargemap_api_test.py`).
3. Run the scripts from your terminal using `python openchargemap_test.py` and `python openchargemap_api_test.py`.

**Note:**

* The provided code snippets are for demonstration purposes only and might require adjustments based on potential changes in the OpenChargeMap website or API.
