# Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'

def not_string(str):  
  if str.startswith('not'):
    return str
  else:
    return 'not ' + str
    
# if str.startswith('not'): It checks if the string begins with the word 'not'.
# return 'not ' + str It adds 'not ' in front of the string and returns the result.