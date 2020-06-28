import re

weathers = '9일 날씨:맑음 기온:21도 / 10일 날씨:흐림 기온:18도'

weather_pattern = re.compile(r'(\d{1,2})일 날씨:([가-힣]+) 기온:(\d+)도')
print(re.findall(weather_pattern, weathers))
