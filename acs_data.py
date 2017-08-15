"""acs_data.py
A series of functions in order to request ACS data from the U.S. Census
Bureau's API.
Eric J. Howard
howard@nlc.org
Aug. 15, 2017
"""

import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_state_fips(state):
    """Function to look up the state FIPS code based on the USPS 2 character
    abberviations

    Args:
        state (str): Two-character abberviation for a given state
    Returns:
        str: The two-digit FIPS for the given state
    """
    lookup_state_fips = {}
    lookup_state_fips['AK'] = '02'
    lookup_state_fips['AL'] = '01'
    lookup_state_fips['AR'] = '05'
    lookup_state_fips['AS'] = '60' #American Samoa
    lookup_state_fips['AZ'] = '04'
    lookup_state_fips['CA'] = '06'
    lookup_state_fips['CO'] = '08'
    lookup_state_fips['CT'] = '09'
    lookup_state_fips['DC'] = '11'
    lookup_state_fips['DE'] = '10'
    lookup_state_fips['FL'] = '12'
    lookup_state_fips['GA'] = '13'
    lookup_state_fips['GU'] = '66' #Guam
    lookup_state_fips['HI'] = '15'
    lookup_state_fips['IA'] = '19'
    lookup_state_fips['ID'] = '16'
    lookup_state_fips['IL'] = '17'
    lookup_state_fips['IN'] = '18'
    lookup_state_fips['KS'] = '20'
    lookup_state_fips['KY'] = '21'
    lookup_state_fips['LA'] = '22'
    lookup_state_fips['MA'] = '25'
    lookup_state_fips['MD'] = '24'
    lookup_state_fips['ME'] = '23'
    lookup_state_fips['MI'] = '26'
    lookup_state_fips['MN'] = '27'
    lookup_state_fips['MO'] = '29'
    lookup_state_fips['MS'] = '28'
    lookup_state_fips['MT'] = '30'
    lookup_state_fips['NC'] = '37'
    lookup_state_fips['ND'] = '38'
    lookup_state_fips['NE'] = '31'
    lookup_state_fips['NH'] = '33'
    lookup_state_fips['NJ'] = '34'
    lookup_state_fips['NM'] = '35'
    lookup_state_fips['NV'] = '32'
    lookup_state_fips['NY'] = '36'
    lookup_state_fips['OH'] = '39'
    lookup_state_fips['OK'] = '40'
    lookup_state_fips['OR'] = '41'
    lookup_state_fips['PA'] = '42'
    lookup_state_fips['PR'] = '72' #Puerto Rico
    lookup_state_fips['RI'] = '44'
    lookup_state_fips['SC'] = '45'
    lookup_state_fips['SD'] = '46'
    lookup_state_fips['TN'] = '47'
    lookup_state_fips['TX'] = '48'
    lookup_state_fips['UT'] = '49'
    lookup_state_fips['VA'] = '51'
    lookup_state_fips['VI'] = '78' #Virgin Islands
    lookup_state_fips['VT'] = '50'
    lookup_state_fips['WA'] = '53'
    lookup_state_fips['WI'] = '55'
    lookup_state_fips['WV'] = '54'
    lookup_state_fips['WY'] = '56'

    #Use the created dictonary to get the result
    try:
        statefp = lookup_state_fips[state]
    except:
        statefp = None
    return(statefp)


def get_acs_place_data(statefp, placefp, apikey, tablenumber):
    """Function to send a get request to the API endpoint for the
    ACS 5-year data that ends in 2015 for a specified place.

    Args:
        statefp (str): The FIPS code for the state in which the place is found
        placefp (str): The FIPS code for the place of interest
        apikey (str): The user's Census API key
        tablenumber (str): The table number of interest
    Returns:
        dict: A dictonary with the results of the API request

    """
    url = "https://api.census.gov/data/2015/acs5?get=NAME,%s&for=place:%s&in=state:%s&key=%s" %(tablenumber, placefp, statefp, apikey)
    r = requests.get(url)
    result = json.loads(r.text)
    return(result)

#def get_acs_msa_data()
#def get_acs_block_group_data()
#def get_acs_tract_data()
#def get_acs_block_data()
