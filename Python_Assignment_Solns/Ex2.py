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

#creating 3 rovers (instances of the Rover Class)
Rover_1=Rover(101,123,[1,2,3]) #list (x,y,z) for location
Rover_2=Rover(102,100,[0,0,0])
Rover_3=Rover(103,110,[5,5,5])
#changing the position of Rover_1
Rover_1.move_or_not(([101],[123],[1,1,1]))
#changing the position of Rover 2 but wrong rover_id
Rover_2.move_or_not(([101],[100],[2,1,2]))
#changing the position of Rover 3 but wrong Swarm id
Rover_3.move_or_not(([103],[111],[1,2,3]))
#printing the new details
Rover_1.get_details();
Rover_2.get_details();
Rover_3.get_details();
