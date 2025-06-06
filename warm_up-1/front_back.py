# Given a string, return a new string where the first and last chars have been exchanged.

# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(str):
  mid = str[1:len(str)-1]
  if len(str) <= 1:
    return str
  else:
      return str[len(str)-1] + mid + str[0]