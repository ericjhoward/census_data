from acs_data import *
from credentials import *
from pandas import *

#from openpyxl import load_workbook
print("Getting started!")
#Path to test workbox
print("Loading in file")
fname = 'C:\scratch\Recession Drops - FINAL TARGET LIST.xlsx'
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
#wb = load_workbook(filename=fname)
#ws = wb['Targets']

df = pandas.read_excel(fname, sheetname='Targets', header=0)
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
    output = df_get_acs_place_data(df, 'State', 'FIPS Code', table, apikey, True)
    df = output

print "FINISHED PROCESS DATA NOW CREATING EXPORT"

writer = pandas.ExcelWriter('C:\scratch\output_age_by_sex2.xlsx')
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
