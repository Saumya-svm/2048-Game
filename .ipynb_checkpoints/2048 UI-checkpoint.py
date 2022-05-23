from tkinter import Frame,CENTER,Label

import constants as c
import logics

# inherit frame
class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>",self.key_down)
        self.commands = {c.KEY_DOWN:logics.move_down,c.KEY_UP:logics.move_up,c.KEY_LEFT:logics.move_left,c.KEY_RIGHT:logics.move_right}

        self.grid_cells = []
        self.init_grid()
        self.init_matrix()        
        self.update_grid_cells()
        
        self.mainloop()

    def init_grid(self):
        background = Frame(self,bg = c.BACKGROUND_COLOR_GAME,width=c.size,height=c.size)
        background.grid()

        for i in range(c.grid_len):
            grid_row = []
            for j in range(c.grid_len):
                cell = Frame(background,bg = c.BACKGROUND_COLOR_CELL,
                width=c.size/c.grid_len,height=c.size/c.grid_len)

                cell.grid(row=i,column=j,padx=c.grid_padding,pady=c.grid_padding)

                t = Label(master=cell,bg=c.BACKGROUND_COLOR_CELL,justify=CENTER,font=c.FONT,width=5,height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix = logics.startgame()
        logics.add_new_2(self.matrix)
        logics.add_new_2(self.matrix)

    def update_grid_cells(self):
        for i in range(c.grid_len):
            for j in range(c.grid_len):
                num = int(self.matrix[i][j])
                if num==0:
                    self.grid_cells[i][j].configure(text = '',bg ='blue')
                else:
                    self.grid_cells[i][j].configure(text = str(num),bg = c.BACKGROUND_COLOR_DICT[num],fg = c.CELL_COLOR_DICT[num])
        self.update_idletasks()
    
    def key_down(self,event):
        key = repr(event.char)
        if key in self.commands:
            self.matrix,changed = self.commands[repr(event.char)](self.matrix)
            if changed:
                logics.add_new_2(self.matrix)
                self.update_grid_cells()
                changed = False
                if logics.get_current_state(self.matrix) == 'win':
                    self.grid_cells[1][1].configure(text = 'You')
                    self.grid_cells[1][2].configure(text = 'Win!!')
                if logics.get_current_state(self.matrix) == 'lose':
                    self.grid_cells[1][1].configure(text = 'You')
                    self.grid_cells[1][2].configure(text = 'Lose!!')

g = Game2048()