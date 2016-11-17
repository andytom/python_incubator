#! /usr/bin/env python

#-- Helper functions ---------------------------------------------------------#
def all_equal(iterable):
    """
    Returns True if all items in the iterable are the same and False otherwise
    An empty iterable returns True.

    :param iterable: The iterable to check.

    :returns: True or False
    """
    return len(set(iterable)) <= 1


#-- Helper functions ---------------------------------------------------------#
class TicTacToeBoard(object):
    def __init__(self):
        self.board = [" " for i in range(9)]

    def have_winner(self):
        """
        Checks the board to see if there is a winner.
        If there is returns a the winner else returns False.
        """
        # Check rows
        if all_equal(self.board[:3]):
            return self.board[0]
        if all_equal(self.board[3:6]):
            return self.board[3]
        if all_equal(self.board[6:]):
            return self.board[6]

        # Check columns
        if all_equal(self.board[0::3]):
            return self.board[0]
        if all_equal(self.board[1::3]):
            return self.board[1]
        if all_equal(self.board[2::3]):
            return self.board[2]

        # Check diagonals
        if all_equal([self.board[0], self.board[4], self.board[8]]):
            return self.board[0]
        if all_equal([self.board[2], self.board[4], self.board[6]]):
            return self.board[2]
        return False

    def is_tied(self):
        return (" " not in self.board) and not self.have_winner

    def __repr__(self):
        return "TicTacToeBoard({})".format(self.board)

    def __str__(self):
        """
        print the board
        """
        return "\n".join([
            "|".join([i for i in self.board[:3]]),
            "-" * 5,
            "|".join([i for i in self.board[3:6]]),
            "-" * 5,
            "|".join([i for i in self.board[6:]])
        ])


if __name__ == '__main__':
    ttt = TicTacToeBoard()

    ttt.board = [
        'X', 'X', 'X',
        ' ', 'O', ' ',
        'O', ' ', 'O'
    ]

    print(ttt)
    winner = ttt.have_winner()
    if winner:
        print("The winner is {}".format(winner))
