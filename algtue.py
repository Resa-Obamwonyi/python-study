import re


def autocorrect(text):
    pattern = r'yo(u)+'
    text_split = text.split(' ')
    # return text_split
    if len(text_split) > 1 and text_split[-1] == 'you.':
        text_split[-1] = 'your client.'
        return ' '.join(text_split)
    elif len(text_split) > 1:
        for x in text_split:
            if re.match(pattern, x, re.I):

        return ' '.join(text_split)
    else:
        return text

import re

def autocorrect(text):
  pattern = 'you+'
  text_split = text.split(' ')
  #return text_split
  if len(text_split) > 1 and text_split[-1] == 'you.':
    text_split[-1] = 'your client.'
    return ' '.join(text_split)
  elif len(text_split) > 1:
    for x in text_split:
      if re.match(pattern, x, re.I) == True:
        text_split[-1] = 'your client'
      return re.match(pattern, x, re.I)
      return ' '.join(text_split)
  else:
    return text