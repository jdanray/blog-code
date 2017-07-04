data = [r"", r"from sys import stdout", r"", r"stdout.write(\'data = [')", r"for i, d in enumerate(data):", r"  stdout.write(\'r\')", r"  stdout.write(\'q\"\')", r"  stdout.write(d)", r"  stdout.write(\'q\"\')", r"  if i + 1 < len(data):", r"    stdout.write(\', \')", r"print(\']\')", r"", r"for i, code in enumerate(data):", r"  for c in code:", r"    if i != 15 and c == \'q\':", r"      stdout.write(\'qq\')", r"    elif c != 'qq':", r"      stdout.write(c)", r"  stdout.write(\'qn\')"]

from sys import stdout

stdout.write('data = [')
for i, d in enumerate(data):
  stdout.write('r')
  stdout.write('\"')
  stdout.write(d)
  stdout.write('\"')
  if i + 1 < len(data):
    stdout.write(', ')
print(']')

for i, code in enumerate(data):
  for c in code:
    if i != 15 and c == 'q':
      stdout.write('\\')
    elif c != '\\':
      stdout.write(c)
  stdout.write('\n')
