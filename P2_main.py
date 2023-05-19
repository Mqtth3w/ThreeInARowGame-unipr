from gui3inarow import gui_play
from P2_321490 import _3inarow

def main():
    level = [0,6,8,10,12,14,18]
    try:
        dim = int(input("Dimensione del puzzle: 6, 8, 10, 12, 14, 18? "))
    except ValueError:
        print("\n","Ouch! Ritenta sarai più fortunato")
        dim = int(input("Dimensione del puzzle: 6, 8, 10, 12, 14, 18? "))
        
    if dim not in level:
        raise NotImplementedError("Livello non presente!")
    game = _3inarow((dim,dim))
    gui_play(game)
main()