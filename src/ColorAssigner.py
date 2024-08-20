from BoardPiece import BoardPiece
from Piece import Piece

class ColorAssigner:
    colorCode: list[str]
    colorAssigned: dict
    matrix: list[list[str]]
    boardPiece: BoardPiece
    uniqueList: list[str]

    def __init__ (self, matrix: list[list[str]]):
        self.colorCode = ["#FF0000","#0000FF",
                          "#00FF00","#FFFF00",
                          "#FF00FF","#00FFFF",
                          "#FFFFFF","#808080",
                          "#FF8000","#FF0080"]
        self.boardPiece = BoardPiece()
        self.matrix = matrix
        self.uniqueList = self.getUnique()
        self.colorAssigned = {}
        temp_liste = []
        for i in range(len(self.uniqueList)):
            self.colorAssigned[self.uniqueList[i]] = self.colorCode[i]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if (self.matrix[i][j]+"_Length" in self.colorAssigned):
                    self.colorAssigned[self.matrix[i][j]+"_Length"] += 1
                else:
                    self.colorAssigned[self.matrix[i][j]+"_Length"] = 1
                temp_liste.append(Piece(i,j))
                self.colorAssigned[self.matrix[i][j]+str(self.colorAssigned[self.matrix[i][j]+"_Length"]-1)] = temp_liste[len(temp_liste)-1]
            self.boardPiece.Board.append(temp_liste)
            temp_liste = []

    def getUnique (self) -> list[str]:
        liste = []
        for matri in self.matrix:
            for elMatri in matri:
                liste.append(elMatri)
        liste = list(set(liste))
        return liste