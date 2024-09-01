n=int(input())
board=[0]*n
cnt=0

def possible(row,col):
    for i in range(row):
        if board[i]==col or abs(board[i]-col)==abs(i-row):
            return False
    return True

def place(row):
    global cnt
    if row==n:
        cnt+=1
        return

    for col in range(n):
        if possible(row,col):
            board[row]=col
            place(row+1)

place(0)
print(cnt)