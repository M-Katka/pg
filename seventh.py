from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
   def possible_moves(self):
       r, c = self.position
       d = 1 if self.color == 'white' else -1
       moves = [(r + d, c)]
       return [m for m in moves if self.is_position_on_board(m)]
   
   def __str__(self):
       return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
       r, c = self.position
       moves = [
           (r + 2, c + 1), (r + 2, c - 1),
           (r - 2, c + 1), (r - 2, c - 1),
           (r + 1, c + 2), (r + 1, c - 2),
           (r - 1, c + 2), (r - 1, c - 2)
       ]
       return [m for m in moves if self.is_position_on_board(m)]

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
   def possible_moves(self):
       r, c = self.position
       moves = []
       for i in range(1, 8):
           moves.extend([(r+i, c+i), (r+i, c-i), (r-i, c+i), (r-i, c-i)])
       return [m for m in moves if self.is_position_on_board(m)]

   def __str__(self):
       return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
   def possible_moves(self):
       r, c = self.position
       moves = []
       for i in range(1, 8):
           moves.extend([(r+i, c), (r-i, c), (r, c+i), (r, c-i)])
       return [m for m in moves if self.is_position_on_board(m)]

   def __str__(self):
       return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
   def possible_moves(self):
       r, c = self.position
       moves = []
       for i in range(1, 8):
           moves.extend([(r+i, c), (r-i, c), (r, c+i), (r, c-i)])
           moves.extend([(r+i, c+i), (r+i, c-i), (r-i, c+i), (r-i, c-i)])
       return [m for m in moves if self.is_position_on_board(m)]

   def __str__(self):
       return f'Queen({self.color}) at position {self.position}'


class King(Piece):
   def possible_moves(self):
       r, c = self.position
       moves = [
           (r+1, c), (r-1, c), (r, c+1), (r, c-1),
           (r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1)
       ]
       return [m for m in moves if self.is_position_on_board(m)]

   def __str__(self):
       return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    piece = Knight("black", (1, 2))
    print(piece)
    print(piece.possible_moves())