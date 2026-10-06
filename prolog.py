batsman(sachin).
batsman(virat).
batsman(dhoni).

cricketer(X):- batsman(X).
sportsman(X):- cricketer(X).
famousperson(X):- sportsman(X).

query:
cricketer(virat).
famousperson(X). then ;

