def info_extract(maasa, thithi) :
    comma_index = maasa.index(",")
    maasa_string = maasa[comma_index+2:]
    day_of_month = maasa[:comma_index]
    print(maasa_string)
    print(day_of_month)
    print(thithi)