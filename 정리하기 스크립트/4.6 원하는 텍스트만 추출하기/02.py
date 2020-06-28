import re

text = '<em>와! 세탁기 마음에 들어요!</em> 조용하네요.'

tag_pattern = re.compile(r'</?.+>')
tags = re.findall(tag_pattern, text)
print(tags)
