import tkinter as tk

def create_board(root, rows, cols, cell_size):
    canvas = tk.Canvas(root, width=cols * cell_size, height=rows * cell_size)
    canvas.pack()

    colors = ['#FF5733', '#33FF57', '#3357FF', '#FFFF33', '#FF33FF']  # Example colors

    for row in range(rows):
        for col in range(cols):
            color = colors[(row + col) % len(colors)]  # Cycle through colors
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
            
            # Adding text above each rectangle
            canvas.create_text((x1 + x2) // 2, y1 - 10, text=f"({row},{col})", fill="black")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Colored Board with Text")

    # Parameters
    rows = 5
    cols = 5
    cell_size = 50

    create_board(root, rows, cols, cell_size)
    root.mainloop()
