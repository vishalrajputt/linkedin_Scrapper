from selenium import webdriver
from openpyxl import Workbook

# Start a web driver to automate the web browser
driver = webdriver.Firefox()

# Navigate to the LinkedIn Jobs page
driver.get('https://www.linkedin.com/jobs/')

# Locate the elements on the page that contain the job information you want to scrape
job_elements = driver.find_elements_by_xpath("//li[@class='job-listing']")

# Extract the job information you need from each job element
jobs = []
for job_element in job_elements:
    title = job_element.find_element_by_xpath(".//h3").text
    company = job_element.find_element_by_xpath(".//span[@class='job-result-card__company-name']").text
    location = job_element.find_element_by_xpath(".//span[@class='job-result-card__location']").text
    jobs.append((title, company, location))

# Create a new Excel workbook and add the job information to a worksheet
workbook = Workbook()
worksheet = workbook.active
worksheet.append(["Title", "Company", "Location"])
for job in jobs:
    worksheet.append(job)

# Save the workbook to disk
workbook.save("linkedin_jobs.xlsx")

# Close the web driver
driver.quit()
