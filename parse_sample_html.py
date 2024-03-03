import csv
from bs4 import BeautifulSoup

# Path to your HTML file
file_path = 'sampleSIRPC_Input.html'

# Open and read the HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Define the path for the output CSV file
output_csv_path = 'labor_force_data.csv'

# Find the 'th' element containing 'Labor Force, 2022' and navigate to the parent table
labor_force_header = soup.find(lambda tag: tag.name == "th" and "Labor Force, 2022" in tag.text)
if labor_force_header:
    labor_force_table = labor_force_header.find_parent("table")

    # Open a new CSV file to write the data into
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Write the headers
        headers = [th.text.strip() for th in labor_force_table.find_all('th')]
        csvwriter.writerow(headers)

        # Write the table rows
        for row in labor_force_table.find_all("tr")[1:]:  # Skip the header row
            columns = row.find_all("td")
            data = [column.text.strip() for column in columns]
            csvwriter.writerow(data)
else:
    print("Labor Force data not found")
