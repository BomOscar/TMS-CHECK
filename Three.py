from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# URL of the webpage
url = 'https://tms.tpf.go.tz/'  # Replace with the actual URL

# Set up the Selenium WebDriver with headless option
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode without opening the browser window
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the webpage
    driver.get(url)

    # Find the search input and fill in the search query
    search_input = driver.find_element(By.ID, 'searchable')

    search_input.send_keys('T772EBZ')  # Replace with the new plate number

    # Find and click the search button
    search_button = driver.find_element(By.CLASS_NAME, 'search-form')
    search_button.click()

    # Wait for the results to load (you might need to adjust the time based on your network speed)
    time.sleep(5)  # Adjust the sleep time as needed

    # Find and extract data from the result table
    result_table = driver.find_element(By.ID, 'result-table')
    
    # Extract the table header
    header_row = result_table.find_element(By.TAG_NAME, 'thead')
    header_columns = header_row.find_elements(By.TAG_NAME, 'th')
    header_data = [column.text.strip() for column in header_columns]

    # Extract and append the table data
    rows = result_table.find_elements(By.TAG_NAME, 'tr')
    data = []
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, 'td')
        row_data = [column.text.strip() for column in columns]
        data.append(row_data)

    # Create a Pandas DataFrame
    df = pd.DataFrame(data, columns=header_data)

    # Export DataFrame to CSV
    df.to_csv('outputFile.csv', index=False)

finally:
    # Close the browser window
    driver.quit()
