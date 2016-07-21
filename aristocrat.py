##Simple Substutition cipher without spaces left between the wordpress


import string
from cipher import *
from cipher import Cipher


import shared


class Aristocrat(Cipher):
  def __init__(self):
    Cipher.__init__(self)
    self.ctkey = string.ascii_uppercase
    self.ptkey = "-" * 26
    self.decrypt_filter = lambda char: char in (string.ascii_letters + string.punctuation + " ")
    self.encrypt_filter = self.decrypt_filter


  def decrypt(self, text = ""):
    text = Cipher.decrypt(self, text)
    return self.process(self.ctkey, self.ptkey, text.upper())

  def encrypt(self, text = ""):
    text = Cipher.encrypt(self, text)
    return self.process(self.ptkey, self.ctkey, text.lower())

  def process(self, key1, key2, text):
    output = ""
    for char in text:
      if char in key1:
        output += key2[key1.index(char)]
      elif char.lower() in string.ascii_lowercase:
        output += "-"
      else:
        output += char
    return output


  def set(self, ct, pt = "-"):
    ct = ct.upper()
    pt = pt.lower()
    if pt == "-":
      pt = "-" * len(ct)
    for index in range(len(ct)):
      ctindex = self.ctkey.index(ct[index])
      self.ptkey = self.ptkey[:ctindex] + pt[index] + self.ptkey[ctindex+1:]



class AristocratSolver(CipherSolver):
  def __init__(self):
    CipherSolver.__init__(self)
    self.cipher = Aristocrat()
    self.shortcuts['f'] = 'frequency_list'
    self.shortcuts['k'] = 'keys'
    self.shortcuts['s'] = "set"
    self._inherit_docs(CipherSolver)


  def display(self):
    data = ""
    ct = shared.breaklines(Cipher.encrypt(self.cipher), self.maxlinelen).split("n")
    pt = shared.breaklines(self.cipher.decrypt(), self.maxlinelen).split("n")

    for index in range(len(ct)):
      data += ct[index] + "n"
      data += pt[index] + "nn"
    print data.strip("n")

  def frequency_list(self, length = 1, text = ""):
    """Displays counts for frequencies of characters"""
    text = Cipher.encrypt(self.cipher, text)
    self.print_counts(shared.calc_graphs(text.split(" "), int(length)))


  def keys(self):
    """Displays the plaintext and ciphertext keys."""
    print "ct:", self.cipher.ctkey, "npt:", self.cipher.ptkey, "n"
    values = zip(self.cipher.ptkey, self.cipher.ctkey)
    values.sort()
    ptval=""
    ctval=""
    for pt,ct in values:
      ptval += pt
      ctval += ct
    print "pt:",ptval, "nct:", ctval


  def set(self, ct, pt = "-"):
    """Sets the plaintext equivalent for each ciphertext character.
    You can enter multiple letters at a time.
    Enter a single dash '-' to set the plaintext characters to blank."""

    self.cipher.set(ct,pt)
    self.display()