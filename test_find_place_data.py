from acs_data import *
from credentials import *
from pandas import *

#from openpyxl import load_workbook
print("Getting started!")
#Path to test workbox
print("Loading in file")
#fname = 'C:\scratch\Recession Drops - FINAL TARGET LIST.xlsx'
fname = 'C:\scratch\output_age_by_sex2.xlsx'
tablelist = ['B15003_001E', #Educational Attainment
             'B15003_002E',
             'B15003_003E',
             'B15003_004E',
             'B15003_005E',
             'B15003_006E',
             'B15003_007E',
             'B15003_008E',
             'B15003_009E',
             'B15003_010E',
             'B15003_011E',
             'B15003_012E',
             'B15003_013E',
             'B15003_014E',
             'B15003_015E',
             'B15003_016E',
             'B15003_017E',
             'B15003_018E',
             'B15003_019E',
             'B15003_020E',
             'B15003_021E',
             'B15003_022E',
             'B15003_023E',
             'B15003_024E',
             'B15003_025E',
             'B19001_001E', #Household Income
             'B19001_002E',
             'B19001_003E',
             'B19001_004E',
             'B19001_005E',
             'B19001_006E',
             'B19001_007E',
             'B19001_008E',
             'B19001_009E',
             'B19001_010E',
             'B19001_011E',
             'B19001_012E',
             'B19001_013E',
             'B19001_014E',
             'B19001_015E',
             'B19001_016E',
             'B19001_017E',
             'B25003_001E', #Tenure
             'B25003_002E',
             'B25003_003E',
             'B02001_001E', #Race
             'B02001_002E',
             'B02001_003E',
             'B02001_004E',
             'B02001_005E',
             'B02001_006E',
             'B02001_007E',
             'B02001_008E',
             'B02001_009E',
             'B02001_010E',
             'B03002_001E', #Ethnicity / Hispanic
             'B03002_002E',
             'B03002_003E',
             'B03002_004E',
             'B03002_005E',
             'B03002_006E',
             'B03002_007E',
             'B03002_008E',
             'B03002_009E',
             'B03002_010E',
             'B03002_011E',
             'B03002_012E',
             'B03002_013E',
             'B03002_014E',
             'B03002_015E',
             'B03002_016E',
             'B03002_017E',
             'B03002_018E',
             'B03002_019E',
             'B03002_020E',
             'B03002_021E',
             'B12001_001E', # Marital Status
             'B12001_002E',
             'B12001_003E',
             'B12001_004E',
             'B12001_005E',
             'B12001_006E',
             'B12001_007E',
             'B12001_008E',
             'B12001_009E',
             'B12001_010E',
             'B12001_011E',
             'B12001_012E',
             'B12001_013E',
             'B12001_014E',
             'B12001_015E',
             'B12001_016E',
             'B12001_017E',
             'B12001_018E',
             'B12001_019E']
"""
tablelist = ['B01001_001E', #Age by Sex
                'B01001_002E',
               'B01001_003E',
                'B01001_004E',
                'B01001_005E',
                'B01001_006E',
                'B01001_007E',
                'B01001_008E',
                'B01001_009E',
                'B01001_010E',
                'B01001_011E',
                'B01001_012E',
                'B01001_013E',
                'B01001_014E',
                'B01001_015E',
                'B01001_016E',
                'B01001_017E',
                'B01001_018E',
                'B01001_019E',
                'B01001_020E',
                'B01001_021E',
                'B01001_022E',
                'B01001_023E',
                'B01001_024E',
                'B01001_025E',
                'B01001_026E',
                'B01001_027E',
                'B01001_028E',
                'B01001_029E',
                'B01001_030E',
                'B01001_031E',
                'B01001_032E',
                'B01001_033E',
                'B01001_034E',
                'B01001_035E',
                'B01001_036E',
                'B01001_037E',
                'B01001_038E',
                'B01001_039E',
                'B01001_040E',
                'B01001_041E',
                'B01001_042E',
                'B01001_043E',
                'B01001_044E',
                'B01001_045E',
                'B01001_046E',
                'B01001_047E',
                'B01001_048E',
                'B01001_049E',
            ]
"""

#wb = load_workbook(filename=fname)
#ws = wb['Targets']

#df = pandas.read_excel(fname, sheetname='Targets', header=0)
df = pandas.read_excel(fname, sheetname='Sheet1', header=0)
#fix leading zeros
fips = df['FIPS Code'].apply(str).str.pad(7, 'left', '0')
df['FIPS Code'] = fips
#dataset = df[['org_cst_key', 'FIPS Code', 'State']].values

#statefp='02'
#placefp = '38420'
#tablenumber = 'B01001_001E'



def df_get_acs_place_data(df, state_index, place_index, tablenumber, apikey, verbose):
    addcolumn = []
    nrows = len(df.index)
    i = 0
    for index, row in df.iterrows():
        if verbose:
            print "Processing place %s of %s" %(str(i), str(nrows))
        try:
            temp_placefp = str(row[place_index])
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

for table in tablelist:
    print "Working on %s" % table
    output = df_get_acs_place_data(df, 'State', 'FIPS Code', table, apikey, False)
    df = output

print "FINISHED PROCESS DATA NOW CREATING EXPORT"

writer = pandas.ExcelWriter('C:\scratch\membership_target_list_output.xlsx')
df.to_excel(writer, 'Sheet1')
writer.save()

#test = df_get_acs_place_data(df, 'State', 'FIPS Code', 'B06011_001E', apikey, True)

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
