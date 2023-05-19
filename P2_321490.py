# MATTEO GIANVENUTI
from boardgame import BoardGame

class _3inarow(BoardGame):
    def __init__(self, dim):
        self._righe, self._colonne = dim
        self._matrix = []
        self._file = None
        if self._righe == 0:
            self._file = "testmatrix.py"
            self._righe, self._colonne = 6, 6
        elif self._righe == 6: self._file = "matrix6.py"
        elif self._righe == 8: self._file = "matrix8.py"
        elif self._righe == 10: self._file = "matrix10.py"
        elif self._righe == 12: self._file = "matrix12.py"
        elif self._righe == 14: self._file = "matrix14.py"
        elif self._righe == 18: self._file = "matrix18.py"
        with open(self._file) as f:
            for line in f:
                l = line.split(",")
                for v in l:
                    if v[-1] == "\n":
                        self._matrix.append(str(v[-2]))
                    else:
                        self._matrix.append(str(v))
        self._solved = False
        self._ripetizioni = True
           
    def cols(self) -> int:
        return self._colonne
       
    def rows(self) -> int:
        return self._righe
           
    def value_at(self, x: int, y: int):
        m, w, h = self._matrix, self._righe, self._colonne
        if 0 <= y < w and 0 <= x < h:
            return str(m[y * h + x])
        return str(m[y * h + x])
       
    def play_at(self, x: int, y: int):
        w, h = self._righe, self._colonne
        if 0 <= y < w and 0 <= x < h:
            m, i = self._matrix, y * h + x
            if m[i] == "-":
                m[i] = "W"
            elif m[i] == "W":
                m[i] = "B"
            elif m[i] == "B":
                m[i] = "-"
            
    def reset(self):
        self._matrix = []
        with open(self._file) as f:
            for line in f:
                l = line.split(",")
                for v in l:
                    if v[-1] == "\n":
                        self._matrix.append(str(v[-2]))
                    else:
                        self._matrix.append(str(v))
        return self._matrix
    
    def solve_recursive(self, i: int) -> bool:
        self.automatic_color() 
        if self.unsolvable(): return False  
        while i < len(self._matrix) and self._matrix[i] != "-":
            i += 1
        if i < len(self._matrix):
            saved = self._matrix[:] 
            for color in ("B", "W"):
                self._matrix[i] = color
                if self.solve_recursive(i + 1):
                    return True
                self._matrix = saved  
        return self.finished()
    
    def suggerimenti(self) -> bool:
        c = self._matrix
        
        for i in range(len(c)):
            if c[i] == "-":
                c[i] = "B"
                if self.unsolvable():
                    c[i] = "W"
                    return True
                c[i] = "W"
                if self.unsolvable():
                    c[i] = "B"
                    return True
                c[i] = "-"
        return False
    
    def automatic_color(self):
        copy = self._matrix
        m, rig, cln = copy, self._righe, self._colonne
        nero_row, bianco_row, c_bianco_row, c_nero_row = 0, 0, [], []
        nero_col, bianco_col, c_bianco_col, c_nero_col = 0, 0, [], []
        trip_w_row, trip_b_row, trip_w_col, trip_b_col = [], [], [], []
        bianco_final, nero_final = [], []
        pos_w, pos_b = [], []
        for a in range(0,rig): 
            for b in range(0,cln):
                if (m[a * cln + b] == "w"): #row
                    m[a * cln + b] = "W"
                    pos_w.append(a * cln + b)
                elif (m[a * cln + b] == "b"):
                    m[a * cln + b] = "B"
                    pos_b.append(a * cln + b)
                if (m[b * cln + a] == "w"): #col
                    m[b * cln + a] = "W"
                    pos_w.append(b * cln + a)
                elif (m[b * cln + a] == "b"):
                    m[b * cln + a] = "B"
                    pos_b.append(b * cln + a)
                #controllo righe   
                if (m[a * cln + b] == "W"):
                    bianco_row += 1
                elif (m[a * cln + b] == "-"):
                    c_bianco_row.append(a * cln + b)
                #controllo colonne
                if (m[b * cln + a] == "W"):
                    bianco_col += 1
                elif (m[b * cln + a] == "-"):
                    c_bianco_col.append(b * cln + a)
                #controllo righe
                if (m[a * cln + b] == "B"):
                    nero_row += 1
                elif (m[a * cln + b] == "-"):
                    c_nero_row.append(a * cln + b)
                #controllo colonne
                if (m[b * cln + a] == "B"):
                    nero_col += 1
                elif (m[b * cln + a] == "-"):
                    c_nero_col.append(b * cln + a)
                #verificare se le celle da colorare sono nella stessa riga/colonna
                if (a*rig+b)//cln == (a*rig+b-1)//cln == (a*rig+b-2)//cln:
                    #controllo righe #caso w w - || b b -
                    if (m[a * cln + (b-1)] == m[a * cln + (b-2)] == "W"):
                        if m[a * cln + b] == "-": trip_w_row.append(a * cln + b)
                    elif (m[a * cln + (b-1)] == m[a * cln + (b-2)] == "B"):
                        if m[a * cln + b] == "-": trip_b_row.append(a * cln + b)
                    #controllo colonne #caso w w - || b b -
                    if (m[(b-1) * cln + a] == m[(b-2) * cln + a] == "W"):
                        if m[b * cln + a] == "-": trip_w_col.append(b * cln + a) 
                    elif (m[(b-1) * cln + a] == m[(b-2) * cln + a] == "B"):
                        if m[b * cln + a] == "-": trip_b_col.append(b * cln + a)
                    #controllo righe #caso - b b || - w w
                    if (m[a * cln + b] == m[a * cln + (b-1)] == "W"):
                        if m[a * cln + (b-2)] == "-": trip_w_row.append(a * cln + (b-2)) 
                    elif (m[a * cln + b] == m[a * cln + (b-1)] == "B"):
                        if m[a * cln + (b-2)] == "-": trip_b_row.append(a * cln + (b-2))
                    # controllo colonne #caso - w w || - b b
                    if (m[b * cln + a] == m[(b-1) * cln + a] == "W"):
                        if m[(b-2) * cln + a] == "-": trip_w_col.append((b-2) * cln + a) 
                    elif (m[b * cln + a] == m[(b-1) * cln + a] == "B"):
                        if m[(b-2) * cln + a] == "-": trip_b_col.append((b-2) * cln + a)
                    # controllo righe # caso w - w || b - b
                    if (m[a * cln + b] == m[a * cln + (b-2)] == "W"):
                        if m[a * cln + (b-1)] == "-": trip_w_row.append(a * cln + (b-1)) 
                    elif (m[a * cln + b] == m[a * cln + (b-2)] == "B"):
                        if m[a * cln + (b-1)] == "-": trip_b_row.append(a * cln + (b-1))
                    #controllo colonne # caso w - w || b - b
                    if (m[b * cln + a] == m[(b-2) * cln + a] == "W"):
                        if m[(b-1) * cln + a] == "-": trip_w_col.append((b-1) * cln + a) 
                    elif (m[b * cln + a] == m[(b-2) * cln + a] == "B"):
                        if m[(b-1) * cln + a] == "-": trip_b_col.append((b-1) * cln + a)
            #controllo righe
            if bianco_row == rig/2:
                for G in c_bianco_row:
                    bianco_final.append(G)
            if nero_row == rig/2: 
                for B in c_nero_row:
                    nero_final.append(B)
            bianco_row, nero_row = 0, 0
            c_bianco_row, c_nero_row = [], []
            #controllo colonne
            if bianco_col == cln/2:
                for Q in c_bianco_col:
                    bianco_final.append(Q)
            if nero_col == cln/2:
                for K in c_nero_col:
                    nero_final.append(K)
            bianco_col, nero_col = 0, 0
            c_bianco_col, c_nero_col = [], []
        #colorazione casi 
        for X in trip_w_row:
            if m[X] == "-":
                m[X] = "B"
        for Y in trip_b_row:
            if m[Y] == "-":
                m[Y] = "W"
        for F in trip_w_col:
            if m[F] == "-":
                m[F] = "B"
        for P in trip_b_col:
            if m[P] == "-":
                m[P] = "W"
        trip_w_row, trip_b_row = [], []
        trip_w_col, trip_b_col = [], []
        #colorazione colonne/righe intere
        for BF in bianco_final:
            m[BF] = "B"
        for NF in nero_final:
            m[NF] = "W"
        bianco_final, nero_final = [], []
        for pw in pos_w:
            if m[pw] == "W":
                m[pw] = "w"
        for pb in pos_b:
            if m[pb] == "B":
                m[pb] = "b"
        self._matrix = copy
        return self._matrix
    
    def unsolvable(self) -> bool:
        copia = self._matrix
        m, rig, cln = copia, self._righe, self._colonne
        bianco_row, nero_row, row = 0, 0, 0
        bianco_col, nero_col, col = 0, 0, 0
        for a in range(rig): 
            for b in range(cln):
                # conversione righe
                if (m[a * cln + b] == "w"): 
                    m[a * cln + b] = "W"
                elif (m[a * cln + b] == "b"):
                    m[a * cln + b] = "B"
                # conversione colonne
                if (m[b * cln + a] == "w"): 
                    m[b * cln + a] = "W"
                elif (m[b * cln + a] == "b"):
                    m[b * cln + a] = "B"
                #conteggio valori righe
                if (m[a * cln + b] == "W"): 
                    bianco_row += 1
                elif (m[a * cln + b] == "B"):
                    nero_row += 1
                #conteggio valori colonne
                if (m[b * cln + a] == "W"): 
                    bianco_col += 1
                elif (m[b * cln + a] == "B"):
                    nero_col += 1
                #tre valori righe
                val_r = m[a * cln + b]
                val1_r = m[a * cln + (b-1)]
                val2_r = m[a * cln + (b-2)]
                #tre valori colonne
                val_c = m[b * cln + a]
                val1_c = m[(b-1) * cln + a]
                val2_c = m[(b-2) * cln + a]
            if val_r == val1_r == val2_r == "W":
                return True # true = non solvable
            elif val_r == val1_r == val2_r == "B":
                return True
            if val_c == val1_c == val2_c == "W":
                return True
            elif val_c == val1_c == val2_c == "B":
                return True 
            if bianco_row == rig/2 and nero_row == rig/2: #riga
                row += 1
            if bianco_col == cln/2 and nero_col == cln/2: #colonna
                col += 1
            nero_row, bianco_row, nero_col, bianco_col = 0, 0, 0, 0
        if "-" not in m:
            if (row < rig) or (col < cln):
                return True # true = non solvable
        return False # false  = non ci sono errori evidenti 
    
    def flag_at(self, x: int, y: int):
        pass
   
    def message(self) -> (str):
        return "Game won!"
    
    def finished(self) -> bool:
        copia = self._matrix
        bianco_row, nero_row, row = 0, 0, 0
        bianco_col, nero_col, col = 0, 0, 0
        m, cln, rig = copia, self._colonne, self._righe
        if "-" in m:
            return False
        for a in range(rig):
            for b in range(cln):
                # conversione righe
                if (m[a * cln + b] == "w"): 
                    m[a * cln + b] = "W"
                elif (m[a * cln + b] == "b"):
                    m[a * cln + b] = "B"
                # conversione colonne
                if (m[b * cln + a] == "w"): 
                    m[b * cln + a] = "W"
                elif (m[b * cln + a] == "b"):
                    m[b * cln + a] = "B"
                #conteggio valori righe
                if (m[a * cln + b] == "W"): 
                    bianco_row += 1
                elif (m[a * cln + b] == "B"):
                    nero_row += 1
                #conteggio valori colonne
                if (m[b * cln + a] == "W"): 
                    bianco_col += 1
                elif (m[b * cln + a] == "B"):
                    nero_col += 1
                #tre valori righe
                val_r = m[a * cln + b]
                val1_r = m[a * cln + (b-1)]
                val2_r = m[a * cln + (b-2)]
                #tre valori colonne
                val_c = m[b * cln + a]
                val1_c = m[(b-1) * cln + a]
                val2_c = m[(b-2) * cln + a]
            if val_r == val1_r == val2_r == "W":
                return False
            elif val_r == val1_r == val2_r == "B":
                return False
            if val_c == val1_c == val2_c == "W":
                return False
            elif val_c == val1_c == val2_c == "B":
                return False
            if bianco_row == rig/2 and nero_row == rig/2: #righe
                nero_row, bianco_row = 0, 0
                row += 1
            if bianco_col == cln/2 and nero_col == cln/2: #colonne
                nero_col, bianco_col = 0, 0
                col += 1
        if row == rig and col == cln:
            self._solved = True
        return self._solved 
   

