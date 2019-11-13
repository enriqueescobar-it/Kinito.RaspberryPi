#import spidev
import glob
import time
import sys
import datetime

import time
#import gdata.spreadsheet.service
import os
import subprocess

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
#
# Scope
scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
# Credentials
creds = ServiceAccountCredentials.from_json_keyfile_name("GSheetsAPI.json", scope)
# Authorization
client = gspread.authorize(creds)
# Open the spreadhseet
sheet = client.open("GSheetsAPI").sheet1
## Gets Now as today
def getNowDDMMYYYY():
	return time.strftime('%d/%m/%Y')
## Gets Now as HHMM
def getNowHHMM():
	return time.strftime('%H:%M')
# Get all
print("+\tall records")
data = sheet.get_all_records()
pprint(data)
# Get a specific row
row = sheet.row_values(1)
print("+\trow[1]")
pprint(row)
# Get a specific column
print("+\tcol[3]")
col = sheet.col_values(3)
pprint(col)
# Get the value of a specific cell
cell = sheet.cell(1,2).value
print("+\tcel[1,2]")
pprint(cell)
# Get all
print("+\tall records")
data = sheet.get_all_records()
pprint(data)
# Insert data
insertRow = [getNowDDMMYYYY(), getNowHHMM(), 12.34]
# Insert the list as a row at index 2
#sheet.add_rows(2)
sheet.append_row(insertRow)
# Get the number of rows in the sheet
numRows = sheet.row_count
print("+\t_row count")
pprint(numRows)
# Update one cell
sheet.update_cell(3,1, getNowDDMMYYYY())
sheet.update_cell(3,2, getNowHHMM())
sheet.update_cell(3,3, 43.21)
