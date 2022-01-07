#############################################################
# FILE : ex9.py
# WRITER : Sagi Kelner , skelner , 203666516
# EXERCISE : intro2cs ex9 2018-2019
# DESCRIPTION : Classes.
#############################################################


class Board:
    """
    This class create board object and use the Car class.
    It responsible for all the board creation and cars move on the board.
    for one rush hour game there will be only one board object.
    """

    def __init__(self):
        """
        A constructor for a Board object.
        """
        self.size = 7
        self.cars = []

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        board_lists = [['_'] * self.size for rows in range(self.size)]
        board_lists[3].append('>')
        for one_car in self.cars:
            for cell in one_car.car_coordinates():
                board_lists[cell[0]][cell[1]] = one_car.get_name()
        board_image = ''
        for i in board_lists:
            for j in i:
                board_image += j + ' '
            board_image += '\n'
        return board_image

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        cell_lst = []
        for i in range(self.size):
            for j in range(self.size):
                cell = (i, j)
                cell_lst.append(cell)
        cell_lst.append((3, 7))
        return cell_lst

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        lst = []
        for one_car in self.cars:
            if one_car.orientation == 0:
                if one_car.location[0] != 0:
                    argument = one_car.get_name(), \
                               'u', "cause the car to go up"
                    lst.append(argument)
                if one_car.location[0] != 6:
                    argument = one_car.get_name(), \
                               'd', "cause the car to go down"
                    lst.append(argument)
            elif one_car.orientation == 1:
                if one_car.location[1] != 0:
                    argument = one_car.get_name(), \
                               'r', "cause the car to go right"
                    lst.append(argument)
                if one_car.location[1] != 6:
                    argument = one_car.get_name(), \
                               'l', "cause the car to go left"
                    lst.append(argument)
        return lst

    def target_location(self):
        """
        This function returns the coordinates of the location which is
        to be filled for victory.
        :return: (row,col) of goal location
        """
        return 3, 7

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        for one_car in self.cars:
            for cell in one_car.car_coordinates():
                if cell == coordinate:
                    name = one_car.get_name
                    return name
        return None

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        for cell in car.car_coordinates():
            if self.cell_content(cell) is not None:
                return False
            if cell not in self.cell_list():
                return False
        self.cars.append(car)
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        for one_car in self.cars:
            name1 = one_car.get_name()
            if name == name1:
                cell_lst = one_car.movement_requirements(movekey)
                if cell_lst[0][0] < 0 or cell_lst[0][0] > 6 \
                    or cell_lst[0][1] < 0 \
                        or cell_lst[0] \
                        in [(0, 7), (1, 7), (2, 7), (3, 8),
                            (4, 7), (5, 7), (6, 7)]:
                    return False
                cell_empty = self.cell_content(cell_lst[0])
                if cell_empty is not None:
                    return False
                one_car.move(movekey)
                return True
        return False
