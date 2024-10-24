from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Command():
    url = "https://www.lursoft.lv"
    
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 3)
    
    def handle_cookie_consent(self):
        try:
            cookie_consent_div = self.wait.until(EC.visibility_of_element_located((By.ID, 'siteCookieApproval')))
            accept_button = cookie_consent_div.find_element(By.CSS_SELECTOR, '.cookie-accept-all.button.btn.btn-secondary')
            accept_button.click()
        except TimeoutException:
            pass

    def handle_searching(self, registration_number):
        try:
            input_field = self.wait.until(EC.visibility_of_element_located((By.ID, 'q')))
            input_field.clear()
            input_field.send_keys(registration_number)
            self.driver.find_element(By.XPATH, "//button[.//i and .//span[text()='Meklēt']]").click()

        except Exception as e:
            pass
        
    def click_company_data_link(self, registration_number):
        try:
            print("1")
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//a[text()='{registration_number}']"))
            )
            print("2")
            element.click()
            print('3')
            return True

        except Exception as e:
            print('4')
            return False

    def extract_nace_codes(self):
        activity_codes = []
        try:
            activities_cell = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//td[@data-label='Darbības veidi:']"))
            )
            
            ul_element = activities_cell.find_element(By.XPATH, ".//ul")
            list_items = ul_element.find_elements(By.TAG_NAME, 'li')
            
            for li in list_items:
                anchor_tags = li.find_elements(By.TAG_NAME, 'a')
                activity_codes.extend([anchor.text for anchor in anchor_tags])

        except Exception as e:
            pass

        finally:
            return activity_codes

    def scrape_website(self, registration_numbers):
        all_data = {}
        try:
            self.driver.get(self.url)
            self.handle_cookie_consent()

            count = 1
            for registration_number in registration_numbers:
                print(f"{count} : Scraping data for company with registration number {registration_number}")
                count += 1

                self.handle_searching(registration_number)
                print("Clicking...") 
                if self.click_company_data_link(registration_number):
                    print("Extracting...")
                    nace_codes = self.extract_nace_codes()
                    all_data[str(registration_number)] = nace_codes
            
            print(all_data)
            return all_data 

        except Exception as e:
            print(str(e))
        finally:
            self.driver.quit()
       

registration_numbers = ["50103744891", "41502039796"]
command = Command()
command.scrape_website(registration_numbers)