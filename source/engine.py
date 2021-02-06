from system import System
from system_help import SystemHelp
from os import system,name


class Engine:
  def __init__(self):
    self.manager = System()

  def execute_operation(self,number):
    if number == 1:
      login_info = SystemHelp.login()
      self.manager.login(login_info[0],login_info[1])
    elif number == 2:
      usr = SystemHelp.register()
      self.manager.register(usr)
    elif number == 3:
      self.manager.logout()
    elif number == 4:
      self.manager.perform_system_check()

  def system_clear(self):
    if name == 'nt':
      system('cls')
    else:
      system('clear')

  def run(self):
    print("1.Login")
    print("2.Register")
    print("3.Logout")
    print("4.System check")
    print("5.Exit the program")
    print()
    operation = int(input())
    if operation != 5:
      self.execute_operation(operation)
      input()
      self.system_clear()
      self.run()
    else:
      print("Goodbye")


    