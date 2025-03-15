class Vector():
    def __init__(self, *comps):
        self.len = len(comps)
        self.comps = comps
    
    def __add__(self, other):
        if type(self) == type(other):
            if self.len == other.len:
                return Vector(*(self.comps[i] + other.comps[i] for i in range(self.len)))
            else:
                return "Длины должны совпадать"
    
    def __sub__(self, other):
        if type(self) == type(other):
            if self.len == other.len:
                return Vector(*(self.comps[i] - other.comps[i] for i in range(self.len)))
            else:
                return "Длины должны совпадать"
            
    def __neg__(self):
        return Vector(*(-self.comps[i] for i in range(self.len)))
    
    def __str__(self):
        return '(' + ', '.join(map(str, self.comps)) + ')'
    
    def __mul__(self, other):
        if type(other) == Vector:
            if self.len == other.len:
                return sum((self.comps[i]*other.comps[i] for i in range(self.len)))
            else:
                return "Длины должны совпадать"
        if type(other) == int:
            return Vector(*(self.comps[i] * other for i in range(self.len)))
        
    def __round__(self):
        return Vector(*(round(self.comps[i]) for i in range(self.len)))
    
    def tuple(self):
        return self.comps