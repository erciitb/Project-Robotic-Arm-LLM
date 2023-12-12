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

        print("Rover Geometry: ",str(self.Rover_Geometry_lwh))
        print("Rover Id: ",str(self.Rover_Id))
        print("Swarm Id: ",str(self.Swarm_Id))
        print("Rover Location: ",str(self.Rover_Loc))

#creating 3 rovers (instances of the Rover Class)
Rover_1=Rover(101,123,[1,2,3]) #list (x,y,z) for location
Rover_2=Rover(102,100,[0,0,0])
Rover_3=Rover(103,110,[5,5,5])
#printing the details of Rover_1
Rover_1.get_details();
Rover_2.get_details();
Rover_3.get_details();
