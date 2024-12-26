import requests

BASE_URL = "https://api.openchargemap.io/v3"

#please enter your API key to test the API!
API_KEY = ""
BEARER_TOKEN = "123"
country_id = "172"

# Please enter your email and password to test the login functionality!
user_email = ""
user_pass = ""


test_cases = [
    {"description": "Valid GET request to /poi", "method": "GET", "endpoint": "/poi", "params": {"key": API_KEY}, "expected_status": 200},
    {"description": "Valid GET request to /poi/{countryid}", "method": "GET", "endpoint": "/poi", "params": {"key": API_KEY}, "expected_status": 404},
    {"description": "Valid GET request to /referencedata", "method": "GET", "endpoint": "/referencedata", "params": {"key": API_KEY}, "expected_status": 200},
    {"description": "Valid POST request to /profile/authenticate", "method": "POST", "endpoint": "/profile/authenticate", "params": {"key": API_KEY}, "data": {"emailaddress": user_email, "password": user_pass}, "expected_status": 200},
    {"description": "Invalid POST request to /profile/authenticate", "method": "POST", "endpoint": "/profile/authenticate", "params": {"key": API_KEY}, "data": {"emailaddress": "example@example.com", "password": "example"}, "expected_status": 401},
    {"description": "Valid POST request to /comment", "method": "POST", "endpoint": "/comment", "params": {"key": API_KEY}, "data": {
        "chargePointID": 0,
        "commentTypeID": 0,
        "userName": "marifkuzgun",
        "comment": "This place is great!",
        "rating": 3,
        "relatedURL": "https://openchargemap.org/site/poi/details/31450",
        "checkinStatusTypeID": 0
    }, "expected_status": 200},
    {"description": "Valid POST request to /mediaitem", "method": "POST", "endpoint": "/mediaitem", "params": {"key": API_KEY}, "data": {
        "chargePointID": 1234,
        "comment": "An example comment",
        "imageDataBase64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=="
    }, "expected_status": 200},
]


def send_request(method, endpoint, params=None, data=None):
    global BEARER_TOKEN
    headers = {"Accept": "application/json", "X-API-Key": API_KEY}
    if endpoint == "/comment":
        headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
    elif endpoint == "/mediaitem":
        headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
    url = f"{BASE_URL}{endpoint}"
    if method == "GET":
        response = requests.get(url, headers=headers, params=params)
    elif method == "POST":
        headers["Content-Type"] = "application/json"
        response = requests.post(url, headers=headers, json=data, params=params)
    if endpoint == "/profile/authenticate":
        try:
            BEARER_TOKEN = response.json()["Data"]["access_token"]
        except:
            pass
    return response

def validate_response(response, expected_status):
    if response.status_code != expected_status:
        return (f"Test failed! Expected {expected_status}, got {response.status_code}")
    else:
        return "Test passed!"

for case in test_cases:
    print(f"Running test: {case['description']}")
    response = send_request(case["method"], case["endpoint"], case.get("params"), case.get("data"))
    
    print(validate_response(response, case["expected_status"]))
    