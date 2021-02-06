class User:
  def __init__(self,username,password,email,age,fname,lname):
    self.username = username
    self.password = password
    self.email = email
    self.age = age
    self.fname = fname
    self.lname = lname

  def describe(self):
    return "Username: " + self.username + "/nEmail: " + self.email + "/nAge: " + str(self.age) + "/nFirst Name: " + self.fname + "/nLast Name: " + self.lname