#!/bin/python3
import sys
import random

class TicTacToe(object):

    def __init__(self, player_token, ai_marker):
        self.user_marker = player_token
        self.ai_marker = ai_marker
        self.winner = '-'
        self.board = self.set_board()
        self.current_marker = self.user_marker

    def play_turn(self, spot):

        if self.within_range(spot) and not self.spot_taken(spot):
            self.board[spot-1] = self.current_marker
            self.current_marker = self.ai_marker if self.current_marker == self.user_marker else self.user_marker
            return True
        else:
            return False

    def within_range(self, spot):
        return True if 1 <= spot <= 9 else False

    def spot_taken(self, spot):
        return (self.board[spot-1] != '-')

    @classmethod
    def set_board(cls):
        return ['-' for i in range(0,9)]

    def print_board(self):
        print("--- GAME ---\n")
        for i in range(0,len(self.board)):
            if (i % 3 == 0 and i != 0):
                print("\n--------------")

            line = ' | %s ' % (self.board[i])
            print(line, end="")
        print("\n")

    def print_index_board(self):
        print("--- Indexes ---\n")
        for i in range(0,9):
            if (i % 3 == 0 and i != 0):
                print("\n--------------")

            #line = ' | %s ' % (i)
            print(' | %s ' % (i+1), end="")
        print("\n")

    def have_winner(self):
        diagonals_and_middles = (self.right_diagonal() or\
                                self.left_diagonal() or \
                                self.middle_row() or \
                                self.second_col()) and \
                                self.spot_taken(5)
        top_row_and_first_col = (self.top_row() or \
                                self.first_col()) and \
                                self.spot_taken(1)
        bot_row_and_third_col = (self.bottom_row() or \
                                self.third_col()) and \
                                self.spot_taken(9)
        if diagonals_and_middles:
            self.winner = self.board[4]
        elif top_row_and_first_col:
            self.winner = self.board[0]
        elif bot_row_and_third_col:
            self.winner = self.board[8]
        return diagonals_and_middles or top_row_and_first_col or bot_row_and_third_col

    def top_row(self):
        return self.board[0] == self.board[1] == self.board[2]

    def middle_row(self):
        return self.board[3] == self.board[4] == self.board[5]

    def bottom_row(self):
        return self.board[6] == self.board[7] == self.board[8]

    def first_col(self):
        return self.board[0] == self.board[3] == self.board[6]

    def second_col(self):
        return self.board[1] == self.board[4] == self.board[7]

    def third_col(self):
        return self.board[2] == self.board[5] == self.board[8]

    def right_diagonal(self):
        return self.board[0] == self.board[4] == self.board[8]

    def left_diagonal(self):
        return self.board[2] == self.board[4] == self.board[6]

    def board_full(self):
        for i in range(0,9):
            if self.board[i] == '-':
                return False
        return True

    def game_over(self):
        game_has_winner = self.have_winner()
        if game_has_winner:
            if self.winner == self.ai_marker:
                return "I WIN!! YES!! YES!! I am the true master\n"
            else:
                return "Ok you've won this time, but I'll get you in the next one\n"
            # return "We have a winner!!!\nThe winner is %s" % self.winner
        elif self.board_full():
            return "Draw: Game Over!"
        else:
            return "notover"

class AI(object):
    @classmethod
    def pick_spot(cls, game):
        options = []
        for i in range(1,10):
            if not game.spot_taken(i):
                options.append(i)
        if len(options) > 0:
            return random.choice(options)
        else:
            raise Exception('No choices left bro')



print("=========================")
print("=== TIC TAC TOE GAME ====")
print("=========================\n\n")

print("You're about to witness a true MASTER playing!!\nChoose your weap.. ops, characters!")
playing = True
while (playing):
    print("enter player 1 char:")
    player1 = input()
    print("enter AI player char:")
    player2 = input()
    curr_game = TicTacToe(player1, player2)

    curr_game.print_index_board()
    print("starting... \n")

    while curr_game.game_over() == "notover":
        if curr_game.current_marker == curr_game.user_marker:
            print("It's your turn, pick an index:")
            p_spot = int(input())
            while not curr_game.play_turn(p_spot):
                print("Invalid spot, try again...\n")
                p_spot = int(input())
            print("You picked", p_spot)
            print("\n")
        else:
            print("It's my turn!!")
            try:
                ai_pic = AI.pick_spot(curr_game)
            except Exception:
                print("Error, no choices left\ngame over")
                playing = False
                sys.exit()
            curr_game.play_turn(ai_pic)
            print("I picked", ai_pic)
            print("\n")
        curr_game.print_board()

    print(curr_game.game_over())
    print("Do you want to play again? Enter Y for yes or anything else for no.")
    answer = input()
    playing = (answer == 'Y')
    if not playing:
        print("Ok chap, take care...")
