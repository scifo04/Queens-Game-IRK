import tkinter as tk
from tkinter import ttk
import os
from tkinter import filedialog
from tkinter import messagebox
from ColorAssigner import ColorAssigner
from Solver import Solver
from PIL import Image, ImageTk
from tkinter import PhotoImage

class MainPage:
    root: tk.Tk
    txt_frm: ttk.LabelFrame
    setup_frm: ttk.LabelFrame
    cnv_frm: ttk.LabelFrame
    size_frm: ttk.LabelFrame
    file_name: str
    file_path: str
    txt_label: ttk.Label
    upload_button: ttk.Button
    board: list[str]
    row: int
    col: int
    colors: int
    assign: ColorAssigner
    choice: ttk.Combobox
    solve: ttk.Button
    canvas: tk.Canvas
    stringvar: tk.StringVar
    solution: Solver
    pointSolution: list
    height: ttk.Spinbox
    width: ttk.Spinbox
    resize: ttk.Button
    bg_label: ttk.Label
    bg_image: PhotoImage

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Queens")
        self.root.geometry("800x600")  # Adjusted for better layout
        self.root.state("zoomed")
        self.file_name = "File: "
        self.board = []
        self.pointSolution = []
        
        # Configure the grid layout for the root window
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)

        self.construct_txt_frm()
        self.construct_set_frm()
        self.construct_cnv_frm()
        self.construct_size_frm()
        self.create_background()
        self.construct_canvas()
        self.construct_chosen_file()
        self.construct_upload_button()
        self.construct_piece_choice()
        self.construct_solve_button()
        self.construct_size_spinbox()
        self.root.mainloop()

    def create_background(self):
        self.bg_image = PhotoImage(file='../asset/bgCheck.png')
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(relheight=1,relwidth=1)
        self.bg_label.lower()

    def construct_txt_frm(self):
        self.txt_frm = ttk.LabelFrame(self.root, padding=10, text="Upload TXT Here")
        self.txt_frm.grid(row=0, column=0, padx=10, pady=20, ipadx=10, ipady=10, sticky="nsew")

    def construct_cnv_frm(self):
        self.cnv_frm = ttk.LabelFrame(self.root, padding=10, text="Board")
        self.cnv_frm.grid(row=0, column=1, rowspan=3, padx=20, pady=20, ipadx=10, ipady=10, sticky="nsew")
        self.root.grid_columnconfigure(1, weight=2)

    def construct_set_frm(self):
        self.setup_frm = ttk.LabelFrame(self.root, padding=10, text="Setup")
        self.setup_frm.grid(row=1, column=0, padx=10, pady=20, ipady=10, sticky="nsew")

    def construct_size_frm(self):
        self.size_frm = ttk.LabelFrame(self.root, padding=10, text="Size")
        self.size_frm.grid(row=2, column=0, padx=10, pady=20, ipady=10, sticky="nsew")

    def construct_upload_button(self):
        self.upload_button = tk.Button(self.txt_frm, text="Choose File", command=self.process_file)
        self.upload_button.grid(row=0, column=0, pady=20)

    def construct_chosen_file(self):
        self.txt_label = ttk.Label(self.txt_frm, text=self.file_name)
        self.txt_label.grid(row=0, column=1, padx=10, pady=0)

    def construct_piece_choice(self):
        self.stringvar = tk.StringVar()
        self.choice = ttk.Combobox(self.setup_frm, width=20, textvariable=self.stringvar, state="readonly")
        self.choice.grid(row=0, column=0, pady=20, padx=20)
        self.choice["values"] = ["Queen (Default)", "Queen Chess Version", "Rook", "Bishop", "Knight"]

    def construct_solve_button(self):
        self.solve = tk.Button(self.setup_frm, text="Solve", command=self.solve_board)
        self.solve.grid(row=1, column=0, pady=20,padx=120)

    def construct_size_spinbox(self):
        self.height = tk.Spinbox(self.size_frm, from_=1, to=25, state="readonly")
        self.height.grid(row=0, column=0, padx=20, pady=20)
        self.width = tk.Spinbox(self.size_frm, from_=1, to=25, state="readonly")
        self.width.grid(row=0, column=2, padx=20, pady=20)
        self.resize = tk.Button(self.size_frm, text="Resize",state="disabled",command=self.resize_board)
        self.resize.grid(row=1,column=1,padx=20,pady=20)

    def construct_canvas(self):
        # Check if the board is populated
        if len(self.board) == 0 or len(self.board[0]) == 0:
            # Handle the case where the board is not ready to be displayed
            print("Board is empty, cannot create canvas")
            return

        # Clear the existing canvas if it exists
        if hasattr(self, 'canvas'):
            self.canvas.destroy()

        # Create a new canvas
        self.canvas = tk.Canvas(self.cnv_frm, height=len(self.board) * 50, width=len(self.board[0]) * 50)
        self.canvas.pack()

        # Draw the board
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                x1 = j * 50
                y1 = i * 50
                x2 = x1 + 50
                y2 = y1 + 50
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.assign.colorAssigned[self.board[i][j]], outline="black")

                # Draw text if needed
                points = [i, j]
                if points in self.pointSolution:
                    texte = self.get_piece_text()
                    self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=texte, fill="black")

    def get_piece_text(self):
        if self.solution.chessPiece == "Queen (Default)":
            return "QR"
        elif self.solution.chessPiece == "Queen Chess Version":
            return "QC"
        elif self.solution.chessPiece == "Rook":
            return "R"
        elif self.solution.chessPiece == "Bishop":
            return "B"
        elif self.solution.chessPiece == "Knight":
            return "K"
        return ""

    def process_file(self):
        filename = filedialog.askopenfilename(
            title="Choose a TXT file",
            filetypes=[("TXT files","*.txt")]
        )
        self.file_path = filename
        self.file_name = "File: " + os.path.basename(filename)
        self.construct_chosen_file()
        self.assign_to_board()
        self.resize.config(state="normal")
        print(self.file_path)
        print(self.file_name)

    def assign_to_board(self):
        f = open(self.file_path,"r",encoding="utf-8")
        container = []
        for i in f.readlines():
            texte = i.replace("\n","")
            tracker = list(map(str,texte.split()))
            container.append(tracker)
        self.row = int(container[0][0])
        self.col = int(container[0][1])
        self.colors = int(container[1][0])
        print(self.row,self.col,self.colors)
        if (len(container)-2 == self.row):
            for i in range(2,len(container)):
                if (len(container[i]) != self.col):
                    messagebox.showinfo("Warning","Incorrect array length")
                    return
            self.board = container[2:len(container)]
            self.assign = ColorAssigner(self.board)
            if (len(self.assign.uniqueList) != self.colors):
                messagebox.showinfo("Warning","Incorrect color amount")
                return
            self.construct_canvas()
        else:
            messagebox.showinfo("Warning","Incorrect array length")

    def solve_board(self):
        if (self.stringvar.get() is None or self.stringvar.get() == ""):
            messagebox.showinfo("Chess Piece Unselected","Please choose the chess piece")
            return
        else:
            self.solution = Solver(self.assign, self.stringvar.get())
            self.solution.solve()
            if (len(self.solution.solutions) > 0):
                self.pointSolution = []
                for i in range(len(self.solution.solutions)):
                    rowe = self.assign.colorAssigned[self.solution.solutions[i]].Row
                    cole = self.assign.colorAssigned[self.solution.solutions[i]].Col
                    points = [rowe,cole]
                    self.pointSolution.append(points)
                print(self.pointSolution)
                self.canvas.delete('all')
                self.construct_canvas()
            else:
                messagebox.showinfo("No solution found","No solution found in the board")

    def resize_board(self):
        newHeight = int(self.height.get())
        newWidth = int(self.width.get())
        if (newHeight <= len(self.board)):
            self.board = self.board[:newHeight]
        else:
            for i in range(newHeight-len(self.board)):
                self.board.append(self.board[-1])
        for i in range(len(self.board)):
            if (newWidth <= len(self.board[i])):
                self.board[i] = self.board[i][:newWidth]
            else:
                for j in range(newWidth-len(self.board[i])):
                    self.board[i].append(self.board[i][-1])
        self.assign = ColorAssigner(self.board)
        self.construct_canvas()