ziping1 = list(zip('<^>',['left', 'center', 'right']))
a = zip('123', ['a', 'b', 'c'])
print(type(ziping1))
print(type(a))
print(ziping1)
print()

for align, text in zip('<^>', ['a', 'b', 'c']):
  print('{0:{fill}{align}26}'.format(text, fill = align, align= align))

