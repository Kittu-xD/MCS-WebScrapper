import concurrent.futures
import requests
from bs4 import BeautifulSoup

__author__ = "Kartik Aggarwal"
__version__ = 1.0


def scrape_page(page):
  url = f'https://www.insiderbiz.in/company-list/?page={page}'
  try:
    response = session.get(url)
    response.raise_for_status(
    )  # Raise an exception for 4xx or 5xx status codes
    soup = BeautifulSoup(response.text, 'html.parser')

    table_data = set()  # Use a set to store unique table data

    # Find the table element with class 'table'
    table = soup.find('table', class_='table')

    # Find all <tr> elements within the table
    rows = table.find_all('tr')

    # Iterate over each row and extract the text from the <td> elements
    for row in rows:
      row_data = tuple(
        td.get_text(strip=True)
        for td in row.find_all('td'))  # Convert row_data to a tuple
      if len(row_data) == 4:
        table_data.add(row_data)  # Add the tuple to the set

    return table_data
  except requests.exceptions.RequestException as e:
    print(f"Error occurred while scraping page {page}: {e}")
    return set()
  except Exception as e:
    print(f"An error occurred while scraping page {page}: {e}")
    return set()


# Create a session object
session = requests.Session()

# Number of pages to scrape
num_pages = int(input("Enter Number of pages to scrape: "))

# Create a ThreadPoolExecutor with max_workers set to the number of pages
with concurrent.futures.ThreadPoolExecutor(max_workers=num_pages) as executor:
  # Submit tasks for each page to scrape_page function
  futures = [
    executor.submit(scrape_page, page) for page in range(1, num_pages + 1)
  ]

  # Collect the results as they become available
  table_data = set()  # Use a set to store unique table data
  for future in concurrent.futures.as_completed(futures):
    try:
      result = future.result()
      table_data.update(result)  # Merge the sets from each page
    except Exception as e:
      print(f"An error occurred while processing a future: {e}")

# Print the extracted table data
i = 1
for row_data in table_data:
  print(i, "---", row_data)
  i += 1
