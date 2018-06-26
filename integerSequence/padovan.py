##@file
#@author Tyler R. Drury
#@date June 2016
#@copyright Tyler R. Drury, All Rights Reserved
#@brief represents Padovan series of the form f(n) = r * f(n-2) + s * f(n-3) [f(0) = o, f(1) = p, f(2) = q]
#

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
    print(lhs)
    print(rhs)
    
    for x,y in zip(lhs, rhs):
        if x == y:
            continue
        else:
            return False
            
    return True
#

##@todo A200220 a(n) = fib(n+1) * p(n+5)

##@class Padovan Padovan.py
#recurrence of the form: f(n) = r * f(n-2) + s * f(n-3); [f(0) = o, f(1) = p, f(2) = q]
#@arg o f(0) integer in series
#@arg p f(1) integer in series
#@arg q f(2) integer in series

#Padovan(1,0,0,1,1) #https://oeis.org/A000931 
#Padovan(1,1,1,1,1)	#https://oeis.org/A000931 except missing the starting: [1, 0, 0, 1, 0]
#
class Padovan():
    """represents a binomial expression of the format:
    f(n) = r * f(n-2) + s * f(n-3) [f(0) = o, f(1) = q, f(2) = q]
    NOTE:aside from ensuring N > 0, this class does not support
    bounds checking and will return a python integer of arbitrary length,
    NOT for use with C(or related) APIs,
    as the returned value may cause integer overflow.
    There are no supporting documentation for the auto-generated series,
    please reference specific helper class for specific documentation"""
    __slots__ = ['_o', '_p', '_q', '_r', '_s']
    
    def __init__(self, o = 1, p = 0, q = 0, r = 1, s = 1):
        """o, p, q, r, s MUST be integer values, or types convertible to integers"""
        self._o = int(o)    #n(0)
        self._p = int(p)    #n(1)
        self._q = int(q)    #n(2)
        self._r = int(r)    #coefficient of first term, r * f(n-2)
        self._s = int(s)    #coefficient of second term, s * f(n-3)
        
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
            return self._o
        if n == 1:
            return self._p
        if n == 2:
            return self._q

        return self._r * self.element(n - 2) + self._s * self.element(n - 3)
    
    #@timeCall    
    def elementIt(self, n):
        """returns value for element N in the series as an integer"""
        #assert type(n) is IntType
        isNegThrow(n)
        
        if n == 0:
            return self._o
        elif n == 1:
            return self._p
        elif n == 2:
            return self._q
        
        f1 = self._q
        f2 = self._p    #first element f(n - 2)
        f3 = self._o     #second element f(n - 3)
        
        ret = 0
        
        for i in range(2, n):
            #t = f3   #v stores previous value
            
            ret = self._r * f2 + self._s * f3
            f3 = f2 #prev stores what will be previous value on next iteration
            f2 = f1
            f1 = ret
            
        return ret

    def __str__(self):
        return 'o: {O},\np: {P},\nq: {Q},\nr: {R},\ns: {S}'.format(O=str(self._o),P=str(self._p), Q=str(self._q),R=str(self._r), S=str(self._s))

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
                    
                if not Padovan._isEqual(d[k[i]], d[k[j]], n):
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
                    
                if not Padovan._isEqualIt(d[k[i]], d[k[j]], n):
                    return False
                
        return True
    
    #@staticmethod
    #def getNameSeries():
        """returns all familiar Named Horadam Series"""
        # return T = [
        # ]
    #@timeCall
    @staticmethod
    def builtins():
        def _dictGen(extended = False):#**kwargs): #start = 0, stop = 2)
            """generates all fundamental Padovan Series from either [10011-22222] || [10011-99999]"""
            ret = {}
            s = 10 if extended else 3
            
            o = {'start':0,'stop':s}
            p = {'start':0,'stop':s}
            q = {'start':0,'stop':s}
            r = {'start':1,'stop':s}   #r = {'start':-9,'stop':10}
            s = {'start':1,'stop':s}   #s = {'start':-9,'stop':10}
            #inc = 1
            
            for a in range(q['start'], q['stop']):
                for b in range(p['start'], p['stop']):
                    for c in range(1 if (a == 0 or b == 0) else o['start'], o['stop']):
                        #
                        for d in range(r['start'], r['stop']):
                            #if c == 0 and b == 0 and a == 0
                            if d == 0:
                                continue
                                
                            for e in range(s['start'], s['stop']):
                                if e == 0:
                                    continue
                                k = str(c) + str(b) + str(a) + str(d) + str(e)
                                v = Padovan(c,b,a,d,e)
                                
                                #assert k not in d.keys()
                                #print(k)
                                #print(v)
                                ret[k] = v
                            
                            #print()
            return ret
        
        ret = _dictGen()
        #assert(Horadam.validate(ret))
        return ret
    
    #@timeCall
    @staticmethod
    def test(n = 20):
        p = Padovan.builtins()
        
        #Padovan.validate(p)
        
        c = 0
        
        print('****')
        print('Padovan Built-in Sequences')
        print('****')
        
        i = p.items()
        
        for k, v in i:
            print("Recursive Series {S}".format(S= k))
            print(v.series(n))
            c += 1
        
        for k, v in i:
            print("Iterative Series {S}".format(S= k))
            print(v.seriesIt(n))
            
        # print('series count: {C}'.format(C=c))
        
        # print('****')
        # print('Named Sequences')
        
        # c = 10

        # #@timeCall
        # def r(cls):
            # print(cls.__name__ + ' series:')
            # print(cls.series(c))
            # print('')
            
        # def it(cls):
            # print(cls.__name__ + ' series:')
            # print(cls.seriesIt(c))
            # print('')
        
        # #series types
        # T = [
            #Perrin
            #Perrin.Squared
        # ]
        
        #@timeCall
        # def rec():
        
        #@timeCall
        # def it():

        #
        # print('****')
        # print('recursive')
       
        # for t in T:
            # r(t)

        # print('****')
        # print('iterative')
        
        # for t in T:
            # it(t)
            
        # print('****')
        
##@class Perrin
#series [A001608](https://oeis.org/A001608)
#
class Perrin(Base):
    P = Padovan(3,0,2)
    
    @classmethod
    def element(cls, n, unbound = False):
        return cls.P.element(n, unbound)
    
    @classmethod
    def elementIt(cls, n, unbound = False):
        return cls.P.elementIt(n, unbound)
     
    # ## @class Squared
    #series [A192932](https://oeis.org/A192932)
    #class Squared(Base):
 