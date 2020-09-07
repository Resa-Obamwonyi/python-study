def is_isogram(str):
  if str == '':
    return True
  else:
    str = str.lower()
    new_str = ''.join([x for x in str if str.count(x) == 1])
    return str.lower() == new_str