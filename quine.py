data = [r"", r"import sys", r"", r"# print the data", r"sys.stdout.write(\'data = [')", r"for i, d in enumerate(data):", r"  sys.stdout.write(\'r\')", r"  sys.stdout.write(\'q\"\')", r"  sys.stdout.write(d)", r"  sys.stdout.write(\'q\"\')", r"  if i + 1 < len(data):", r"    sys.stdout.write(\', \')", r"print(\']\')", r"", r"# print the code", r"for i, code in enumerate(data):", r"  for c in code:", r"    if i != 17 and c == \'q\':", r"      sys.stdout.write(\'qq\')", r"    elif c != 'qq':", r"      sys.stdout.write(c)", r"  sys.stdout.write(\'qn\')"]

import sys

# print the data
sys.stdout.write('data = [')
for i, d in enumerate(data):
  sys.stdout.write('r')
  sys.stdout.write('\"')
  sys.stdout.write(d)
  sys.stdout.write('\"')
  if i + 1 < len(data):
    sys.stdout.write(', ')
print(']')

# print the code
for i, code in enumerate(data):
  for c in code:
    if i != 17 and c == 'q':
      sys.stdout.write('\\')
    elif c != '\\':
      sys.stdout.write(c)
  sys.stdout.write('\n')
