# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'

def left2(str):
    result = ''
i = range(2, len(str))
for i in range(2, len(str)):
    if len(str) >= 2:
      result += str[i]
result += str[0] + str[1]       
return result
return ('') + str