category = ['name', 'gender', 'age']
value = ['Francis', 'M', '38']

cat_val = list(zip(category, value))
result = {x: y for x, y in cat_val}

print(cat_val)
print(result)
