import re

weather = '<div><p> 오늘 날짜: 9일 날씨:맑음 기온:21도 </p></div>'

weather_pattern = re.compile(r'(\d{1,2})일 날씨:([가-힣]+) 기온:(\d+)도')
searched = re.search(weather_pattern, weather)
print(searched.group(0))
print(searched.group(1))
print(searched.group(2, 3))
print(searched.groups())
