from tictactoe import player,actions,winner,terminal,result,utility,minimax

E = None
X = 'X'
O = 'O'

a = [[X,X, X],
     [X,O, O],
     [E,E, O]]


print(player(a))
print(terminal(a))

print(minimax(a))
