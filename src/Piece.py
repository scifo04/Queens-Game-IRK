class Piece:
    Row: int
    Col: int
    Occupier: str
    Xed: int

    def __init__ (self, Row, Col):
        self.Row = Row
        self.Col = Col
        self.Occupier = "None"
        self.Xed = 0