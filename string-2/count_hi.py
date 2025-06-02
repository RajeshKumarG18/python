# Return the number of times that the string "hi" appears anywhere in the given string.

# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

def count_hi(str):
  result = 0
  a = range(len(str)-1)

  for a in range(len(str)-1):
      if str[a:a+2] == "hi":
          result += 1
  return result