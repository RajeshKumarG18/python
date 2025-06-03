# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

def xyz_there(str):
  j = range(len(str)-2)
  for j in range(len(str)-2):
    if str[j:j+3] == "xyz":
      
      if j == 0 or str[j-1] != ".":
        return True
  else:
        return False