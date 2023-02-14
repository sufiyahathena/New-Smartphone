#Sufiyah Sajan
#Object_Oriented Programming

# Part C

class Smartphone:
    
    def __init__(self, capacity, name):
        print("Smartphone created!")
        self.apps = {}
        self.capacity = capacity
        self.name = name
        self.used_space = 0
        self.available_space = capacity
        
    def add_app(self, appname, appsize):
        if appname in self.apps:
            print("App already installed on smartphone")
            return
        elif int(self.available_space) < appsize:
            print("Not enough memory on smartphone")
        else:
            self.apps[appname] = appsize
            self.available_space = int(self.available_space) - int(appsize)
            self.used_space += int(appsize)
  
    def remove_app(self, appname):
        if appname in self.apps:
            self.available_space = int(self.available_space) + self.apps[appsize]
            appsize = self.apps.pop(appname)
            self.used_space -= int(appsize)
            del self.apps[appsize]
            #key error
        else:
            print("App not installed.")

    def has_app(self, appname):
        if appname in self.apps:
            return True
        else:
            return False

    def get_available_space(self):
        return int(self.capacity) - int(self.used_space)

    def report(self):
        print("Name: {}'s phone".format(self.name))
        print("Capacity: ", self.used_space, "out of", self.capacity, "GB")
        print("Available Space: ", self.get_available_space())
        print("Apps Installed: ", len(self.apps))
        #print entire list of apps
        if len(self.apps) > 0:
            for apps in self.apps:
                print("- {} is using {} GB".format(appname, appsize))
        print()

capacity = input("Size of your new smartphone (32, 64, or 128 GB): ")
while int(capacity) != 32 and int(capacity) != 64 and int(capacity) != 128:
    print("Invalid Input.")
    capacity = input("Size of your new smartphone (32, 64, or 128 GB): ")
name = str(input("Smartphone name: "))

phone = Smartphone(capacity, name)
phone.report()

cont = 'yes'
while cont!= 'q':
    cont = input("(r)eport, (a)dd app, r(e)move app or (q)uit: ")
    if cont == 'a':
        appname = input("App name to add: ")
        appsize = int(input("App size in GB: "))
        phone.add_app(appname, appsize)
        print()
 #       cont = input("(r)eport, (a)dd app, r(e)move app or (q)uit: ")
    elif cont == 'r':
        phone.report()
        print()
 #       cont = input("(r)eport, (a)dd app, r(e)move app or (q)uit: ")
    elif cont == 'e':
        appname = input("App name to remove: ")
        phone.remove_app(appname)
        print("App removed: ", appname)
        print()
  #      cont = input("(r)eport, (a)dd app, r(e)move app or (q)uit: ")
    elif cont == 'q':
        print("Goodbye!")
        break
        
