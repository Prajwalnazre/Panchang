'''
Functions :
>> info_extract(maasa, thithi) 
- Extract the thithi information from HTML content and return the panchang object
- Function used in main.py

This file is temporary - will stay until the native logic is completed
'''

from panchangClass import PanchangObject

# Extract the thithi information from HTML content and return the panchang object
def info_extract(maasa, thithi) :
    comma_index = maasa.index(",")
    maasa_string = maasa[comma_index+2:]
    day_of_month_string = maasa[:comma_index]
    pakshas = ['krishna', 'shukla']
    thithis = [
        'amavasya',
        'pratipada',
        'dwitiya',
        'tritiya',
        'chaturthi',
        'panchami',
        'shashthi',
        'saptami',
        'ashtami',
        'navami',
        'dashami',
        'ekadashi',
        'dwadashi',
        'trayodashi',
        'chaturdashi',
        'purnima'
    ]

    for p in pakshas :
        if p in str(thithi) :
            paksha_string = p

    for t in thithis :
        if t in str(thithi) :
            thithi_string = t

    panchang_var = PanchangObject(thithi_string.upper(), maasa_string.upper(), day_of_month_string.upper(), paksha_string.upper())

    return panchang_var