def info_extract(maasa, thithi) :
    comma_index = maasa.index(",")
    maasa_string = maasa[comma_index+2:]
    day_of_month = maasa[:comma_index]
    print(maasa_string)
    print(day_of_month)
    
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
            paksha = p
            print(paksha)

    for t in thithis :
        if t in str(thithi) :
            thithi_string = t
            print(thithi_string)
    
    