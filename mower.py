class Mower:
    """
    This class define a mower behavior
    """

    def __init__(self, X, Y, orientation, upper_right_corner_X, upper_right_corner_Y):
        """
        Constructor of the Mower class

        Parameters:
        -----------
        X: int, position in the axis of the mower
        Y: int, position on the ordinate of the mower
        orientation: int, orientation of the mower
        (1:nord, 2:south, 3:east, 4:west)
        upper_right_corner_X: int, upper right corner
        upper_right_corner_Y: int, upper right corner

        Return:
        -------
        None
        """
        self.X = X
        self.Y = Y
        self.orientation = orientation
        self.upper_right_corner_X = upper_right_corner_X
        self.upper_right_corner_Y = upper_right_corner_Y

    def verify_area(self, mowers_position):
        """
        check that the mower does not come out of the given area
        or that the area is empty

        Parameters:
        -----------
        mowers_position: dict, current positions of all the mower

        Return:
        -------
        0 if the area isn't aviable, 1: if the area is aviable
        """
        mowers_position_list = [value for value in mowers_position.values()]
        a = 1

        if(self.orientation == "N"):
            if(((self.X, self.Y+1) in mowers_position_list) |
               (self.Y+1 > self.upper_right_corner_Y)):
                a = 0
            else:
                a = 1

        elif(self.orientation == "S"):
            if(((self.X, self.Y-1) in mowers_position_list) | (self.Y-1 < 0)):
                a = 0
            else:
                a = 1

        elif(self.orientation == "E"):
            if(((self.X+1, self.Y) in mowers_position_list) |
               (self.X+1 > self.upper_right_corner_X)):
                a = 0
            else:
                a = 1

        elif(self.orientation == "W"):
            if(((self.X-1, self.Y) in mowers_position_list) | (self.X-1 < 0)):
                a = 0
            else:
                a = 1

        return a

    def switch_move_to_left(self, argument):
        """
        Switch function to select the new orientation

        Parameters:
        -----------
        argument: actual orientation of the mower

        Return:
        int, which is the new orientation of the mower after a left move
        -------
        """
        switcher = {
            "N": "W",
            "S": "E",
            "E": "N",
            "W": "S",
        }
        return switcher.get(argument, "N")

    def switch_move_to_rigth(self, argument):
        """
        Switch function to select the new orientation

        Parameters:
        -----------
        argument: actual orientation of the mower

        Return:
        int, which is the new orientation of the mower after a rigth move
        """
        switcher = {
            "N": "E",
            "S": "W",
            "E": "S",
            "W": "N",
        }
        return switcher.get(argument, "N")

    def move_forward(self, mowers_positon):
        """
        This function define

        Parameters:
        -----------
        mowers_positions:

        Return:
        -------
        None
        """
        if(self.verify_area(mowers_positon) == 1):
            if(self.orientation == "N"):
                self.Y = self.Y+1
            elif (self.orientation == "S"):
                self.Y = self.Y-1
            elif (self.orientation == "E"):
                self.X = self.X+1
            elif (self.orientation == "W"):
                self.X = self.X-1
        else:
            pass

    def move_to_left(self, orientation):
        """
        Function to set the orientation of the mower after left move

        Parameters:
        -----------
        orientation: actual orientation of the mower

        Return:
        None
        """
        self.orientation = self.switch_move_to_left(orientation)

    def move_to_rigth(self, orientation):
        """
        Function to set the orientation of the mower after rigth move

        Parameters:
        -----------
        orientation: actual orientation of the mower

        Return:
        -------
        None
        """
        self.orientation = self.switch_move_to_rigth(orientation)

    def __str__(self):
        """
        Overiding toString function

        Return:
        -------

        """
        return "position ({}, {}) orientation {}".format(self.X, self.Y, self.orientation)

    def get_mower_position(self):
        """
        get the position and the orientation of the mower

        Return:
        -------
        tuple which content position and orientation of the mower
        """
        return (self.X, self.Y, self.orientation)
