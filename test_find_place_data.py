from acs_data import *
from credentials import *
from pandas import *

#from openpyxl import load_workbook
print("Getting started!")
#Path to test workbox
print("Loading in file")
fname = 'C:\scratch\Recession Drops - FINAL TARGET LIST.xlsx'
tablelist = ['','','']
#wb = load_workbook(filename=fname)
#ws = wb['Targets']

df = pandas.read_excel(fname, sheetname='Targets', header=0)
#dataset = df[['org_cst_key', 'FIPS Code', 'State']].values

def df_get_acs_place_data(df, state_index, place_index, tablenumber, apikey, verbose):
    addcolumn = []
    nrows = len(df.index)
    i = 0
    for row in df:
        if verbose:
            print "Processing place %s of %s" %(str(i), str(nrows))
        try:
            temp_placefp = str(int(row[place_index]))
            placefp = temp_placefp[2:]
        except:
            placefp=''
        state = row[state_index]
        statefp = get_state_fips(state)
        try:
            output = get_acs_place_data(statefp, placefp, apikey, tablenumber)
            result = int(output[1][1])
        except:
            result = -99
        addcolumn.append(result)
        i += 1
    df[tablenumber] = pandas.Series(addcolumn, dtype=int)
    return(df)

test = df_get_acs_place_data(df, 'State', 'FIPS Code', 'B06011_001E', apikey, True)

'''
for row in dataset:
    cstkey = row[0]
    try:
        temp_placefp = str(int(row[1]))
        placefp = temp_placefp[2:]
    except:
        placefp = ''
    state = row[2]
    statefp = get_state_fips(state)
    try:
        output = get_acs_place_data(statefp, placefp, apikey, 'B06011_001E')
        result = output[1][1]
    except:
        result = None
    print("statefp:%s, placefp:%s, ouput:%s" %(statefp, placefp, result))
    '''
