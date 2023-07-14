# MCS-WebScrapper

## Approach:

The provided code performs web scraping to extract table data from multiple pages of the target website. It utilizes concurrent execution using "concurrent.futures.ThreadPoolExecutor" to improve performance. The scraped data is stored in a set to ensure uniqueness.

1. "scrape_page" Function: This function is responsible for scraping the data from a single page. It constructs the URL based on the page number, sends an HTTP GET request, and parses the HTML response using BeautifulSoup. The function extracts the desired table data from the HTML and returns it as a set.

2. Error Handling: The code implements error handling using try-except blocks. It catches exceptions related to requests and general exceptions. In case of an error, it prints an error message and returns an empty set.

3. ThreadPoolExecutor: The code creates a "ThreadPoolExecutor" with a maximum number of workers set to the number of pages to scrape. It submits tasks to the executor for each page using the "scrape_page" function.

4. Collecting Results: The code iterates over the futures returned by the executor's "as_completed" method. It retrieves the result of each future and updates the "table_data" set with the extracted data.

5. Printing Table Data: Finally, the code iterates over the "table_data" set and prints the extracted table data along with a serial number.

----------------------------------------------------------------

## Design Decisions:

1. Using a Set: The code uses a set to store the extracted table data. This ensures that only unique data is stored, eliminating duplicates.

2. Multithreading: By utilizing "concurrent.futures.ThreadPoolExecutor", the code achieves concurrent execution of scraping tasks, allowing for improved performance.

----------------------------------------------------------------

## Challenges Faced:

1. Handling Exceptions: One challenge during implementation is handling exceptions that may occur during web requests or data extraction. The code includes error handling to catch and handle these exceptions gracefully.

2. Website Structure: Extracting data from websites requires understanding their structure. If the website structure changes or is complex, it can pose challenges in locating and extracting the desired data accurately.

3. Data Uniqueness: Ensuring uniqueness of the extracted data is crucial to avoid duplications. By using a set, the code ensures that only unique data is stored.

4. Concurrent Execution: Implementing concurrent execution introduces challenges related to synchronization and potential race conditions. The code manages this by using the "as_completed" method to collect results and update the "table_data" set safely.
