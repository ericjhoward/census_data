#fix_column_headings.py
from pandas import *

fname = 'C:\scratch\membership_target_list_output.xlsx'
df = pandas.read_excel(fname, sheetname='Sheet1', header=0)

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
                'B15003_001E', #Educational Attainment
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
                'B12001_019E'
            ]

nameslist = ['Sex by Age: Total', #Age by Sex
                'Sex by Age: Male',
                'Sex by Age: Male Under 5 Years',
                'Sex by Age: Male 5 to 9 Years',
                'Sex by Age: Male 10 to 14 Years',
                'Sex by Age: Male 15 to 17 Years',
                'Sex by Age: Male 18 to 19 Years',
                'Sex by Age: Male 20 Years',
                'Sex by Age: Male 21 Years',
                'Sex by Age: Male 22 to 24 Years',
                'Sex by Age: Male 25 to 29 Years',
                'Sex by Age: Male 30 to 34 Years',
                'Sex by Age: Male 35 to 39 Years',
                'Sex by Age: Male 40 to 44 Years',
                'Sex by Age: Male 45 to 49 Years',
                'Sex by Age: Male 50 to 54 Years',
                'Sex by Age: Male 55 to 59 Years',
                'Sex by Age: Male 60 to 61 Years',
                'Sex by Age: Male 52 to 64 Years',
                'Sex by Age: Male 65 to 66 Years',
                'Sex by Age: Male 67 to 69 Years',
                'Sex by Age: Male 70 to 74 Years',
                'Sex by Age: Male 75 to 79 Years',
                'Sex by Age: Male 80 to 84 Years',
                'Sex by Age: Male 85 Years and Over',
                'Sex by Age: Female',
                'Sex by Age: Female Under 5 Years',
                'Sex by Age: Female 5 to 9 Years',
                'Sex by Age: Female 10 to 14 Years',
                'Sex by Age: Female 15 to 17 Years',
                'Sex by Age: Female 18 to 19 Years',
                'Sex by Age: Female 20 Years',
                'Sex by Age: Female 21 Years',
                'Sex by Age: Female 22 to 24 Years',
                'Sex by Age: Female 25 to 29 Years',
                'Sex by Age: Female 30 to 34 Years',
                'Sex by Age: Female 35 to 39 Years',
                'Sex by Age: Female 40 to 44 Years',
                'Sex by Age: Female 45 to 49 Years',
                'Sex by Age: Female 50 to 54 Years',
                'Sex by Age: Female 55 to 59 Years',
                'Sex by Age: Female 60 to 61 Years',
                'Sex by Age: Female 52 to 64 Years',
                'Sex by Age: Female 65 to 66 Years',
                'Sex by Age: Female 67 to 69 Years',
                'Sex by Age: Female 70 to 74 Years',
                'Sex by Age: Female 75 to 79 Years',
                'Sex by Age: Female 80 to 84 Years',
                'Sex by Age: Female 85 Years and Over',
                'Edu. Attainment: Total', #Educational Attainment
                'Edu. Attainment: No Schooling',
                'Edu. Attainment: Nursery School',
                'Edu. Attainment: Kindergarten',
                'Edu. Attainment: 1st Grade',
                'Edu. Attainment: 2nd Grade',
                'Edu. Attainment: 3rd Grade',
                'Edu. Attainment: 4th Grade',
                'Edu. Attainment: 5th Grade',
                'Edu. Attainment: 6th Grade',
                'Edu. Attainment: 7th Grade',
                'Edu. Attainment: 8th Grade',
                'Edu. Attainment: 9th Grade',
                'Edu. Attainment: 10th Grade',
                'Edu. Attainment: 11th Grade',
                'Edu. Attainment: 12th Grade No Diploma',
                'Edu. Attainment: Regular High School Diploma',
                'Edu. Attainment: GED or Alternative Credential',
                'Edu. Attainment: Some College Less Than 1 Year',
                'Edu. Attainment: Some College More Than 1 Year No Degree',
                'Edu. Attainment: Associates Degree',
                'Edu. Attainment: Bachelors Degree',
                'Edu. Attainment: Masters Degree',
                'Edu. Attainment: Professional School Degree',
                'Edu. Attainment: Doctorate Degree',
                'Household Income: Total', #Household Income
                'Household Income: Less Than $10,000',
                'Household Income: $10,000 to $14,999',
                'Household Income: $15,000 to $19,999',
                'Household Income: $20,000 to $24,999',
                'Household Income: $25,000 to $29,999',
                'Household Income: $30,000 to $34,999',
                'Household Income: $35,000 to $39,999',
                'Household Income: $40,000 to $44,999',
                'Household Income: $45,000 to $49,999',
                'Household Income: $50,000 to $59,999',
                'Household Income: $60,000 to $74,999',
                'Household Income: $75,000 to $99,999',
                'Household Income: $100,000 to $124,999',
                'Household Income: $125,000 to $149,999',
                'Household Income: $150,000 to $199,999',
                'Household Income: $200,000 or More',
                'Housing Tenure: Total', #Tenure
                'Housing Tenure: Owner Occupied',
                'Housing Tenure: Renter Occupied',
                'Race: Total', #Race
                'Race: White Alone',
                'Race: Black or African American Alone',
                'Race: American Indian and Alaska Native Alone',
                'Race: Asian Alone',
                'Race: Native Hawaiian and Other Pacific Islander Alone',
                'Race: Some Other Race Alone',
                'Race: Two or More Races',
                'Race: Two or More Races Including Some Other Race',
                'Race: Two Races Excluding Some Other Race, and Three or More Races',
                'Hispanic or Latino by Race: Total', #Ethnicity / Hispanic
                'Hispanic or Latino by Race: Not Hispanic or Latino',
                'Hispanic or Latino by Race: Not Hispanic or Latino, White Alone',
                'Hispanic or Latino by Race: Not Hispanic or Latino, Black or African American Alone',
                'Hispanic or Latino by Race: Not Hispanic or Latino, American Indian and Alaska Native Alone',
                'Hispanic or Latino by Race: Not Hispanic or Latino, Asian Alone',
                'Hispanic or Latino by Race: Not Hispanic or Latino, Native Hawaiian and Other Pacific Islander Alone',
                'Hispanic or Latino by Race: Not Hispanic or Latino, Some Other Race Alone',
                'Hispanic or Latino by Race: Not Hispanic or Latino, Two or More Races',
                'Hispanic or Latino by Race: Not Hispanic or Latino, Two or More Races, Two Races Including Some Other Race',
                'Hispanic or Latino by Race: Not Hispanic or Latino, Two or More Races, Two Races Excluding Some Other Race, and Three or More Races',
                'Hispanic or Latino by Race: Hispanic or Latino',
                'Hispanic or Latino by Race: Hispanic or Latino, White Alone',
                'Hispanic or Latino by Race: Hispanic or Latino, Black or African American Alone',
                'Hispanic or Latino by Race: Hispanic or Latino, American Indian and Alaska Native Alone',
                'Hispanic or Latino by Race: Hispanic or Latino, Asian Alone',
                'Hispanic or Latino by Race: Hispanic or Latino, Native Hawaiian and Other Pacific Islander Alone',
                'Hispanic or Latino by Race: Hispanic or Latino, Some Other Race Alone',
                'Hispanic or Latino by Race: Hispanic or Latino, Two or More Races',
                'Hispanic or Latino by Race: Hispanic or Latino, Two or More Races, Two Races Including Some Other Race',
                'Hispanic or Latino by Race: Hispanic or Latino, Two or More Races, Two Races Excluding Some Other Race, and Three or More Races',
                'Sex by Marital Status: Total', # Marital Status
                'Sex by Marital Status: Male',
                'Sex by Marital Status: Male, Never Married',
                'Sex by Marital Status: Male, Now Married',
                'Sex by Marital Status: Male, Now Married, Spouse Present',
                'Sex by Marital Status: Male, Now Married, Spouse Absent',
                'Sex by Marital Status: Male, Now Married, Spouse Absent, Separated',
                'Sex by Marital Status: Male, Now Married, Spouse Absent, Other',
                'Sex by Marital Status: Male, Widowed',
                'Sex by Marital Status: Male, Divorced',
                'Sex by Marital Status: Female',
                'Sex by Marital Status: Female, Never Married',
                'Sex by Marital Status: Female, Now Married',
                'Sex by Marital Status: Female, Now Married, Spouse Present',
                'Sex by Marital Status: Female, Now Married, Spouse Absent',
                'Sex by Marital Status: Female, Now Married, Spouse Absent, Separated',
                'Sex by Marital Status: Female, Now Married, Spouse Absent, Other',
                'Sex by Marital Status: Female, Widowed',
                'Sex by Marital Status: Female, Divorced',
            ]


df.rename(columns=dict(zip(tablelist, nameslist)), inplace=True)
writer = pandas.ExcelWriter('C:\scratch\membership_target_list_output_renamed_columns.xlsx')
df.to_excel(writer, 'Sheet1')
writer.save()


#test = dict(zip(tablelist, nameslist))
