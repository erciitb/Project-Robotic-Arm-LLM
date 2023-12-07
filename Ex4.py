class Rover:
    #defining the l,w,h (geometry) as class attributes
    #shared among all the objects of the class

    Rover_Geometry_lwh=[20,10,15] #list storing the common lwh for the rovers

    def __init__(self,Rover_Id,Swarm_Id,Rover_Loc):
        #constructor that defines the instant attributes
        #Unique for all instances of the class
        self.Rover_Id=Rover_Id
        self.Swarm_Id=Swarm_Id
        self.Rover_Loc=Rover_Loc

    def get_details(self):
        #printing the details of the current rover instance
        print("Rover Geometry: ",str(self.Rover_Geometry_lwh))
        print("Rover Id: ",str(self.Rover_Id))
        print("Swarm Id: ",str(self.Swarm_Id))
        print("Rover Location: ",str(self.Rover_Loc))

    def get_Rover_Id(self):
        return self.Rover_Id;
    def get_Swarm_Id(self):
        return self.Swarm_Id;
    def get_loc(self):
        return self.Rover_Loc;
    def change(self,motion):
        #updating the location if the Id's match
        self.Rover_Loc[0]+=motion[0]
        self.Rover_Loc[1] += motion[1]
        self.Rover_Loc[2]+= motion[2]

    def move_or_not(self,msg):
        if(self.Rover_Id==msg[0][0]):#checking for the Rover Id
            if(self.Swarm_Id==msg[1][0]):#checking for the Swarm Id
                self.change(msg[2])#changing the location if the ID's match
            else:
                print("No match")

        else:
            print("No match")
class Daughter_Rover(Rover):
    Daughter_Rover_lwh=[10,5,7.5]
    #this change function overwrites the one in the class rover
    def change(self,motion):
        #updating the location if the Id's match
        self.Rover_Loc[0]+=motion[0]/float(2)
        self.Rover_Loc[1] += motion[1]/float(2)
        self.Rover_Loc[2]+= motion[2]/float(2)
class User(Daughter_Rover):
    id=[[]]
    def __init__(self,User_Id):
        self.User_Id=User_Id
class Manager(User):
    def __init__(self,User_Id):
        super().__init__(User_Id)
    def add_new(self,rover):  #for manager to add rovers
        boolean = False
        for i in range(len(self.id)):
            if self.id[i] == [rover.Swarm_Id, rover.Rover_Id]:
                boolean = True
        if boolean == False:
            (self.id).append([rover.Swarm_Id, rover.Rover_Id])
        else:
            print('Already there')

    def remove(self, rover): #for managers to remove rovers

        boolean = False

        for i in range(len(self.id)):
            if self.id[i] == [rover.Swarm_Id, rover.Rover_Id]:
                boolean = True

        if boolean == True:
            (self.id).remove([rover.Swarm_Id, rover.Rover_Id])
        else:
            print('Not there')
class Scientist(User):

  def __init__(self, userid):
    super().__init__(userid)

  def view(self, rover):    #for scientists to view the location of rovers

    boolean = False

    for i in range(len(self.id)):
      if self.id[i] == [rover.Swarm_Id, rover.Rover_Id]:
        rover.get_details()
        boolean = True

    if boolean == False:
      print('Not there')
class Operator(User):

  def __init__(self, userid):
    super().__init__(userid)

  def control(self, rover, disp):     #for operators to change the location of rovers

    boolean = False

    for i in range(len(self.id)):
      if self.id[i] == (rover.Swarm_Id, rover.Rover_Id):
        rover.move_or_not(disp)
        boolean = True

    if boolean == False:
      print('Not there')

  def find(self, rover1, rover2):

    boolean1 = False
    boolean2 = False

    for i in range(len(self.id)):
      if self.id[i] == [rover1.get_Swarm_Id(), rover1.get_Rover_Id()]:
        boolean1 = True
        for j in range(len(self.id)):
          if self.id[j] == [rover2.get_Swarm_Id(), rover2.get_Rover_Id()]:
            boolean2 = True
            rover1.Rover_Loc = rover2.Rover_Loc

    if boolean1 == False and boolean2 == False:
      print('Not there')
#checking using some  cases
rover1 = Rover(1, 1, [1,1,1])
rover2 = Rover(2, 2, [1,0,2])
rover1.get_details()
manager1 = Manager(1)
scientist1 = Scientist(2)
manager1.add_new(rover2)
scientist1.view(rover2)
scientist1.view(rover1)
operator1 = Operator(3)
operator1.control(rover2, [5,0,0])
manager1.add_new(rover1)
operator1.find(rover1, rover2)
scientist1.view(rover2)
scientist1.view(rover1)
