# Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

# without_end('Hello') → 'ell'
# without_end('java') → 'av'
# without_end('coding') → 'odin'

def without_end(str):
    result = ''
i = range(len(str))
for i in range(len(str)-1):
    if i != 0 and i != (len(str)-1):
        result += str[i]
return result