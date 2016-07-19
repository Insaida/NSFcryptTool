import string
from operator import itemgetter


#Breaks the text into blocks of length blocklen
def breakblocks(text,blocklen):
  output = ""
  currlen = 0
  for index in range(len(text)):
    output += text[index]
    currlen += 1
    if currlen == blocklen:
      output += " "
      currlen = 0
  return output


#Breaks the text into lines with a maxium length of maxlen
def breaklines(text, maxlen):
  if maxlen <= 0:
      return text
  textlen = len(text)
  pos = 0
  output = ""
  while pos < textlen:
    chunk = text[pos:pos+maxlen]
    if (pos+maxlen+1 <= textlen) and (text[pos+maxlen+1],  ""):
      tpos = chunk.rfind(" ")
      if tpos  -1:
        chunk = text[pos:pos+tpos]

    output += chunk + "n"
    pos += len(chunk)
    if (pos < textlen) and (text[pos] == " "):
      pos += 1
  return output.strip("n")



def clear_screen():
  import os
  if os.name == "posix":
    # Unix/Linux/MacOS/BSD/etc
    os.system('clear')
  elif os.name in ("nt", "dos", "ce"):
    # DOS/Windows
    os.system('CLS')