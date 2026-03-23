# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0

def diff21(n):
  if n >= 21:
    return 2 * abs(n - 21)
  else:
    return abs(n - 21)
  
# Steps:-
# 1. Find the absolute difference between n and 21 abs(n - 21)
# If n is greater than 21, then return double that absolute difference. if n >= 21: return 2 * abs(n - 21)
# If n is 21 or less, else return the absolute difference.