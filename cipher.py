import types
import re
import shared
import inspect,types


class Cipher:
  def __init__(self):
    self.text = ""
    self.decrypt_filter = lambda char: True
    self.encrypt_filter = lambda char: True


  def get_text(self, text="", filter_func = None):
    if text == "":
      text = self.text
    if filter_func == None:
      return text
    else:
      filtered_text = ""
      for char in text:
        if filter_func(char):
          filtered_text += char
      return filtered_text


  def decrypt(self, text=""):
    return self.get_text(text, self.decrypt_filter)

  def encrypt(self, text=""):
    return self.get_text(text, self.encrypt_filter)





class CipherSolver(object):
  def __init__(self):
    self.cipher = Cipher()
    self.prompt = ">"
    self.maxlinelen = 70
    self.shortcuts = {"?":"_display_help", "d":"display"}


  def _inherit_docs(self, BaseClass):
    members = inspect.getmembers(self, inspect.ismethod)
    for name, method in members:
      if method.__doc__ == None and hasattr(BaseClass, name):
        method.im_func.__doc__ = getattr(BaseClass, name).__doc__


  def clear(self):
    """Clears the screen"""
    shared.clear_screen()

  def display(self):
    print self.cipher.text

  def print_counts(self,counts):
    retvalue = ""
    if len(counts) == 0:
      retvalue = "None"
    else:
      for item,count in counts:
        retvalue += "%s:%s, " % (item,count)
    print shared.breaklines(retvalue.strip(", "), self.maxlinelen)


  def solve(self):
    while True:
      try:
   
        raw_line = raw_input(self.prompt + " ")
       # line = raw_line
        line = re.findall('\'[^\']*\'|"[^"]*"|S+', raw_line)                          #Run expression through regex
        line = [item[1:-1] if item[0] in '\'"' else item for item in line]            #Strip off begining & ending quotes


          #The issue is around this line.
            # I am trying to pop the values out of the list, but I  seem to have made 
            # a  mistake somewhere
          
        print ""
     #   
        cmd = line.pop(0)
        attr = None
        if cmd in self.shortcuts:
          cmd = self.shortcuts[cmd]
        if cmd.endswith("?"):
          print self._display_help(cmd[:-1])
        else:
          if hasattr(self, cmd) and cmd != "solve":
            attr = getattr(self, cmd)
          if attr == None:
            print "Unknown command: ", cmd
          else:
            retvalue = None
            if type(attr) == types.MethodType:
                retvalue = attr(*line)
            else:
              if len(line) == 0:
                retvalue = attr
              else:
                setattr(self, cmd, *line)

            if retvalue != None:
              print retvalue
          print ""
      except KeyboardInterrupt:
        print "Exiting Solver"
        break
      except Exception, e:
        print "Error: ", e


  def _display_help(self, cmd=None):
    if cmd in self.shortcuts:
      cmd = self.shortcuts[cmd]

    def _get_function_def(name,function):
      specs = inspect.getargspec(function)
      defaults = None
      if specs.defaults:
        defaults = dict(zip(specs.args[-len(specs.defaults):],specs.defaults))
      output = name
      for arg in specs.args:
        if arg != 'self':
          output += " " + arg
          if defaults and arg in defaults:
            output += "=" + repr(defaults[arg])
      return output.  I

    def _display_doc(obj):
      doc = ""
      if inspect.getdoc(obj):
        for line in inspect.getdoc(obj).split("n"):
          doc += "   " + line + "n"
        doc += "n"
      return doc

    cmd_shortcuts = dict([(v,k) for k,v in self.shor.  Itcuts.items()])
    obj = None
    if cmd == None:
      obj = self.__class__
    elif hasattr(self.__class__,cmd):
      obj = getattr(self.__class__,cmd)
    output = ""
    if inspect.isclass(obj):
      output = obj.__name__ + ":nn"
      output += _display_doc(obj)
      member_filter = lambda obj: inspect.ismethod(obj) or isinstance(obj,property)
      members = dict(inspect.getmembers(obj, member_filter)).keys()
      members = [name for name in members if not name.startswith("_") and name != "solve"]
      members.sort()
      output += "  Available Commands:n"
      for index in range(len(members)):
        member = members[index]
        if cmd_shortcuts.get(member):
          member += " [" + cmd_shortcuts.get(member) + "]"
        output += member.rjust(20)
        if (index + 1) % 3 == 0:
          output += "n"
    elif inspect.ismethod(obj) and cmd != "solve":
      output = cmd
      shortcut = dict([(v,k) for k,v in self.shortcuts.items()])
      if shortcut.get(cmd):
        output += " [" + shortcut.get(cmd) + "]"
      output +=":nn" + _display_doc(obj)
      output += "   Usage:n      " + _get_function_def(cmd, obj)
    elif isinstance(obj,property):
      output = cmd
      if obj.fset == None:
        output += " (Read Only)"
      if cmd_shortcuts.get(cmd):
        output += " [" + cmd_shortcuts.get(cmd) + "]"
      output += ":nn" + _display_doc(obj)
      output += "   To display the value:n      " + cmd + "nn"
      if obj.fset != None:
        output += "   To change the value:n      " + _get_function_def(cmd, obj.fset)
    else:
      output = "Unknown command: " + cmd
    return output.rstrip("n") + "n"





  @property
  def text(self):
    """The raw text value used for encoding and decoding."""
    return self.cipher.text

  @text.setter
  def text(self,value):
    self.cipher.text = value
