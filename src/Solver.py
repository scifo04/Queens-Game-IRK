from ColorAssigner import ColorAssigner
from BoardPiece import BoardPiece
from Piece import Piece

class Solver:
    colorController: ColorAssigner
    chessPiece: str
    matrix: BoardPiece
    solutions: list

    def __init__ (self, coleur, chess):
        self.colorController = coleur
        self.chessPiece = chess
        self.matrix = self.colorController.boardPiece
        self.solutions = []

    def xIfyVert (self, row, col):
        for i in range(len(self.matrix.Board)):
            if (i != row):
                self.matrix.Board[i][col].Xed += 1

    def xIfyHorz (self, row, col):
        for i in range(len(self.matrix.Board[row])):
            if (i != col):
                self.matrix.Board[row][i].Xed += 1

    def xIfyDiagDownRight (self, row, col):
        i = row
        j = col
        while (i > 0 and j > 0):
            i -= 1
            j -= 1
        while (i < len(self.matrix.Board) and j < len(self.matrix.Board[i])):
            if (i != row and j != col):
                self.matrix.Board[i][j].Xed += 1
            i += 1
            j += 1
        
    def xIfyDiagDownLeft(self, row, col):
        i = row
        j = col
        while (i > 0 and j < len(self.matrix.Board[i])-1):
            i -= 1
            j += 1
        while (i < len(self.matrix.Board) and j > 0):
            if (i != row and j != col):
                self.matrix.Board[i][j].Xed += 1
            i += 1
            j -= 1

    def xIfySingleDiag(self,row,col):
        if (row+1 < len(self.matrix.Board) and col+1 < len(self.matrix.Board[row])):
            self.matrix.Board[row+1][col+1].Xed += 1
        if (row+1 < len(self.matrix.Board) and col-1 >= 0):
            self.matrix.Board[row+1][col-1].Xed += 1
        if (row-1 >= 0 and col-1 >= 0):
            self.matrix.Board[row-1][col-1].Xed += 1
        if (row-1 >= 0 and col+1 < len(self.matrix.Board[row])):
            self.matrix.Board[row-1][col+1].Xed += 1

    def xIfyL(self, row, col):
        if (row+2 < len(self.matrix.Board) and col+1 < len(self.matrix.Board[row])):
            self.matrix.Board[row+2][col+1].Xed += 1
        if (row+2 < len(self.matrix.Board) and col-1 >= 0):
            self.matrix.Board[row+2][col-1].Xed += 1
        if (row-2 >= 0 and col-1 >= 0):
            self.matrix.Board[row-2][col-1].Xed += 1
        if (row-2 >= 0 and col+1 < len(self.matrix.Board[row])):
            self.matrix.Board[row-2][col+1].Xed += 1
        if (row+1 < len(self.matrix.Board) and col+2 < len(self.matrix.Board[row])):
            self.matrix.Board[row+1][col+2].Xed += 1
        if (row+1 < len(self.matrix.Board) and col-2 >= 0):
            self.matrix.Board[row+1][col-2].Xed += 1
        if (row-1 >= 0 and col-2 >= 0):
            self.matrix.Board[row-1][col-2].Xed += 1
        if (row-1 >= 0 and col+2 < len(self.matrix.Board[row])):
            self.matrix.Board[row-1][col+2].Xed += 1

    def deXIfyVert (self, row, col):
        for i in range(len(self.matrix.Board)):
            if (i != row):
                self.matrix.Board[i][col].Xed -= 1

    def deXIfyHorz (self, row, col):
        for i in range(len(self.matrix.Board[row])):
            if (i != col):
                self.matrix.Board[row][i].Xed -= 1

    def deXIfyDiagDownRight (self, row, col):
        i = row
        j = col
        while (i > 0 and j > 0):
            i -= 1
            j -= 1
        while (i < len(self.matrix.Board) and j < len(self.matrix.Board[i])):
            if (i != row and j != col):
                self.matrix.Board[i][j].Xed -= 1
            i += 1
            j += 1
        
    def deXIfyDiagDownLeft(self, row, col):
        i = row
        j = col
        while (i > 0 and j < len(self.matrix.Board[i])-1):
            i -= 1
            j += 1
        while (i < len(self.matrix.Board) and j > 0):
            if (i != row and j != col):
                self.matrix.Board[i][j].Xed -= 1
            i += 1
            j -= 1

    def deXIfyL(self, row, col):
        if (row+2 < len(self.matrix.Board) and col+1 < len(self.matrix.Board[row])):
            self.matrix.Board[row+2][col+1].Xed -= 1
        if (row+2 < len(self.matrix.Board) and col-1 >= 0):
            self.matrix.Board[row+2][col-1].Xed -= 1
        if (row-2 >= 0 and col-1 >= 0):
            self.matrix.Board[row-2][col-1].Xed -= 1
        if (row-2 >= 0 and col+1 < len(self.matrix.Board[row])):
            self.matrix.Board[row-2][col+1].Xed -= 1
        if (row+1 < len(self.matrix.Board) and col+2 < len(self.matrix.Board[row])):
            self.matrix.Board[row+1][col+2].Xed -= 1
        if (row+1 < len(self.matrix.Board) and col-2 >= 0):
            self.matrix.Board[row+1][col-2].Xed -= 1
        if (row-1 >= 0 and col-2 >= 0):
            self.matrix.Board[row-1][col-2].Xed -= 1
        if (row-1 >= 0 and col+2 < len(self.matrix.Board[row])):
            self.matrix.Board[row-1][col+2].Xed -= 1

    def deXIfySingleDiag(self,row,col):
        if (row+1 < len(self.matrix.Board) and col+1 < len(self.matrix.Board[row])):
            self.matrix.Board[row+1][col+1].Xed -= 1
        if (row+1 < len(self.matrix.Board) and col-1 >= 0):
            self.matrix.Board[row+1][col-1].Xed -= 1
        if (row-1 >= 0 and col-1 >= 0):
            self.matrix.Board[row-1][col-1].Xed -= 1
        if (row-1 >= 0 and col+1 < len(self.matrix.Board[row])):
            self.matrix.Board[row-1][col+1].Xed -= 1

    def solveQueenRegular(self, counter, prevSerial, serialSolutions):
        print(counter, prevSerial, serialSolutions)
        if (len(serialSolutions) == len(self.colorController.uniqueList)):
            self.solutions = serialSolutions
            return
        if (prevSerial != ""):
            if (self.colorController.colorAssigned[prevSerial].Xed > 0):
                return
        for i in range(self.colorController.colorAssigned[self.colorController.uniqueList[counter]+"_Length"]):
            rowe = self.colorController.colorAssigned[self.colorController.uniqueList[counter]+""+f"{i}"].Row
            cole = self.colorController.colorAssigned[self.colorController.uniqueList[counter]+""+f"{i}"].Col
            if (self.colorController.colorAssigned[self.colorController.uniqueList[counter]+""+f"{i}"].Xed <= 0):
                self.xIfyVert(rowe,cole)
                self.xIfyHorz(rowe,cole)
                self.xIfySingleDiag(rowe,cole)
                serialSolutions.append(self.colorController.uniqueList[counter]+""+f"{i}")
                self.solveQueenRegular(counter+1,self.colorController.uniqueList[counter]+""+f"{i}",serialSolutions)
                self.deXIfyVert(rowe,cole)
                self.deXIfyHorz(rowe,cole)
                self.deXIfySingleDiag(rowe,cole)
                if (len(serialSolutions) == len(self.colorController.uniqueList)):
                    self.solutions = serialSolutions
                    return
                serialSolutions.remove(serialSolutions[-1])

    def solveQueenChess(self, counter, prevSerial, serialSolutions):
        print(counter, prevSerial, serialSolutions)
        if (len(serialSolutions) == len(self.colorController.uniqueList)):
            self.solutions = serialSolutions
            return
        if (prevSerial != ""):
            if (self.colorController.colorAssigned[prevSerial].Xed > 0):
                return
        for i in range(self.colorController.colorAssigned[self.colorController.uniqueList[counter]+"_Length"]):
            rowe = self.colorController.colorAssigned[self.colorController.uniqueList[counter]+""+f"{i}"].Row
            cole = self.colorController.colorAssigned[self.colorController.uniqueList[counter]+""+f"{i}"].Col
            if (self.colorController.colorAssigned[self.colorController.uniqueList[counter]+""+f"{i}"].Xed <= 0):
                self.xIfyVert(rowe,cole)
                self.xIfyHorz(rowe,cole)
                self.xIfyDiagDownRight(rowe,cole)
                self.xIfyDiagDownLeft(rowe,cole)
                serialSolutions.append(self.colorController.uniqueList[counter]+""+f"{i}")
                self.solveQueenChess(counter+1,self.colorController.uniqueList[counter]+""+f"{i}",serialSolutions)
                self.deXIfyVert(rowe,cole)
                self.deXIfyHorz(rowe,cole)
                self.deXIfyDiagDownRight(rowe,cole)
                self.deXIfyDiagDownLeft(rowe,cole)
                if (len(serialSolutions) == len(self.colorController.uniqueList)):
                    self.solutions = serialSolutions
                    return
                serialSolutions.remove(serialSolutions[-1])

    def solveRook(self, counter, prevSerial, serialSolutions):
        print(counter, prevSerial, serialSolutions)
        if (len(serialSolutions) == len(self.colorController.uniqueList)):
            self.solutions = serialSolutions
            return
        if (prevSerial != ""):
            if (self.colorController.colorAssigned[prevSerial].Xed > 0):
                return
        for i in range(self.colorController.colorAssigned[self.colorController.uniqueList[counter]+"_Length"]):
            rowe = self.colorController.colorAssigned[self.colorController.uniqueList[counter]+""+f"{i}"].Row
            cole = self.colorController.colorAssigned[self.colorController.uniqueList[counter]+""+f"{i}"].Col
            if (self.colorController.colorAssigned[self.colorController.uniqueList[counter]+""+f"{i}"].Xed <= 0):
                self.xIfyVert(rowe,cole)
                self.xIfyHorz(rowe,cole)
                serialSolutions.append(self.colorController.uniqueList[counter]+""+f"{i}")
                self.solveRook(counter+1,self.colorController.uniqueList[counter]+""+f"{i}",serialSolutions)
                self.deXIfyVert(rowe,cole)
                self.deXIfyHorz(rowe,cole)
                if (len(serialSolutions) == len(self.colorController.uniqueList)):
                    self.solutions = serialSolutions
                    return
                serialSolutions.remove(serialSolutions[-1])

    def solveBishop(self, counter, prevSerial, serialSolutions):
        print(counter, prevSerial, serialSolutions)
        if (len(serialSolutions) == len(self.colorController.uniqueList)):
            self.solutions = serialSolutions
            return
        if (prevSerial != ""):
            if (self.colorController.colorAssigned[prevSerial].Xed > 0):
                return
        for i in range(self.colorController.colorAssigned[self.colorController.uniqueList[counter]+"_Length"]):
            rowe = self.colorController.colorAssigned[self.colorController.uniqueList[counter]+""+f"{i}"].Row
            cole = self.colorController.colorAssigned[self.colorController.uniqueList[counter]+""+f"{i}"].Col
            if (self.colorController.colorAssigned[self.colorController.uniqueList[counter]+""+f"{i}"].Xed <= 0):
                self.xIfyDiagDownRight(rowe,cole)
                self.xIfyDiagDownLeft(rowe,cole)
                serialSolutions.append(self.colorController.uniqueList[counter]+""+f"{i}")
                self.solveBishop(counter+1,self.colorController.uniqueList[counter]+""+f"{i}",serialSolutions)
                self.deXIfyDiagDownRight(rowe,cole)
                self.deXIfyDiagDownLeft(rowe,cole)
                if (len(serialSolutions) == len(self.colorController.uniqueList)):
                    self.solutions = serialSolutions
                    return
                serialSolutions.remove(serialSolutions[-1])

    def solveKnight(self, counter, prevSerial, serialSolutions):
        print(counter, prevSerial, serialSolutions)
        if (len(serialSolutions) == len(self.colorController.uniqueList)):
            self.solutions = serialSolutions
            return
        if (prevSerial != ""):
            if (self.colorController.colorAssigned[prevSerial].Xed > 0):
                return
        for i in range(self.colorController.colorAssigned[self.colorController.uniqueList[counter]+"_Length"]):
            rowe = self.colorController.colorAssigned[self.colorController.uniqueList[counter]+""+f"{i}"].Row
            cole = self.colorController.colorAssigned[self.colorController.uniqueList[counter]+""+f"{i}"].Col
            if (self.colorController.colorAssigned[self.colorController.uniqueList[counter]+""+f"{i}"].Xed <= 0):
                self.xIfyL(rowe,cole)
                serialSolutions.append(self.colorController.uniqueList[counter]+""+f"{i}")
                self.solveKnight(counter+1,self.colorController.uniqueList[counter]+""+f"{i}",serialSolutions)
                self.deXIfyL(rowe,cole)
                if (len(serialSolutions) == len(self.colorController.uniqueList)):
                    self.solutions = serialSolutions
                    return
                serialSolutions.remove(serialSolutions[-1])

    def solve(self):
        if (self.chessPiece == "Queen (Default)"):
            self.solveQueenRegular(0,"",[])
        elif (self.chessPiece == "Queen Chess Version"):
            self.solveQueenChess(0,"",[])
        elif (self.chessPiece == "Rook"):
            self.solveRook(0,"",[])
        elif (self.chessPiece == "Bishop"):
            self.solveBishop(0,"",[])
        elif (self.chessPiece == "Knight"):
            self.solveKnight(0,"",[])