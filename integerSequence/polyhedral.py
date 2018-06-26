##@file
#@author Tyler R. Drury
#@copyright 2017 Tyler R. Drury, All Rights Reserved
#@brief represents polyhedral Series of the form: f(B,N) = B > 1 ? ((B * N) - B) + 1 : (B * N) + f(B, N - 1)
#
""""
region polygonal Number Series of the form
f(B,N) = B > 1 ? ((B * N) - B) + 1 : (B * N) + f(B, N - 1)
Where
@arg B is some numeric base, B > 0
@arg N is an index in the series, N >= 0
"""
#from chrono import timer.timeCall as timeCall
#from timer import timeCall
#
from integerSequence import IntegerSequenceBase as isBase
from integerSequence import inRange as inRange
#
##@class Polyhedral polyhedral.py
#@brief represents a generic polygonal number sequence
#
#@timeClass
class Polyhedral:
    """represents a generic polygonal number sequence"""
    #@timeCall
    @staticmethod
    def test(N = 15):
        """test to make sure recursive and iterative methods return
        the same results and determine how long the algorithms take to run"""
        
        def r(cls):
            print(cls.__name__)
            print(cls.series(N))
            
        def sit(cls):
            print(cls.__name__)
            print(cls.seriesIt(N))
        
        T = [
            Tetrahedral,
            Cube,
            Pentahedral,
            Hexahedral,
            Heptahedral,
            Octahedral,
            # Nonahedral,
            # Decahedral,
            # Dodecahedral,
            # Hexadecahedral,
            # Icosahedral,
            # Icosipentahedral,
            # Pentacontahedral,
            # Hectahedral
        ]
        
        #@timeCall
        def rec():
            for t in T:
                r(t)
            
        #@timeCall
        def it():
            for t in T:
                sit(t)
            
        
        print("****")
        print("Polyhedral Numbers Test")
        print("****")
        print("recursive functions")
        #
        rec()
        #
        print("****")
        print("iterative functions")
        #
        it()
    #
    @staticmethod
    def elementR(base, n):
        #assert type(base) is IntType and type(n) is IntType
        #assert base >= 4
        
        #if base <= 0:
            #raise E("invalid arg base: , number system of base 0 or less is illegal")
        
        #if n < 0:
            #raise E("invalid arg base: , number system of base 0 or less is illegal")
        
        if n == 0:
            return 1
        if n == 1:
            return 1 + base
        #f(B,N) = B > 1 ? (B * N) + 1 : (B * N) + f(B, N - 1)
        
        #return ((n*n + n)*(n+2)) // 6 #(n * (n + 1) * (n + 2)) // 6
        #return ((n*n*n + 3*n*n + 2n) // 6 #(n * (n + 1) * (n + 2)) // 6
        
        #nmo = n - 1
        #return (n * ( (n*n*n) + base * (n*n) + base * n + 1)) // (nmo*nmo*nmo*nmo)
        
        #hb = base * n
        f = (base + 1) * (n) #if not (base & 1) else (base + 1) // 2
        p = (f) + Polyhedral.elementR(base, n - 1)
        
        return p
        # bn = base * n
        # val = (bn - base) + 1 if base > 1 else bn;
        
        # return val + Polyhedral.elementR(base, n - 1)
    
    @staticmethod
    def elementIt(base, n):
        #assert type(base) is IntType and type(n) is IntType
        
        #if base <= 0:
            #raise E("invalid arg base: , number system of base 0 or less is illegal")
        
        #if n < 0:
            #raise E("invalid arg base: , number system of base 0 or less is illegal")
        if n == 0:
            return 1
        
        prev = 0
        ret = 1
        #
        for i in range(1, n):
            bn = base * i
            val = (bn - base) + 1 if base > 1 else bn
            ret = val + prev
            prev = ret
            #print('f({I}) = {N}, val = {V}, f(n - 1) = {P}'.format(I=i, N=ret, V=val, P=prev))
            #prev = ret
        
        bn = base * n
        val = (bn - base) + 1 if base > 1 else bn
        ret = val + prev
        #print('f({N}) = {R}'.format(N=n, R=ret))    
        
        return ret
#
class Tetrahedral(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polyhedral.elementR(3, n)
            
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polyhedral.elementIt(3, n)
            
class Cube(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polyhedral.elementR(4, n)
            
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polyhedral.elementIt(4, n)
    
##@class Pentahedral
#[series](https://oeis.org/A000326)
#
class Pentahedral(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polyhedral.elementR(5, n)
        
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polyhedral.elementIt(5, n)
##@class Hexahedral
#[series](https://oeis.org/A000384)
#
class Hexahedral(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polyhedral.elementR(6, n)
        
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polyhedral.elementIt(6, n)

##@class Heptahedral
#[series](https://oeis.org/A000566)
#        
class Heptahedral(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polyhedral.elementR(7, n)
        
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polyhedral.elementIt(7, n)
        
##@class Octahedral
#[series](https://oeis.org/A000567)
#        
class Octahedral(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polyhedral.elementR(8, n)
    
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polyhedral.elementIt(8, n)

##@class Nonahedral
#[series](https://oeis.org/A001106)
#                
class Nonahedral(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polyhedral.elementR(9, n)
    
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polyhedral.elementIt(9, n)

##@class Decahedral
#[series](https://oeis.org/A001107)
#        
class Decahedral(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polyhedral.elementR(10, n)
    
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polyhedral.elementIt(10, n)

##@class Dodecahedral
#[series]()
#                
class Dodecahedral(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polyhedral.elementR(12,n)
        
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polyhedral.elementIt(12, n)

##@class Hexadecahedral
#[series]()
#                
class Hexadecahedral(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polyhedral.elementR(16, n)
    
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polyhedral.elementIt(16, n)
        
##@class Icosahedral
#[series]()
#
class Icosahedral(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polyhedral.elementR(20, n)
    
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polyhedral.elementIt(20, n)

##@class Icosipentahedral
#[series]()
#        
class Icosipentahedral(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polyhedral.elementR(25, n)
    
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polyhedral.elementIt(25, n)

##@class Pentacontahedral
#[series]()
#        
class Pentacontahedral(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polyhedral.elementR(50, n)
        
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polyhedral.elementIt(50, n)

##@class Hectahedral
#[series]()
#        
class Hectahedral(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polyhedral.elementR(100, n)
        
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polyhedral.elementIt(100, n)
#
#class ...hectagonal(n):
    # @classmethod
    # def element(cls, n, unbound = False):
        # return Polygonal.elementR(253, N)

#class ..hectagonal
    # @classmethod
    # def element(cls, n, unbound = False):
        #polygonalSeries<65535, N>{
#
