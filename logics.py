import random
def startgame():
    mat = [[0 for i in range(4)] for j in range(4)]
    return mat

def add_new_2(mat):
    a = random.randint(0, len(mat)-1)
    b = random.randint(0, len(mat)-1)
    while mat[a][b] != 0:
        a = random.randint(0, len(mat)-1)
        b = random.randint(0, len(mat)-1)
    mat[a][b] = 2
    return mat

def get_current_state(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 2048:
                return 'win'
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return 'not over'

    for i in range(len(mat)-1):
        for j in range(len(mat[0])-1):
            if mat[i][j] == mat[i+1][j] or mat[i][j+1] == mat[i][j]:
                return 'not over'
    for k in range(len(mat)-1):  
        if mat[len(mat)-1][k] == mat[len(mat)-1][k+1]:
            return 'not over'
    for j in range(len(mat)-1): 
        if mat[j][len(mat)-1] == mat[j+1][len(mat)-1]:
            return 'not over'
    return 'lose'


def remove_blanks(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([0] * 4)
    done=False
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                pos = pos + 1
                done=True
    return new_mat,done

def merge_same(mat,done):
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1]:
                mat[i][j] = (mat[i][j]) * 2
                mat[i][j + 1] = 0
                done=True
    return mat,done

def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append(mat[i][::-1])
    return new_mat

def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

def move_up(grid):
    transposed_grid = transpose(grid)
    new_grid,done = remove_blanks(transposed_grid)
    new_grid,done = merge_same(new_grid,done)
    new_grid = remove_blanks(new_grid)[0]
    final_grid = transpose(new_grid)
    return final_grid,done

def move_down(grid):
    transposed_grid = transpose(grid)
    reverse_grid = reverse(transposed_grid)
    new_grid,done = remove_blanks(reverse_grid)
    new_grid,done = merge_same(new_grid,done)
    new_grid = remove_blanks(new_grid)[0]
    new_reverse = reverse(new_grid)
    final_grid = transpose(new_reverse)
    return final_grid,done

def move_right(grid):
    reverse_grid = reverse(grid)
    new_grid,done = remove_blanks(reverse_grid)
    new_grid,done = merge_same(new_grid,done)
    new_grid = remove_blanks(new_grid)[0]
    final_grid = reverse(new_grid)
    return final_grid,done

def move_left(grid):
    new_grid,done = remove_blanks(grid)
    new_grid,done = merge_same(new_grid,done)
    new_grid = remove_blanks(new_grid)[0]
    return new_grid,done

