# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

#non_start('Hello', 'There') → 'ellohere'
#non_start('java', 'code') → 'avaode'
#non_start('shotl', 'java') → 'hotlava'

def non_start(a, b):
  result = ''
  new_a = ''
  for i in range(len(a)):
        if i != 0:
            new_a += a[i]
  new_b = ''
  for i in range(len(b)):
        if i != 0:
            new_b += b[i]
  result = new_a + new_b
  return result