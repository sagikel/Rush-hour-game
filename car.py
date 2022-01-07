#############################################################
# FILE : ex9.py
# WRITER : Sagi Kelner , skelner , 203666516
# EXERCISE : intro2cs ex9 2018-2019
# DESCRIPTION : Classes.
#############################################################


class Car:
    """
    This class create car objects. It is used for the rush hour game.
    It responsible for all the data that can be change in the car object.
    """
    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        lst = []
        if self.orientation == 0:
            for i in range(self.length):
                row = self.location[0] + i
                lst.append((row, self.location[1]))
        if self.orientation == 1:
            for i in range(self.length):
                column = self.location[1] + i
                lst.append((self.location[0], column))
        return lst

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        if self.orientation == 0:
            return {'u': "cause the car to go up",
                    'd': "cause the car to go down"}
        elif self.orientation == 1:
            return {'r': "cause the car to go right",
                    'l': "cause the car to go left"}

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        if movekey == 'u':
            end_cell = self.car_coordinates()[0]
            return [(end_cell[0] - 1, end_cell[1])]
        elif movekey == 'd':
            end_cell = self.car_coordinates()[-1]
            return [(end_cell[0] + 1, end_cell[1])]
        elif movekey == 'r':
            end_cell = self.car_coordinates()[-1]
            return [(end_cell[0], end_cell[1] + 1)]
        elif movekey == 'l':
            end_cell = self.car_coordinates()[0]
            return [(end_cell[0], end_cell[1] - 1)]

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if movekey == 'u':
            self.location = self.movement_requirements('u')[0]
            return True
        elif movekey == 'd':
            self.location = self.car_coordinates()[1]
            return True
        elif movekey == 'r':
            self.location = self.car_coordinates()[1]
            return True
        elif movekey == 'l':
            self.location = self.movement_requirements('l')[0]
            return True
        else:
            return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.name
