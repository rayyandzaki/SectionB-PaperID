from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

def login_test(email, password, expected, driver, wait):
    driver.get("https://www.paper.id/webappv1/#/login")

    wait.until(EC.element_to_be_clickable((By.NAME, "email"))).send_keys(email)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-cy='submit']"))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-cy="password"]'))).send_keys(password + Keys.ENTER)

    time.sleep(2)  # wait for redirect or error

    if expected == "success":
        try:
            wait.until(EC.url_contains("/#/invoicer/dashboardv2"))
            print(f"[PASS] Login sukses: {email}")
        except TimeoutException:
            print(f"[FAIL] Tidak redirect dashboard: {email}")
    else:
        try:
            error_element = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "input-warning-message__text"))
            )
            print(f"[PASS] Login gagal sesuai harapan: {email} - {error_element.text}")
        except TimeoutException:
            print(f"[FAIL] Pesan error tidak muncul: {email}")

# Driver setup
driver_path = r"C:\Users\Lenovo\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(driver_path), options=options)
wait = WebDriverWait(driver, 10)

credentials = [
    {"email": "rayyandzaki23@gmail.com", "password": "DipakeRayyan1!", "expected": "success"},
    {"email": "invaliduser@example.com", "password": "WrongPassword123", "expected": "failure"},
]

for cred in credentials:
    try:
        login_test(cred["email"], cred["password"], cred["expected"], driver, wait)
    except Exception as e:
        print(f"[ERROR] Login error {cred['email']}: {e}")
