def get_middle(str):
  if len(str) == 1:
    return str
  elif len(str) == 2:
    return str
  else:
    middle_num = int(round(len(str)/2))
    #return middle_num
    if len(str) % 2 != 0:
      return list(str)[middle_num]
    else:
      return list(str)[middle_num-1] + list(str)[middle_num]