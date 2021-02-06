class System:
  def __init__(self):
    self.current_user = None
    self.users = dict()
  
  def login(self,username, password):
    if username in self.users:
      self.current_user = self.users[username]
    else:
      print("No such user cannot login into system")

  def logout(self):
    if self.current_user != None:
      print("Logging out:", self.current_user.username)
    else:
      print("No user to logout")

  def register(self,user):
    if user.username not in self.users :
      self.users[user.username] = user
    else:
      print("There already exists user with this username")

  def perform_system_check(self):
    if self.current_user != None:
      for user in self.users.values():
        print(user.describe())
    else:
      print("Cannot perform system check!")