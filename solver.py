
import shared
from cipher import CipherSolver
from aristocrat import AristocratSolver
from patristocrat import PatristocratSolver

if __name__ == '__main__':
  solvers = {}
  for name, obj in globals().items():
    if name.endswith("Solver") and issubclass(obj, CipherSolver):
      solvers[name[:-6]] = obj

  while True:
    shared.clear_screen()
    print "-" * 37
    print "    NaijaSecForce Cryptogram Solver"
    print "-" * 37
    print "Type a cipher type or partial (q to quit) [all]: ",
    cmd = raw_input().lower()

    if cmd in ["q","quit"]:
      break
    else:
      list = []
      for name, obj in solvers.items():
        if name.lower().startswith(cmd):
          list.append(name)
      if len(list) > 0:
        list.sort()
        for index in range(1,len(list) + 1):
          print "  {0}. {1}".format(index, list[index-1])
        print "Type number of selection or return to go back: ",
        cmd = raw_input()
        if cmd.isdigit() and (0 < int(cmd) <= len(list)):
          name = list[int(cmd)-1]
          print "nLoaded {0} Solver.".format(name)
          solvers[name]().solve()
      print ""
