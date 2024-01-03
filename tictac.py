def sum(a,b,c):
    return a+b+c
def print_board(xsatte,zstate):
    zero = "x" if xsatte[0] else ("0" if zstate[0] else 0)
    one = "x" if xsatte[1] else ("0" if zstate[1] else 1)
    two = "x" if xsatte[2] else ("0" if zstate[2] else 2)
    three = "x" if xsatte[3] else ("0" if zstate[3] else 3)
    four = "x" if xsatte[4] else ("0" if zstate[4] else 4)
    five = "x" if xsatte[5] else ("0" if zstate[5] else 5)
    six = "x" if xsatte[6] else ("0" if zstate[6] else 6)
    seven = "x" if xsatte[7] else ("0" if zstate[7] else 7)
    eight = "x" if xsatte[8] else ("0" if zstate[8] else 8)
#
    print(f"{zero} | {one} |{two}")
    print("--|---|--")
    print(f"{three}| {four} | {five}")
    print("--|---|--")
    print(f"{six} | {seven} | {eight}")

def win(xstate,zstate):
    wins =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if (sum(xstate[win[0]],xstate[win[1]],xstate[win[2]]) == 3):
            print("x won the match")
            return 1
        if (sum(zstate[win[0]], zstate[win[1]], zstate[win[2]]) == 3):
            print("0 won the match")
            return 0
    return -1




if __name__ == "__main__":
    xstate = [0, 0, 0, 0, 0, 0, 0, 0,0]
    zstate = [0, 0, 0, 0, 0, 0, 0, 0,0]
    turn = 1
    print("Welcome to Tic Tac Toe")
    while True:
        print_board(xstate,zstate)
        if turn == 1:
            print("X's chance")
            value = int(input("enter the value"))
            xstate[value] =1
        else:
            print("0's chance")
            value = int(input("enter the value"))
            zstate[value] = 1
        cwin=win(xstate,zstate)
        if cwin!=-1:
            break

        turn = 1 - turn

        #print_board()
        #break