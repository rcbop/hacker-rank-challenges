#!/bin/python3
import sys
import random
import copy

class TicTacToe(object):

    AI_WIN="I WIN!! YES!! YES!! I am the true master\n"
    USER_WIN="Ok you've won this time, but I'll get you in the next one\n"

    def __init__(self, player_token, ai_marker):
        self.user_marker = player_token
        self.ai_marker = ai_marker
        self.winner = '-'
        self.board = self.set_board()
        self.current_marker = self.user_marker
        self.last_pick = -1

    def play_turn(self, spot):

        if self.within_range(spot) and not self.spot_taken(spot):
            self.board[spot-1] = self.current_marker
            self.current_marker = self.ai_marker if self.current_marker == self.user_marker else self.user_marker
            self.last_pick = spot
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
        print(bcolors.ENDC)
        for i in range(0,len(self.board)):
            if (i % 3 == 0 and i != 0):
                print("\n\x1b[3;34;40m---------------\x1b[0m")

            line = ' | %s ' % (self.board[i])
            if self.last_pick == (i+1):
                line = "\x1b[3;31;40m" + line + "\x1b[0m"
            else:
                line = "\x1b[3;34;40m" + line + "\x1b[0m"

            print(line, end="")
        print("\n"+bcolors.ENDC+bcolors.BOLD)

    def print_index_board(self):
        print(bcolors.HEADER+"--- Indexes ---\n")
        for i in range(0,9):
            if (i % 3 == 0 and i != 0):
                print("\n--------------")

            #line = ' | %s ' % (i)
            print(' | %s ' % (i+1), end="")
        print("\n"+bcolors.ENDC+bcolors.BOLD)

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
                return self.AI_WIN
            else:
                return self.USER_WIN
            # return "We have a winner!!!\nThe winner is %s" % self.winner
        elif self.board_full():
            return "Draw: Game Over!"
        else:
            return "notover"

from abc import ABCMeta, abstractmethod

class AI(object):
    @abstractmethod
    def pick_spot(self):
        pass

    def random_option(self, game):
        options = []
        for i in range(1,10):
            if not game.spot_taken(i):
                options.append(i)
        if len(options) > 0:
            return random.choice(options)
        else:
            raise Exception("No choices left bro, I'm confused")

class DumbAI(AI):
    def pick_spot(self, game):
        return self.random_option(game)

class SmartAI(AI):
    def pick_spot(self, game):
        # print("DEBUG",game.ai_marker, game.user_marker)

        # print("trying to win first")
        move = self.check_win_move(game, game.ai_marker, game.AI_WIN)
        if move != None:
            return move

        # print("trying to avoid that you win")
        move = self.check_win_move(game, game.user_marker, game.USER_WIN)
        if move != None:
            return move

        # print("trying to pick a corner")
        move = self.choose_random_move_from_list(game, [1, 3, 7, 9])
        if move != None:
            return move

        # print("trying to pick the center")
        if not game.spot_taken(5):
            return 5

        # print("picking anything else")
        return self.choose_random_move_from_list(game, [2, 4, 6, 8])

    def check_win_move(self, game, marker, win_message):
        for i in range(1,10):
            game_copy = copy.deepcopy(game)
            game_copy.current_marker = marker
            if not game_copy.spot_taken(i):
                game_copy.play_turn(i)
                if game_copy.game_over() == win_message:
                    return i
        return None

    def choose_random_move_from_list(self, game, move_list):
        choices = []
        for i in move_list:
            if not game.spot_taken(i):
                choices.append(i)

        if len(choices) > 0:
            return random.choice(choices)
        else:
            return None

class Helper(object):
    @classmethod
    def should_loop(cls, user_input, previous_input):
        if previous_input != None:
            return (user_input == '' or previous_input == user_input)
        else:
            return user_input == ''

    @classmethod
    def validate_input(cls, user_input, previous_input):
        while Helper.should_loop(user_input, previous_input):
            print(bcolors.FAIL+'no good, pick another one'+bcolors.OKBLUE+bcolors.BOLD)
            user_input = input()
        return user_input

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("\n")
print("\x1b[1;37;40m=========================\x1b[0m")
print("\x1b[1;37;40m=== TIC TAC TOE GAME ====\x1b[0m")
print("\x1b[1;37;40m=========================\x1b[0m\n")

print(bcolors.BOLD+"You're about to witness a true MASTER playing!!\nChoose your weap.. oh, characters!\n")
playing = True
while (playing):
    print("NEW GAME... \n")

    print("enter player 1 char:")
    player1 = Helper.validate_input(input(), None)
    print("\nok, player picked", player1, "\n")

    print("enter AI player char:")
    player2 = Helper.validate_input(input(), player1)
    print("\nok, I'll use", player2, "\n")

    curr_game = TicTacToe(player1, player2)

    print("choose the level of difficulty, type: (E)asy or (H)ard")
    difficulty = input().lower()
    while difficulty not in ["easy","hard"]:
        print(bcolors.FAIL+"invalid choice bro, try again"+bcolors.OKBLUE)
        difficulty = input().lower()

    if difficulty == "easy" or difficulty == "e":
        print("\nI feel dumber already\n")
        ai = DumbAI()
    elif difficulty == "hard" or difficulty == "h":
        print("\nI will own you!\n")
        ai = SmartAI()

    print("Alright, let's do this!\n")

    curr_game.print_index_board()

    while curr_game.game_over() == "notover":
        if curr_game.current_marker == curr_game.user_marker:
            print("It's your turn, pick an index:")
            p_spot = int(input())
            while not curr_game.play_turn(p_spot):
                print(bcolors.FAIL+"Invalid spot, try again...\n"+bcolors.ENDC+bcolors.BOLD)
                p_spot = int(input())
            print("You picked","\x1b[6;30;42m", p_spot, "\x1b[0m")
            print("\n")
        else:
            print("It's my turn!!")
            ai_pic = ai.pick_spot(curr_game)
            curr_game.play_turn(ai_pic)
            print("I picked","\x1b[6;30;42m",ai_pic,"\x1b[0m")
            print("\n")
        curr_game.print_board()

    print(curr_game.game_over())
    print("Do you want to play again? Enter (Y)es or anything else for no.")
    answer = input().lower()
    playing = (answer == 'y' or answer == "yes")
    if not playing:
        print(bcolors.UNDERLINE+"Ok chap, take care...")
