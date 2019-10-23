import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("GSheetsAPI-73b82ffff956.json", scope)

client = gspread.authorize(creds)
# Open the spreadhseet
sheet = client.open("GSheetsAPI").sheet1
# Get a list of all records
data = sheet.get_all_records()
# Get a specific row
row = sheet.row_values(1)
pprint(row)
# Get a specific column
col = sheet.col_values(3)
pprint(col)
# Get the value of a specific cell
cell = sheet.cell(1,2).value
pprint(cell)
# Get all
pprint(data)
# Insert data
insertRow = ["23-10-2019", "16h30", "13.55"]
# Insert the list as a row at index 2
sheet.add_rows(insertRow)
# Update one cell
#sheet.update_cell(2,1, "23/10/2019")
#sheet.update_cell(2,2, "17h55")
#sheet.update_cell(2,3, "14.05")
sheet.update_cell(3,1, "23/10/2019")
sheet.update_cell(3,2, "17h55")
sheet.update_cell(3,3, "14.05")
