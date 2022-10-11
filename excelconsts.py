import sys

# Charge Variables
BRINKS_FSC = 0.125 # Brinks Fuel Surcharge %
GARDA_FSC = 0.05 # Garda Fuel Surcharge %
GARDA_SECURITY = 0.05 # Garda Security Charge

#Colums Locations
COLS_OF_STORE_INFO = 8 # Amount of blocked out columns for store information
CHARGES_STARTING_COL = COLS_OF_STORE_INFO+1 # Analyzed information start column
BRINKS_RATE_COLUMN = 11 # Column where Brinks pricing is located
GARDA_RATE_COLUMN = 11 # Column where Brinks pricing is located
CURRENT_VENDOR_COL = 8
CURRENT_VENDOR_START_COL = 14 # Current Vendor information start column
VENDOR_PRICE_COLUMN = CURRENT_VENDOR_START_COL-1 # Current Vendor prices

# Column widths of new sheet
BIG_COLUMN_WIDTH = 20
LITTLEST_COLUMN_WIDTH = 10
LITTLE_COLUMN_WIDTH = 17
BIGGEST_COLUMN_WIDTH = 25

# Sheets to Use
STORE_INFORMATION_WB = 'store.xlsx'
GARDA_WB = 'garda.xlsx'
BRINKS_WB = 'brinks.xlsx'
RAC_WB = None
SAVE_NAME = 'Compilation.xlsx'

# GUI Defaults
FONT = 'Verdana'
BIG_FONT_SIZE = '14'
BIGGEST_FONT_SIZE = '20'
REGULAR_FONT_SIZE = '10'
INPUT_BAR_SIZE = 17
DONE_MESSAGE_SIZE = 50

# For Zipcodes and Map
ZIPCODE_COLUMN = 5

try:
    store = str(sys.argv[1])
    if type(store) == str and store.endswith('.xlsx'):
        STORE_INFORMATION_WB = store
        print('Store Information Workbook: ' + store)
except:
    pass # Use original value

try:
    garda = str(sys.argv[2])
    if type(garda) == str and garda.endswith('.xlsx'):
        GARDA_WB = garda
        print('Garda Workbook: ' + garda)
except:
    pass # Use original value

try:
    brinks = str(sys.argv[3])
    if type(brinks) == str and brinks.endswith('.xlsx'):
        BRINKS_WB = brinks
        print('Brinks Workbook: ' + brinks)
except:
    pass # Use original value
