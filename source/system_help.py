from user1 import User

class SystemHelp:
  @staticmethod
  def register():
    username = input("Username:")
    password = input("Password:")
    fname = input ("First Name: ")
    lname = input ("Last Name: ")
    email = input("Email:")
    age = int(input("Age:"))

    return User(username,password,email,age,fname,lname)

  @staticmethod
  def login():
    username = input("Username: ")
    password = input("Password: ")

    return [username , password]
