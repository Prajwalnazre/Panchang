from panchangClass import PanchangObject

def info_extract(maasa, thithi) :
    comma_index = maasa.index(",")
    maasa_string = maasa[comma_index+2:]
    day_of_month_string = maasa[:comma_index]
    # print(maasa_string)
    # print(day_of_month_string)
    
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
        # print(p)
        if p in str(thithi) :
            # print(p)
            paksha_string = p
            # print(paksha_string)

    for t in thithis :
        if t in str(thithi) :
            thithi_string = t
            # print(thithi_string)

    panchang_var = PanchangObject(thithi_string.upper(), maasa_string.upper(), day_of_month_string.upper(), paksha_string.upper())

    return panchang_var