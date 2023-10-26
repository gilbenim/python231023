import requests
from bs4 import BeautifulSoup
import openpyxl

# Create a new Excel workbook and add a worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = "NaverBlogResults"

# Function to scrape and extract information from a single page and add it to the Excel sheet
def scrape_naver_blog_page(url, worksheet):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        blog_entries = soup.find_all("li", class_="bx _svp_item")

        for entry in blog_entries:
            blog_name = entry.find("a", class_="sub_txt").text
            blog_address = entry.find("a", class_="sub_txt")["href"]
            post_title = entry.find("a", class_="api_txt_lines total_tit").text
            post_date = entry.find("span", class_="sub_time").text

            # Add the extracted information to the Excel sheet
            worksheet.append([blog_name, blog_address, post_title, post_date])

    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)

# Loop through pages 1 to 100
for page in range(1, 101):
    search_query = "%EB%A7%A5%EB%B6%81"
    page_url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_query}&start={((page - 1) * 10) + 1}"

    # Call the function to scrape the page and add to the Excel sheet
    scrape_naver_blog_page(page_url, worksheet)

# Save the workbook to the specified file
workbook.save(r"c:\work\result.xlsx")
