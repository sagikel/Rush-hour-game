#############################################################
# WRITER : sagikel
# DESCRIPTION : Classes.
#############################################################
from board import Board
from car import Car
import helper
import sys


class Game:
    """
    This object run the rush hour game.
    The object use the Board class and the Car class.
    It loud the board and the cars and move the cars on the board until the
    target cell.
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        letters_lst = {}
        for one_car in self.board.cars:
            name = one_car.get_name()
            ori = one_car.orientation
            if ori == 0:
                letters_lst[name] = ['u', 'd']
            else:
                letters_lst[name] = ['r', 'l']
        user_choice = input("what color car to move, "
                            "and what direction to move it?\nWrite here:")
        choice = user_choice.split(',')
        repeat = choice[0] in letters_lst and \
                 choice[1] in letters_lst[choice[0]]
        while not repeat:
            print('\nError typing - Make sure your typing is valid '
                  '(with comma and without space).\n')
            user_choice = input("Write here again:")
            choice = user_choice.split(',')
            repeat = choice[0] in letters_lst and \
                     choice[1] in letters_lst[choice[0]]
            if not repeat:
                continue
        if not self.board.move_car(choice[0], choice[1]):
            print('\nYou can not move this car to this direction!\nTry again.')

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        self.restart()
        target_cell = self.board.cell_content(self.board.target_location())
        if target_cell:
            print(self.board.__str__())
            print('\nGame initialized with vehicles that are already in a '
                  'state of success in the game.')
            repeat = False
        else:
            repeat = True
        while repeat:
            print(self.board.__str__())
            self.__single_turn()
            target_cell = self.board.cell_content(self.board.target_location())
            if target_cell:
                print(self.board.__str__())
                print('You did it, well done!')
                repeat = False

    def restart(self):
        """The function use the data from json file to create car objects at
        the beginning. In addition, it add the car to the board."""
        dic = helper.load_json(sys.argv[1])
        for key, value in dic.items():
            car = Car(key, value[0], value[1], value[2])
            if key not in ['R', 'G', 'W', 'O', 'B', 'Y']:
                continue
            if value[0] < 2 or 4 < value[0]:
                continue
            if value[2] != 0 and value[2] != 1:
                continue
            self.board.add_car(car)


if __name__ == '__main__':
    rush_hour = Game(Board())
    rush_hour.play()
