##@file
#@author Tyler R. Drury
#@date June 2016
#@copyright Tyler R. Drury, All Rights Reserved
#@brief represents Horadam series of the form f(n) = r * f(n-1) + s * f(n-2) [f(0) = p, f(1) = q]
#

##@todo A001519		a(n) = 3*a(n-1) - a(n-2), with a(0) = a(1) = 1, NOTE:Horadam(1,1,3,-1)
##@todo A006190		a(n) = 3*a(n-1) + a(n-2), with a(0)=0, a(1)=1. NOTE:Horadam(0,1,3,1)

#print('numeric sequence library')
#
#from chrono import Timer
#from chrono import Timer.timeCall
#
#from timer import Timer
#from timer import timeCall
#
from integerSequence import IntegerSequenceBase as Base
from integerSequence import isNegativeThrow as isNegThrow
from integerSequence import inRange as inRange
#
#@timeCall
def isEqual(lhs, rhs):
    """types should be a either a list, tuple, etc"""
    for x,y in zip(lhs, rhs):
        if x == y:
            continue
        else:
            return False
            
    return True
#

##@class Horadam horadam.py
#equation of the form: f(n) = r * f(n-1) + s * f(n-2); [f(0) = p, f(1) = q]
#
class Horadam():
    """represents a binomial expression of the format:
    f(n) = r * f(n-1) + s * f(n-2) [f(0) = p, f(1) = q]
    NOTE:aside from ensuring N > 0, this class does not support
    bounds checking and will return a python integer of arbitrary length,
    NOT for use with C(or related) APIs,
    as the returned value may cause integer overflow.
    Please use the other convenience classes provided by this library
    for bounds checking when embedding Python.
    There are no supporting documentation for the auto-generated series,
    please reference specific helper class for specific documentation"""
    __slots__ = ['_p', '_q', '_r', '_s']
    
    def __init__(self, p, q, r, s):
        """p, q, r, s MUST be integer values, or types convertible to integers"""
        self._p = int(p)    #n(0)
        self._q = int(q)    #n(1)
        self._r = int(r)    #coefficient of first term, r * f(n-1)
        self._s = int(s)    #coefficient of second term, s * f(n-2)
        
    # def __init__(self, *args, **kwargs):
        # """convenience keyword"""
        # self._p = int(p)    #n(0)
        # self._q = int(q)    #n(1)
        # self._r = int(r)    #coefficient of first term, r * f(n-1)
        # self._s = int(s)    #coefficient of second term, s * f(n-2)
    
    #@timeCall    
    def element(self, n):
        """returns value for element N in the series as an integer"""
        #assert type(n) is IntType
        isNegThrow(n)
        
        if n == 0:
            return self._p
        if n == 1:
            return self._q

        return self._r * self.element(n - 1) + self._s * self.element(n - 2)
    
    #@timeCall    
    def elementIt(self, n):
        """returns value for element N in the series as an integer"""
        #assert type(n) is IntType
        isNegThrow(n)
        
        if n == 0:
            return self._p
        elif n == 1:
            return self._q
        
        prev = self._p    #first element n - 2
        ret = self._q     #second element n - 1
        
        for i in range(1, n):
            v = prev   #v stores previous value
            
            prev = ret #prev stores what will be previous value on next iteration
            ret = self._r * ret + self._s * v
        
        return ret

    def __str__(self):
        return 'p: {P},\nq: {Q},\nr: {R},\ns: {S}'.format(P=str(self._p), Q=str(self._q),R=str(self._r), S=str(self._s))

    def _generator(self, n):
        #try:
            #convert any not integer type to an integer
            #n = n if type n is IntType else int(n)
        isNegThrow(n)
        
        for i in range(n):
            yield self.element(i)
        
        #except as e:
            #print(e.error)
            
    def _generatorIt(self, n):
        
        # #try:
        # #convert any not integer type to an integer
        # #n = n if type n is IntType else int(n)
        isNegThrow(n)

        for i in range(n):
            yield self.elementIt(i)
            
            
            
        # if n == 0:
            # yield self._p
        # if n == 1:
            # yield self._q

        # prev = self._p    #first element n - 2
        # ret = self._q     #second element n - 1
        
        # for i in range(1, n):
            # v = prev   #v stores previous value
            # prev = ret #prev stores what will be previous value on next iteration
            # ret = self._r * ret + self._s * v
    
            # yield ret
        
        # #except as e:
            # #print(e.error)
    
    #@timeCall
    def _listIt(self, n):
        #assert type(n) is IntType        
        return [f for f in self._generatorIt(n)]
    
    #@timeCall
    def _tupleIt(self, n):
        return tuple(f for f in self._generatorIt(n))
        
    #@timeCall
    def _list(self, n):
        #assert type(n) is IntType        
        return [f for f in self._generator(n)]
    
    #@timeCall
    def _tuple(self, n):
        return tuple(f for f in self._generator(n))
    #
    #public methods
    #
    def series(self, n):
        """returns a series of N number of elements
        @return tuple of integers"""
        return self._tuple(n)
    
    def seriesIt(self, n):
        """returns a series of N number of elements
        @return tuple of integers"""
        return self._tupleIt(n)
        
    @staticmethod
    def _isEqual(lhs, rhs, n):
        return isEqual(lhs.series(n), rhs.series(n))
        
    @staticmethod
    def _isEqualIt(lhs, rhs, n):
        return isEqual(lhs.seriesIt(n), rhs.seriesIt(n))
         
    #@timeCall
    def validate(d, n = 10):
        """validates up to 10 elements in a series,
        """
        k = d.keys()
        l = len(k)
        r = range(0, l)
        
        for i in r:
            for j in r:
                if i == j:
                    continue
                    
                if not Horadam._isEqual(d[k[i]], d[k[j]], n):
                    return False
                
        return True
        
    def validateIt(d, n = 10):
        """validates up to 10 elements in a series,
        """
        k = d.keys()
        l = len(k)
        r = range(0, l)
        
        for i in r:
            for j in r:
                if i == j:
                    continue
                    
                if not Horadam._isEqualIt(d[k[i]], d[k[j]], n):
                    return False
                
        return True
    
    #@staticmethod
    #def getNameSeries():
        """returns all familiar Named Horadam Series"""
        # return T = [
            # Fibonacci,
            # Jacobsthal,
            # Lucas,
            #
            #
            # Lucas.Oblong
            # Pell,
            # Pell.Companion
            # NewmanShakesWilliam
        # ]
    #@timeCall
    @staticmethod
    def builtins():
        def _dictGen(extended = False):#**kwargs): #start = 0, stop = 2)
            """generates all fundamental Horadam Series from either 0111-2222 || 0111-9999"""
            ret = {}
            s = 10 if extended else 3
            
            p = {'start':0,'stop':s}
            q = {'start':0,'stop':s}
            r = {'start':1,'stop':s}   #r = {'start':-9,'stop':10}
            s = {'start':1,'stop':s}   #s = {'start':-9,'stop':10}
            #inc = 1
            
            for a in range(p['start'], p['stop']):
                for b in range(1 if a == 0 else q['start'], q['stop']):                    
                    for c in range(r['start'], r['stop']):
                        if c == 0:
                            continue
                            
                        for d in range(s['start'], s['stop']):
                            if d == 0:
                                continue
                            k = str(a) + str(b) + str(c) + str(d)
                            v = Horadam(a,b,c,d)
                            
                            #assert(k not in d.keys())
                            #print(k)
                            #print(v)
                            ret[k] = v
                        
                        #print()
            return ret
        
        ret = _dictGen()
        #assert(Horadam.validate(ret))
        return ret
        # d = {
            # '0' : Horadam._dictGen(),
            # #
            # '1' : Horadam._dictGen(),
            # #
            # '2' : Horadam._dictGen(),
            # '3' : Horadam._dictGen(),
            # '4' : Horadam._dictGen(),
            # '5' : Horadam._dictGen(),
            # '6' : Horadam._dictGen(),
            # '7' : Horadam._dictGen(),
            # '8' : Horadam._dictGen(),
            # '9' : Horadam._dictGen(),
        # }
        
        # return {k : v for k, v in d.items()}
    #@timeCall
    @staticmethod
    def test():
        n = 15
        h = Horadam.builtins()
        # for k in d:
            # print(k)
        c = 0
        
        print('****')
        print('Horadam Built-in Sequences')
        print('****')
        
        for k, v in h.items():
            print("Recursive Series {S}".format(S= k))
            print(v.series(n))
            # c += 1
        
        for k, v in h.items():
            print("Iterative Series {S}".format(S= k))
            print(v.seriesIt(n))
        # print('series count: {C}'.format(C=c))
        
        print('****')
        print('Named Sequences')
        
        c = 10

        #@timeCall
        def r(cls):
            print(cls.__name__ + ' series:')
            print(cls.series(c))
            print('')
            
        def it(cls):
            print(cls.__name__ + ' series:')
            print(cls.seriesIt(c))
            print('')
        
        #series types
        T = [
            Fibonacci,
            Fibonacci.Squared,
            Fibonacci.GoldenRectangle,
            #
            Jacobsthal,
            #
            Lucas,
            #
            Pell,
            Pell.Companion,
            #
            NewmanShakesWilliam
        ]
        
        #@timeCall
        # def rec():
            # #for t in T:
                # #r(t)
            # p('fibonacci', Fibonacci.series) #confirmed+
            # #print('Squared Fibonacci', fib.Squared.seriesIt(25)) #++
            # #print('Golden Rectangle', fib.GoldenRectangle.seriesIt(18)) #++
            
            # p('jacobsthal', Jacobsthal.series)  #confirmed+
            # p('lucas', Lucas.series)   #confirmed+
            # p('Newman-Shakes-William', NewmanShakesWilliam.series) #confirmed+
            # p('Pell', Pell.series) #confirmed+
            # #
            # p('Pell Companion', Pell.Companion.series)
            # #p('Conway-Guy', conGuyR.series)
            # #
            # #print('Pell-Lucas Series')
            # #
            # #print('Hofstadter Series')
            # #
        
        #@timeCall
        # def it():
            # #
            # p('fibonacci', Fibonacci.seriesIt)    #confirmed+
            # p('jacobsthal', Jacobsthal.seriesIt) #confirmed+
            # p('lucas', Lucas.series)  #confirmed+
            # p('Newman-Shakes-William', NewmanShakesWilliam.seriesIt)    #confirmed+
            # p('Pell', Pell.seriesIt)    #confirmed+
            # #
            # p('Pell Companion', Pell.Companion.seriesIt)
            # #p('Conway-Guy', conGuyIt.series)
        #
        print('****')
        print('recursive')
       
        for t in T:
            r(t)

        print('****')
        print('iterative')
        
        for t in T:
            it(t)
            
        print('****')

##@todo Pisano Numbers
##@todo A001654(n) / A007598(n) ~= Golden ratio
##@todo A180662    golden triangle where f(n,k) = A001654(k) for n >= 0 && 0<=k<=n
##todo A008346		a(n) = Fibonacci(n) + (-1)^n.

##@class Fibonacci
#series [A000045](https://oeis.org/A000045)
#
class Fibonacci(Base):
    """"""
    #class constant representing a binomial equation for generating a numeric sequence
    _h = Horadam(0,1,1,1)
    
    @classmethod
    def element(cls, n, unbound = False):
        """returns value for element N in the series"""
        #assert type(n) is IntType
        
        inRange(n, 46, unbound)

        return cls._h.element(n)
    
    @classmethod
    def elementIt(cls, n, unbound = False):
        inRange(n, 46, unbound)
        return cls._h.elementIt(n)
        
    ##@class Squared
    #series [A007598](https://oeis.org/A007598)
    #
    class Squared(Base):
        @classmethod
        def element(cls, n, unbound = False):
            inRange(n, 24, unbound)
            f = Fibonacci.element(n)
            return f * f
        
        @classmethod
        def elementIt(cls, n, unbound = False):
            inRange(n, 24, unbound)
            f = Fibonacci.elementIt(n)
            return f * f
    
    ##@class GoldenRectangle
    #series [A001654](https://oeis.org/A001654)
    #
    class GoldenRectangle(Base):
        """f(n) = fib(n) * fib(n + 1) where fib(n) = Fibonacci(n)"""
        @classmethod
        def element(cls, n, unbound = False):
            #inRange(n, 25, unbound)
            return Fibonacci.element(n) * Fibonacci.element(n + 1)
        
        @classmethod
        def elementIt(cls, n, unbound = False):
            #inRange(n, 25, unbound)
            return Fibonacci.elementIt(n) * Fibonacci.elementIt(n + 1)
            
    #class GoldenNumbers


# class Pisano(Base):
    # """Pisano period, the length of repeating """
    # _seq = Fibonacci.seriesIt(46)
    
    # @classmethod
    # def element(cls, n, unbound = False):
        
        # if n == 0:
            # return 1
        
        # seq = [(x % n + 1) for x in cls._seq]
        
        # #print(N)
        
        # #for x in cls._seq:
            # #m = x % N
            # #print('f:{F}, m:{M}'.format(F=x, M=m))
        
        # l = 1
        # sl = len(seq)   #sequence length
        # hl = l >> 2    #half length
        
        # for x in range(2, hl):
            # s = seq[0:x]
            
            # if s == seq[x:2*x]:
                # l = len(s)
        
        # print(l)
        
        # return l
        
    # @classmethod
    # def elementIt(cls, n, unbound = False):
        # # if n < 1:
            # # ValueError('invalid value of argument n with value ({N}, value must be greater than or equall to 1)'.format(N=n))
        
        # if n == 0:
            # return 1
            
        # seq = [x % (n + 1) for x in cls._seq]
        
        # print(seq)
        
        # l = 1
        # sl = len(seq)   #sequence length
        # hl = l >> 2    #half length
        
        # for x in range(2, hl):
            # if seq[0:x] == seq[x:2*x]:
                # l = x

        # return l
        
    
##@class Newman-Shakes-William
#[series](https://oeis.org/A002315)
#
class  NewmanShakesWilliam(Base):
    """https://oeis.org/A002315"""
    _h = Horadam(1,7,6,-1)
    
    @classmethod
    def element(cls, n, unbound = False):
        inRange(n, 9, unbound)
        
        if n == 0:
            return 1
        elif n == 1:
            return 7

        return 6 * cls.element(n - 1) - cls.element(n - 2)
        #return cls._h.elementR(n)
    
    @classmethod
    def elementIt(cls, n, unbound = False):
        inRange(n, 9, unbound)
        return cls._h.elementIt(n)

##@todo A101622		A Horadam-Jacobsthal sequence.

# ##@class A101622
# #[series](https://oeis.org/A101622)
# #
# class A101622(Base):
    # """series A001045"""
    # #class constant representing a binomial equation for generating a numeric sequence
    # _h = Horadam(0,1,1,2)
    
    # @classmethod
    # def element(cls, n, unbound = False):
        # #assert type(n) is IntType

        # inRange(n, 33, unbound)
        # return cls._h.element(n)
        
    # @classmethod
    # def elementIt(cls, n, unbound = False):
        # inRange(n, 33, unbound)
        # return cls._h.elementIt(n)

##@class Jacobsthal
#series [A001045](https://oeis.org/A001045)
#
class Jacobsthal(Base):
    """series A001045"""
    #class constant representing a binomial equation for generating a numeric sequence
    _h = Horadam(0,1,1,2)
    
    @classmethod
    def element(cls, n, unbound = False):
        #assert type(n) is IntType

        inRange(n, 33, unbound)
        return cls._h.element(n)
        
    @classmethod
    def elementIt(cls, n, unbound = False):
        inRange(n, 33, unbound)
        return cls._h.elementIt(n)
        
    # ##@class Oblong
    # #series [A084175](https://oeis.org/A084175)
    # #
    # class Oblong(Base):
        #"""f(n) = J(n) * J(n + 1)"""
        # @classmethod
        # def element(cls, n, unbound = False):
            # #assert type(n) is IntType
            #inRange(n, unbound)
            # return Jacobsthal.element(n, unbound) * Jacobsthal.element(n + 1, unbound)
            
        # @classmethod
        # def elementIt(cls, n, unbound = False):
            #inRange(n, unbound)
            # return Jacobsthal.elementIt(n, unbound) * Jacobsthal.elementIt(n + 1, unbound)
        

##@todo A005013		a(n) = 3*a(n-2) - a(n-4), a(0)=0, a(1)=1, a(2)=1, a(3)=4. Alternates Fibonacci (A000045) and Lucas (A000032) sequences for even and odd n    

##@class Lucas
#[sequence](https://oeis.org/A000032)
#
class Lucas(Base):
    """numeric sequence https://oeis.org/A000032
    returns value for element N in the series, 0 based indices"""
    _h = Horadam(2,1,1,1) #class constant
    
    @classmethod
    def element(cls, n, unbound = False):
        inRange(n, 46, unbound)
        return cls._h.element(n)
    
    @classmethod
    def elementIt(cls, n, unbound = False):
        inRange(n, 46, unbound)
        return cls._h.elementIt(n)

    
    # ##@class A005248
    # #sequence [A005248](https://oeis.org/A005248)
    # #    
    # class A005248:
        # @classmethod
        # def element(cls, n, unbound = False):
            # return Lucas.element(2 * n)
        
        # @classmethod
        # def elementIt(cls, n, unbound = False):
            # return cls._h.elementIt(2 * n)

    # ##@class A002878
    # #sequence [A002878](https://oeis.org/A002878)
    # #
    # class A002878:
        # @classmethod
        # def element(cls, n, unbound = False):
            # return Lucas.element(2 * n + 1)
        
        # @classmethod
        # def elementIt(cls, n, unbound = False):
            # return Lucas.elementIt(2 * n + 1)

    # ##@class A240926
    # #sequence [A240926](https://oeis.org/A240926)
    # #
    #class A240926(Base):
        """a(n) = 2 + L(2*n)"""
        # @classmethod
        # def element(cls, n, unbound = False):
            # return Lucas.element(2 * n) + 2
        
        # @classmethod
        # def elementIt(cls, n, unbound = False):
            # return Lucas.elementIt(2 * n) + 2
            
            
# ##@class Jacobsthal-Lucas
# #sequence [A014551](https://oeis.org/A014551)
# #        
# class JacobsthalLucas(Base):
    # @classmethod
    # def element(cls, n, unbound = False):
        # inRange(n, 46, unbound)
        # return 2 ** n + (-1) ** n
    
##@todo A113449		Sum of the square root of n-th square triangular number and n-th Pell (or lambda) number 
    
##@class Pell
#[sequence](http://oeis.org/A000129)
#
class Pell(Base):
    """http://oeis.org/A000129"""
    _h = Horadam(0,1,2,1)
    
    @classmethod
    def element(cls, n, unbound = False):
        #assert type(n) is IntType, 'arg n must be an integer value'
        #
        #inRange(n, , unbound)
        # return 2 * cls.element(n - 1) + cls.element(n - 2)
        return cls._h.element(n)
        
    @classmethod
    def elementIt(cls, n, unbound = False):
        return cls._h.elementIt(n)

    ##@class Companion
    #[series](http://oeis.org/A000129)
    #
    class Companion(Base):
        """http://oeis.org/A000129"""
        #class constant representing a binomial equation for generating a numeric sequence
        _h = Horadam(2,2,2,1)
        
        @classmethod
        def element(cls, n, unbound = False):
            #assert type(n) is IntType, 'arg n must be an integer value'
            #
            #inRange(n, 33, unbound)
            
            return cls._h.element(n)    #2 * cls.element(n - 1) + cls.element(n - 2)

        @classmethod
        def elementIt(cls, n, unbound = False):
            #inRange(n, 33, unbound)
            return cls._h.elementIt(n)

 
#

#test()
 
# #
# #unsigned integer sequences, all values of f(n) are >= 0
# #
# '0011' : Horadam(0,0,1,1), #result is series of 0's
# '0111' : Horadam(0,1,1,1), #fibonacci series
# '1011' : Horadam(1,0,1,1),  #1,0,1,1,2,3,5,8
# '1111' : Horadam(1,1,1,1),  #1,1,2,3,5,8,13
# #
# #01sr   series
# #
# #'0111' : Horadam(0,1,1,1), #fibonacci series
# '0112' : Horadam(0,1,1,2), #    0,1,2,4,8,16,32
# '0121' : Horadam(0,1,2,1), #    0,1,2,5,12,29
# '0122' : Horadam(0,1,2,2), #    0,1,2,6,16
# #
# '0123' : Horadam(0,1,2,3),
# '0124' : Horadam(0,1,2,4), #A085449
# '0125' : Horadam(0,1,2,5),
# '0126' : Horadam(0,1,2,6),
# #
# # '0133' : Horadam(0,1,3,3),
# # '0134' : Horadam(0,1,3,4),
# # '0135' : Horadam(0,1,3,5),
# # '0136' : Horadam(0,1,3,6),
# '0139' : Horadam(0,1,3,9),  #A085504		Horadam sequence

# '0146' : Horadam(0,1,4,6),    #A085939		Horadam sequence
# #
# #02sr   series
# #
# '0211' : Horadam(0,2,1,1), #    0,2,2,4,6,10,16,26
# '0221' : Horadam(0,2,2,1), #    0,2,4,10,24,38
# '0212' : Horadam(0,2,1,2), #    0,2,2,6,10,22,42
# '0222' : Horadam(0,2,2,2), #    0,2,4,12,32,88
# #
# #10sr   series
# #
# #'1011' : Horadam(0,1,1,1), #
# '1012' : Horadam(1,0,1,2), #    1,0,2,2,6,10,22
# '1021' : Horadam(1,0,2,1), #    1,0,1,2,5,12,29
# '1022' : Horadam(1,0,2,2), #    1,0,2,4,12,32
# #
# #11sr   series
# #
# #'1111' : Horadam(1,1,1,1)
# '1112' : Horadam(1,1,1,2), #    1,1,3,5,11,21,43
# '1121' : Horadam(1,1,2,1), #    1,1,3,7,17,41
# '1122' : Horadam(1,1,2,2), #    1,1,4,10,28,76
# #
# #12sr   series
# #
# '1211' : Horadam(1,2,1,1), #    1,2,3,5,8,13,21
# '1221' : Horadam(1,2,2,1), #    1,2,5,12,29,70
# '1212' : Horadam(1,2,1,2), #    1,2,4,8,16,32,64    series 2^n
# '1222' : Horadam(1,2,2,2), #    1,2,6,16,44
# #
# #20sr   series
# #
# '2011' : Horadam(2,0,1,1), #    2,0,2,2,4,6,10,16
# '2021' : Horadam(2,0,2,1), #    2,0,2,4,10,24,38
# '2012' : Horadam(2,0,1,2), #    2,0,4,4,12,20,44
# '2022' : Horadam(2,0,2,2), #    2,0,4,8,24,64
# #
# #21sr   series
# #
# '2111' : Horadam(2,1,1,1), #    2,1,3,4,7,11,18,29
# '2121' : Horadam(2,1,2,1), #    2,1,4,9,22,53
# '2112' : Horadam(2,1,1,2), #    2,1,5,7,17,31
# '2122' : Horadam(2,1,2,2), #    2,1,6,14,40,108
# #
# #22sr   series
# #
# '2211' : Horadam(2,2,1,1), #    2,2,4,6,10,16,26
# '2221' : Horadam(2,2,2,1), #    2,2,6,10,22,42
# '2212' : Horadam(2,2,1,2), #    2,2,6,14,34,82
# '2222' : Horadam(2,2,2,2) #    2,2,8,20,56,152
#
#signed numeric series, NOTE: values can be negative
#
# #'0011' : Horadam(0,0,1,1), #result is series of 0's
# '0111' : Horadam(0,1,1,1), #fibonacci series
# '1011' : Horadam(1,0,1,1),
# '1111' : Horadam(1,1,1,1),
# #
# #01sr   series
# #
# #'0111' : Horadam(0,1,1,1), #fibonacci series
# '0112' : Horadam(0,1,1,2), #
# '0121' : Horadam(0,1,2,1), #
# '0122' : Horadam(0,1,2,2), #
# #
# '0142' : Horadam(0,1,4,2), #A085449
# #
# '0164' : Horadam(0,1,6,4),    #A085939		Horadam sequence
# '0193' : Horadam(0,1,9,3)  #A085504		Horadam sequence
# #
# #02sr   series
# #
# '0211' : Horadam(0,2,1,1), #
# '0221' : Horadam(0,2,2,1), #
# '0212' : Horadam(0,2,1,2), #
# '0222' : Horadam(0,2,2,2), #
# #
# #10sr   series
# #
# #'1011' : Horadam(0,1,1,1), #
# '1012' : Horadam(1,0,1,2), #
# '1021' : Horadam(1,0,2,1), #
# '1022' : Horadam(1,0,2,2), #
# #
# #11sr   series
# #
# #'1111' : Horadam(1,1,1,1)
# '1112' : Horadam(1,1,1,2), #
# '1121' : Horadam(1,1,2,1), #
# '1122' : Horadam(1,1,2,2), #
# #
# #12sr   series
# #
# '1211' : Horadam(1,2,1,1), #
# '1221' : Horadam(1,2,2,1), #
# '1212' : Horadam(1,2,1,2), #
# '1222' : Horadam(1,2,2,2), #
# #
# #20sr   series
# #
# '2011' : Horadam(2,0,1,1), #
# '2021' : Horadam(2,0,2,1), #
# '2012' : Horadam(2,0,1,2), #
# '2022' : Horadam(2,0,2,2), #
# #
# #21sr   series
# #
# '211-1' : Horadam(2,1,1,-1), #
# '21-11' : Horadam(2,1,-1,1), #
# '21-12' : Horadam(2,1,-1,2), #
# '21-1-1' : Horadam(2,1,-1,-1), #
# '21-1-2' : Horadam(2,1,-1,-2), #
# '21-21' : Horadam(2,1,2,1), #
# '211-1' : Horadam(2,1,1,1), #

# '212-1' : Horadam(2,1,2,1), #
# '211-2' : Horadam(2,1,1,2), #

# '21-2-2' : Horadam(2,1,2,2), #
# #
# #22sr   series
# #
# '22-11' : Horadam(2,2,-1,1), #    2,2,0,2,-2,4,-6,10
# '22-12' : Horadam(2,2,-1,2), #    2,2,0,2,-2,4,-6,10
# '221-1' : Horadam(2,2,1,-1), #    2,2,0,-2,-2,0,2,2,0
# '22-1-1' : Horadam(2,2,-1,-1), #    2,2,-4,4,0,-4,4
# '22-21' : Horadam(2,2,1,-1), #    2,2,0,-2,-2,0,2,2,0
# '22-2-1' : Horadam(2,2,-2,-1), #    2,2,-6,8,4,0,-4,8,-12
# #'22-2-2' : Horadam(2,2,1,-1), #    2,2,0,-2,-2,0,2,2,0