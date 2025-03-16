from typing import Union, List

class Vector:
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
                return self + (-other)
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
        
    

class Poly:
    def __init__(self, coefs: Union[List[int], int]):

        if type(coefs) == int:
            self.coefs = [coefs]
            self.deg = 0

        elif type(coefs) == list:
            self.coefs = coefs
            self.deg = len(coefs) - 1
    
    def __neg__(self):
        coefs = [-a for a in self.coefs]

        return Poly(coefs)
    
    def __add__(self, other):
        if type(other) == int:
            return self + Poly(other)
        
        if type(other) == Vector:
            new_comps = []
            for com in other.comps:
                new_comps.append(self + com)
            
            return Vector(*new_comps)
        
        if type(other) == Poly:
            p = self.coefs + [0]*other.deg
            q = other.coefs + [0]*self.deg

            n = max(self.deg, other.deg)
            result = [0]*n

            for k in range(n):
                result[k] = p[k] + q[k]

            return Poly(result)
    
    def __sub__(self, other):
        return self + (-other)
    
    def __mul__(self, other):
        if type(other) == int:
            coefs = [other*a for a in self.coefs]

            return Poly(coefs)
        
        elif type(other) == Vector:
            new_coms = []
            
            for com in other.comps:
                new_coms.append(self * com)
            
            return Vector(*new_coms) 
        
        elif type(other) == Poly:
            n = self.deg
            m = other.deg
            p = list(self.coefs) + [0] * other.deg
            q = list(other.coefs) + [0] * self.deg            
            result = [0]*(self.deg + other.deg + 1)
            
            for k in range(self.deg + other.deg + 1):
                for l in range(k + 1):
                    result[k] += p[l]*q[k-l]

            return Poly(result)

    def __str__(self):
        res = []
        for i in range(self.deg+1):
            if self.coefs[i] == 0:
                continue
            
            if i == 0:
                res.append(f"({self.coefs[i]})")
            elif i == 1:
                res.append(f"({self.coefs[i]}*x)")
            else:
                res.append(f"({self.coefs[i]}*x^{i})")
        return ' + '.join(res)
    
    def value(self, t):
        res = 0
        for i in range(self.deg+1):
            res += self.coefs[i]*(t**i)
        return res
    
    def diff(self):
        if self.deg > 0:
            coefs = [self.coefs[i] * i for i in range(1, self.deg + 1)]
            return Poly(coefs)
        else:
            return 0
    
    pass


def interpol(points: List[tuple]) -> Poly:
    n = len(points)

    X = tuple(point[0] for point in points)
    Y = tuple(point[1] for point in points)
    
    res = Poly([0]*n)

    for i in range(n):
        iter = Poly([0]*n)
        iter.coefs[0] = 1

        for j in range(n):
            if i==j:
                continue    

            dx = 1/(X[i] - X[j])
            iter = iter * Poly([-X[j]*dx, dx])

        res = res + (iter * Y[i])
    return res


