##@package polygonal
#
#@file
#@author Tyler R. Drury
#@copyright 2017 Tyler R. Drury, All Rights Reserved
#@brief represents polygonal Series of the form: f(B,N) = B > 1 ? ((B * N) - B) + 1 : (B * N) + f(B, N - 1)
#
""""
Centred polygonal Number Series of the form
f(B,N) = B > 1 ? ((B * N) - B) + 1 : (B * N) + f(B, N - 1)
Where
@arg B is some numeric base, B > 0
@arg N is a numeric index in the series, N >= 0
"""
#from chrono import timer.timeCall as timeCall
#from timer import timeCall
#
from integerSequence import IntegerSequenceBase as isBase
from integerSequence import inRange as inRange
#
##@class Polygonal polygonal.py
#@brief represents a generic polygonal number sequence
#
#@timeClass
class Polygonal:
    """represents a generic polygonal number sequence"""
    #@timeCall
    @staticmethod
    def test(N = 10):
        """test to make sure recursive and iterative methods return
        the same results and determine how long the algorithms take to run"""
        
        def r(cls):
            print(cls.series(N))
            
        def sit(cls):
            print(cls.seriesIt(N))
        
        T = [
            Triangular,
            Square,
            Pentagonal,
            Hexagonal,
            Heptagonal,
            Octagonal,
            Nonagonal,
            Decagonal,
            Dodecagonal,
            Hexadecagonal,
            Icosagonal,
            Icosipentagonal,
            Pentacontagonal,
            Hectagonal
        ]
        
        #@timeCall
        def rec():
            for t in T:
                r(t)
                
            # r(Triangular)
            # r(Square)
            # r(Pentagonal)
            # r(Hexagonal)
            # r(Heptagonal)
            # r(Octagonal)
            # r(Nonagonal)
            # r(Decagonal)
            # r(Dodecagonal)
            # r(Hexadecagonal)
            # r(Icosagonal)
            # r(Icosipentagonal)
            # r(Pentacontagonal)
            # r(Hectagonal)
            
        #@timeCall
        def it():
            for t in T:
                sit(t)
            
            # sit(Triangular)
            # sit(Square)
            # sit(Pentagonal)
            # sit(Hexagonal)
            # sit(Heptagonal)
            # sit(Octagonal)
            # sit(Nonagonal)
            # sit(Decagonal)
            # sit(Dodecagonal)
            # sit(Hexadecagonal)
            # sit(Icosagonal)
            # sit(Icosipentagonal)
            # sit(Pentacontagonal)
            # sit(Hectagonal)
            
        print("****")
        print("Polygonal Numbers Test")
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
        
        #if base <= 0:
            #raise E("invalid arg base: , number system of base 0 or less is illegal")
        
        #if n < 0:
            #raise E("invalid arg base: , number system of base 0 or less is illegal")
        
        if n == 0:
            return 0

        bn = base * n
        val = (bn - base) + 1 if base > 1 else bn;
        
        return val + Polygonal.elementR(base, n - 1)
    
    @staticmethod
    def elementIt(base, n):
        #assert type(base) is IntType and type(n) is IntType
        
        #if base <= 0:
            #raise E("invalid arg base: , number system of base 0 or less is illegal")
        
        #if n < 0:
            #raise E("invalid arg base: , number system of base 0 or less is illegal")
        if n == 0:
            return 0
        elif n == 1:
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

class Triangular(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polygonal.elementR(1, n)
            
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polygonal.elementIt(1, n)
    
class Square(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polygonal.elementR(2, n)
    
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polygonal.elementIt(2, n)
    
##@class Pentagonal
#[series](https://oeis.org/A000326)
#
class Pentagonal(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polygonal.elementR(3, n)
        
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polygonal.elementIt(3, n)
##@class Hexagonal
#[series](https://oeis.org/A000384)
#
class Hexagonal(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polygonal.elementR(4, n)
        
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polygonal.elementIt(4, n)

##@class Heptagonal
#[series](https://oeis.org/A000566)
#        
class Heptagonal(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polygonal.elementR(5, n)
        
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polygonal.elementIt(5, n)
        
##@class Octagonal
#[series](https://oeis.org/A000567)
#        
class Octagonal(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polygonal.elementR(6, n)
    
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polygonal.elementIt(6, n)

##@class Nonagonal
#[series](https://oeis.org/A001106)
#                
class Nonagonal(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polygonal.elementR(7, n)
    
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polygonal.elementIt(7, n)

##@class Decagonal
#[series](https://oeis.org/A001107)
#        
class Decagonal(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polygonal.elementR(8, n)
    
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polygonal.elementIt(8, n)

##@class Dodecagonal
#[series]()
#                
class Dodecagonal(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polygonal.elementR(10,n)
        
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polygonal.elementIt(10, n)

##@class Hexadecagonal
#[series]()
#                
class Hexadecagonal(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polygonal.elementR(14, n)
    
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polygonal.elementIt(14, n)
        
##@class Icosagonal
#[series]()
#
class Icosagonal(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polygonal.elementR(18, n)
    
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polygonal.elementIt(18, n)

##@class Icosipentagonal
#[series]()
#        
class Icosipentagonal(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polygonal.elementR(23, n)
    
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polygonal.elementIt(23, n)

##@class Pentacontagonal
#[series]()
#        
class Pentacontagonal(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polygonal.elementR(48, n)
        
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polygonal.elementIt(48, n)

##@class Hectagonal
#[series]()
#        
class Hectagonal(isBase):
    @classmethod
    def element(cls, n, unbound = False):
        return Polygonal.elementR(98, n)
        
    @classmethod
    def elementIt(cls, n, unbound = False):
        return Polygonal.elementIt(98, n)
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
