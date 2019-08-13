weather = open('weather.txt', 'a+')

weather.write("Rio de Janeiro,Brazil,30.0,18.0\n")

weather.seek(0,0)

headings = weather.readline().split(',')

while weather:
    city_temp = weather.readline().split(',')
    if city_temp == ['']: # kludge
        break
    else:
        print(headings[0].title(), 'of', city_temp[0].title(), headings[2], 'is', city_temp[2], 'Celsius')

weather.close()
