import string
import shared
from cipher import Cipher
from aristocrat import Aristocrat, AristocratSolver

class Patristocrat(Aristocrat):
    def __init__(self):
        Aristocrat.__init__(self)
        self.decrypt_filter = lambda char: char in string.ascii_letters
        self.encrypt_filter = self.decrypt_filter



class PatristocratSolver(AristocratSolver):
    def __init__(self):
        AristocratSolver.__init__(self)
        self.cipher = Patristocrat()
        self._inherit_docs(AristocratSolver)

    def display(self):
        data = ""
        ct = shared.breakblocks(Cipher.encrypt(self.cipher), 5)
        ct = shared.breaklines(ct, self.maxlinelen).split("n")
        pt = shared.breakblocks(self.cipher.decrypt(), 5)
        pt = shared.breaklines(pt, self.maxlinelen).split("n")

        for index in range(len(ct)):
            data += ct[index] + "n"
            data += pt[index] + "nn"
            print data.strip("n") 

    def frequency_list(self, length = 1, text = ""):
        text = Cipher.encrypt(self.cipher, text)
        self.print_counts(shared.calc_graphs(text, int(length)))