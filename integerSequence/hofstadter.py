##@package hofstadter
#
#@file
#@author Tyler R. Drury
#@copyright 2017 Tyler R. Drury, All Rights Reserved
#@brief Hofstadter Series
#

#
#print('importing Hofstadter Sequence library')
#
from abc import ABCMeta, abstractmethod
#
#from integerSequence import IntegerSequenceBase as Base
from integerSequence import inRange as inRange
from integerSequence import isNegativeThrow as isNegThrow

##@class HofstadterBase hofstadter.py
#@brief abstract base class for Hofstadter sequences, equations do not allow for iterative approach
#
class HofstadterBase(metaclass=ABCMeta):
    """abstract base class for Hofstadter Sequences"""
    #static interface to be overridden by derived classes
    def __new__(cls, *args, **kwargs):
        raise NotImplementedError('Abstract Base Class for static interface can not be instantiated')
        
    def __init__(self):
        raise NotImplementedError('Abstract Base Class for static interface can not be instantiated')
    #
    @classmethod
    @abstractmethod
    def element(cls, N, unbound = False):
        """returns a discrete value of N"""
        raise NotImplementedError('function not implemented')
    
    # @classmethod    
    # def out(cls, arg):
        # print("executing class_foo({c},{a})".format(c=cls,a=arg))
    @classmethod
    def _generator(cls, N):
        
        #try:
            #convert any not integer type to an integer
            #N = N if type N is IntType else int(N)
        isNegThrow(N)
        
        for i in range(N):
            yield cls.element(i)
        
        #except as e:
            #print(e.error)
        
    @classmethod
    def _list(cls, N):
        #assert type(N) is IntType
        #print("_gen of class:{c}, N:{var}".format(c=cls, var=N))
        #print('in gen')
        
        return [f for f in cls._generator(N)]
    
    @classmethod
    def _tuple(cls, N):
        return tuple(f for f in cls._generator(N))
    #
    #public methods
    #
    #@timeCall
    @classmethod
    def series(cls, N):
        return cls._tuple(N)

##@class Conway
#series [A004001](http://oeis.org/A004001)
#
class Conway(HofstadterBase):
    @classmethod
    def element(cls, N, unbound = False):
        #if N <= 0:
            #raise E("illegal element, series does not start will an element of N = 0")
        #inRange(N, , unbound)
        
        if N == 1 or N == 2:
            return 1
        
        next = cls.element(N - 1)

        return cls.element(next) + cls.element(N - next)
        
    @classmethod
    def _generator(cls, N):
        
        #try:
            #convert any not integer type to an integer
            #N = N if type N is IntType else int(N)
        isNegThrow(N)
        
        for i in range(1, N):
            yield cls.element(i)
    
    #class A004074(HofstadterBase):
        #@classmethod
        #def element(cls, N, unbound = False):
            #return 2 * Conway.element(N) - N
        
##@class Chaotic
#series [A055748](http://oeis.org/A055748)
#
class Chaotic(HofstadterBase):
    @classmethod
    def element(cls, N, unbound = False):        
        inRange(N, 251, unbound)
        
        if N == 1 or N == 2:
            return 1

        next = cls.element(N - 1)
        n2Val = cls.element(N - 2)
        
        return cls.element(next) + cls.element(N - n2Val - 1)
        
    @classmethod
    def _generator(cls, N):
        
        #try:
            #convert any not integer type to an integer
            #N = N if type N is IntType else int(N)
        isNegThrow(N)
        
        for i in range(1, N):
            yield cls.element(i)

##@class Q
#series [A005185](https://oeis.org/A005185)
#
class Q(HofstadterBase):
    @classmethod
    def element(cls, N, unbound = False):        
        #inRange(N, 251, unbound)
        
        if N == 1 or N == 2:
            return 1

        next = cls.element(N - cls.element(N - 1))
        n2Val = cls.element(N - cls.element(N - 2))
        
        return next + n2Val
        
    @classmethod
    def _generator(cls, N):
        
        #try:
            #convert any not integer type to an integer
            #N = N if type N is IntType else int(N)
        isNegThrow(N)
        
        for i in range(1, N):
            yield cls.element(i)
            
    ##
    #series [A278066](https://oeis.org/A278066)
    #class A278066   
        
##@class G
#series [A005206](https://oeis.org/A005206)
#
class G(HofstadterBase):
    @classmethod
    def element(cls, N, unbound = False):
       #static_assert(N <= 249, "");
        inRange(N, 249, unbound)   #recursive type context too complex in C, could potentially blow stack
        
        if N == 0:
            return 0

        val = cls.element(N - 1)

        return N - cls.element(val)

##@class H
#series [A005206](https://oeis.org/A005206)
#
class H(HofstadterBase):
    @classmethod
    def element(cls, N, unbound = False):
        #f(N) = N - h(h(h(N-1)))
        inRange(N, 166, unbound)
    
        if N == 0:
            return 0

        val = cls.element(N - 1)
        h0 = cls.element(val)

        return N - cls.element(h0)

##@class Male
#series [A005379](https://oeis.org/A005379)
#
class Male(HofstadterBase):
    @classmethod
    def element(cls, N, unbound = False):
        inRange(N, 249, unbound)
        
        if N == 0:
            return 0

        m = cls.element(N - 1)

        return N - Female.element(m)

##@class Female
#series [A005378](https://oeis.org/A005378)
#
class Female(HofstadterBase):
    @classmethod
    def element(cls, N, unbound = False):
        inRange(N, 249, unbound)    #recursive type context too complex for C(++)
        
        if N == 0:
           return 1

        f = cls.element(N - 1)

        return N - Male.element(f)
    
#

def HofstadterTest(N = 20):
    def p(cls):
        print('****')
        print(cls.__name__ + ' series:')
        print(cls.series(N))
        
    T = [
        Chaotic,    #++
        Conway, #++
        Q,  #++
        G,  #++
        H,  #++
        Male,   #++
        Female  #++
    ]
    print('****')
    print('Hofstadter Series Test')
    print('****')
    print('')
    # print('chaotic')
    # for i in range(1, 20):
        # print(Chaotic.element(i))
    
    # print('conway')
    # for i in range(1, 20):
        # print(Conway.element(i))
        
    for t in T:
        p(t)
        
