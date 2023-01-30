# LinkedIn Jobs Scraper
A Python script that automates the process of fetching job information from LinkedIn and saving it to an Excel (.xlsx) file.

## Requirements
- Python 3.x
- selenium
- openpyxl

## Usage
1. Clone the repository to your local machine
2. Install the required libraries:

pip install selenium

pip install openpyxl

3. Run the script:

python linkedin_jobs_scraper.py


## Output
The script will produce a file named `linkedin_jobs.xlsx` that contains the following information for each job:
- Title
- Company
- Location

## Description
This project uses the Selenium library to automate the process of opening a web browser, navigating to the LinkedIn Jobs page, and extracting the job information. The extracted information is then saved to an Excel workbook using the openpyxl library.

The script only fetches information from the first page of the LinkedIn Jobs search results, but it can be easily modified to handle pagination if needed. Additionally, the script only captures a limited set of information about each job, but it can be modified to capture more data if desired.

This project is intended to demonstrate the process of scraping information from a website and saving it to a structured format like an Excel spreadsheet. It is not intended for use in production or for commercial purposes.

