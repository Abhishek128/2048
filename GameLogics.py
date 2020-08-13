import random
def start_game():
    mat=[]
    for i in range(4):
        mat.append([0]*4)
    return mat

# def add_new_2(mat):
    
#     r= random.randint(0,3)
#     c=random.randint(0,3)
#     while mat[r][c] != 0:
#         r= random.randint(0,3)
#         c=random.randint(0,3)
#     mat[r][c] = 2
def addNew(mat):
    option = []
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0 :
                option.append((i,j))
    if len(option) != 0 :
        x,y = random.choice(option)

        l = [2,4]
        num = random.choice(l)
        mat[x][y] = num
        print(mat) 
def reverse(mat):
    new_mat=[]
    for  i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3-j])
    return new_mat
def transpose(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat
def compress(mat):
    c=False
    new_mat=[]
    for i in range(4):
        new_mat.append([0]*4)
    for k in range(4):
        pos=0
        for j in range(4):
            if (mat[k][j])!=(int('0')):
                new_mat[k][pos] = mat[k][j]
                pos=pos+1
                if pos!=j:
                    c=True
    return new_mat,c
def merge(mat):
    c=False
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                mat[i][j]=2*mat[i][j]
                mat[i][j+1]=0
                c=True
    return mat,c
    
def move_up(grid):
    trans_grid=transpose(grid)
    new_grid,c1=compress(trans_grid)
    new_grid,c2=merge(new_grid)
    c=c1 or c2
    new_grid,c3=compress(new_grid)
    new_grid=transpose(new_grid)
    return new_grid,c
def move_down(grid):
    trans_grid=transpose(grid)
    rev_grid=reverse(trans_grid)
    new_grid,c1=compress(rev_grid)
    new_grid,c2=merge(new_grid)
    c=c1 or c2
    new_grid,c3=compress(new_grid)
    new_grid=reverse(new_grid)
    new_grid=transpose(new_grid)
    return new_grid,c
    
def move_right(grid):
    rev_grid=reverse(grid)
    new_grid,c1=compress(rev_grid)
    new_grid,c2=merge(new_grid)
    c = c1 or c2
    new_grid,c3=compress(new_grid)
    new_grid=reverse(new_grid)
    return new_grid,c
def move_left(grid):
    new_grid,c1=compress(grid)
    new_grid,c2=merge(new_grid)
    c = c1 or c2
    new_grid,c3=compress(new_grid)
    return new_grid,c
def isInside(x,y):
    return  x >= 0 and x < 4 and y >= 0 and y < 4 
def get_current_state(mat):
# def currentState(mat) :
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048 :
                return 'WON'
    direct = [[-1,0],[1,0],[0,-1],[0,1]]
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0 :
                return 'Game Not Over'
    for i in range(4) :
        for j in range(4):
            for xi,yi in direct :
                x = i + xi 
                y = yi + j
                if isInside(x,y) and mat[x][y] == mat[i][j] :
                    return 'Game Not Over'
    return 'Lost' 
        
