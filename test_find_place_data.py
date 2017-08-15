from acs_data import *
from credentials import *
from pandas import *

from openpyxl import load_workbook
print("Getting started!")
#Path to test workbox
print("Loading in file")
fname = 'C:\scratch\Recession Drops - FINAL TARGET LIST.xlsx'
tablelist = ['','','']
wb = load_workbook(filename=fname)
ws = wb['Targets']

df = pandas.read_excel(fname, sheetname='Targets', header=0)
dataset = df[['org_cst_key', 'FIPS Code', 'State']].values

for row in dataset:
    cstkey = row[0]
    try:
        temp_placefp = str(int(row[1]))
        placefp = temp_placefp[2:]
    except:
        placefp = ''
    state = row[2]
    statefp = get_state_fips(state)
    print("cstkey:%s, statefp:%s, placefp:%s" %(cstkey, statefp, placefp))
get_acs_place_data('53', '79590', apikey, 'B06011_001')

statefp:53, placefp:79590

for row in ws.rows:
    temp_placefip = str(row[1].value)
    placefip = temp_placefip[2:]
    state = row[8].value
    statefp = get_state_fips(state)
    print("State:%s, Place:%s" %(statefp, placefip))
