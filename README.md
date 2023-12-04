# Project-Robotic-Arm-LLM
Assignments to be submitted here
class Rover:
    # Class attribute
    Rover_Geometry = (l, w, h)

    def __init__(self, Swarm_ID, Rover_ID, Rover_Location):
        # Instance attributes
        self.Swarm_ID = Swarm_ID
        self.Rover_ID = Rover_ID
        self.Rover_Location = Rover_Location

    def print_location(self):
        print(f"Rover Location: {self.Rover_Location}, Swarm ID: {self.Swarm_ID}, Rover ID: {self.Rover_ID}")

    def move_rover(self, message):
        if message.Swarm_ID == self.Swarm_ID and message.Rover_ID == self.Rover_ID:
            self.Rover_Location += message.move_distance

class DaughterRover(Rover):
    def __init__(self, Swarm_ID, Rover_ID, Rover_Location):
        super().__init__(Swarm_ID, Rover_ID, Rover_Location)
        self.Rover_Geometry = (l/2, w/2, h/2)

    def move_rover(self, message):
        if message.Swarm_ID == self.Swarm_ID and message.Rover_ID == self.Rover_ID:
            self.Rover_Location += message.move_distance/2

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.controlled_rovers = set()

    def print_user_id(self):
        print(f"User ID: {self.user_id}")

    def add_rover_to_control(self, rover):
        self.controlled_rovers.add((rover.swarm_id, rover.rover_id))
        print(f"Rover added to controlled rovers: Swarm ID {rover.swarm_id}, Rover ID {rover.rover_id}")

    def remove_rover_from_control(self, rover):
        self.controlled_rovers.remove((rover.swarm_id, rover.rover_id))
        print(f"Rover removed from controlled rovers: Swarm ID {rover.swarm_id}, Rover ID {rover.rover_id}")
    
    def new_feature(self, gyroscope_data, velocity_data):
    acceleration = calculate_acceleration(gyroscope_data, velocity_data)
    tilt_angle = calculate_tilt_angle(gyroscope_data)
    return acceleration, tilt_angle

class Scientist(User):
    def move_rover(self, rover, move_distance):
        print("Scientists can only view the rover location and are denied access to move the rover.")

class Operator(User):
    def move_rover(self, rover, move_distance):
        rover.move_rover(self.controlled_rovers, move_distance)

class Manager(User):
    def move_rover(self, rover, move_distance):
        rover.move_rover(self.controlled_rovers, move_distance)

    def add_rover_to_control(self, rover):
        super().add_rover_to_control(rover)

    def remove_rover_from_control(self, rover):
        super().remove_rover_from_control(rover)

