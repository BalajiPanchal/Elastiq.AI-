import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

driver = webdriver.Chrome()
driver.maximize_window()
def test_search_new_york():
   
    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
    print("Enterd URL Playground table search")
    time.sleep(2) 
    
    search_box = driver.find_element(By.XPATH,"//input[@type='search']")
    print("the search box to search for New York")
    time.sleep(2)
    search_box.clear() 
    search_box.send_keys("New York")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    rows = driver.find_elements(By.XPATH, "//table[@id='table']/tbody/tr")
    assert len(rows) == 5, f"Expected 5 rows, but found {len(rows)}" 
    total_entries = driver.find_element(By.XPATH, "//div[@id='table_info']").text
    assert "24" in total_entries, f"Expected total entries to be 24, but got {total_entries}"
    
    print("Test passed: Search results are correct!")

def teardown_module(module):
    driver.quit()

if __name__ == "__main__":
    pytest.main()
