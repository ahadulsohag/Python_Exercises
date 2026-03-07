num_1 = 19
num_2 = 22
print('{:.2%}'.format(num_1/num_2))
import datetime
d = datetime.datetime(2026, 3, 6, 7, 59)
printt= '{:%Y-%m-%d %H:%M:%Spm}'.format(d)
print(printt)

for align, text in zip('<^>', ['left', 'center', 'right']):
      '{0:{fill}{align}16}'.format(text, fill=align, align=align)
  # Returns:
  # 'left<<<<<<<<<<<<'
  # '^^^^^center^^^^^'
  # '>>>>>>>>>>>right'
print(len('>>>>>>>>>>>right'))