## @package integerSequence
# @author Tyler R. Drury
# @date June 2016
# @copyright Tyler R. Drury, All Rights Reserved
# @brief Module for the Abstract Base Class for Integer Sequence
#

#print('importing numeric sequence library')
from abc import ABCMeta, abstractmethod
#typedef exception as E
#from types import IntType  #types only available in 3.5+
#

##@brief throws an exception if @a n is less than zero
#@throw @c ValueError
def isNegativeThrow(n):
    """ensure type of n is of IntType,
    raise an exception if less than zero"""
    #assert type(n) is IntType
    
    if n < 0:
        raise ValueError('invalid value of argument n with value ({N}, value must be greater than or equall to 0)'.format(N=n))

##@brief if @a unbound is @c True, throws a @c ValueError if @a n exceeds @a maxN or is less than 0
def inRange(n, maxN, unbound = False):
    """
    unbound-if true function will return an arbitrary length integer,
        if false, constrains return values up to the maximum for a C unsigned 32 bit integer
    """
    isNegativeThrow(n)
        
    if not unbound:
        if n > maxN:
            raise ValueError('invalid value of argument n with value:{N}, value can not be greater than {MAX}, return would exceed maximum allowable value of 4294967295. Enforcing C 32 bit unsigned integer return values'.format(N=n, MAX=maxN))

            
#class IntegerSequenceBase(metaclass=ABCMeta):
    #"""abstract base class for numeric sequences which can be calculated using a single method,
    # can be overridden for use with either recursive, iterative or tail recursive algorithms
    #"""
    # # #static interface to be overridden by derived classes
    # # def __new__(cls, *args, **kwargs):
        # # raise NotImplementedError('static interface can not be instantiated')
        
    # # def __init__(self):
        # # raise NotImplementedError('static interface can not be instantiated')
    # # #
    # # @classmethod
    # # @abstractmethod
    # # def element(cls, n, unbound = False):
        # # """returns a discrete value of N to be overridden by inheriting classes"""
        # # raise NotImplementedError('function not implemented')
        # # #pass
        
    # # #generic generator for series with N number of elements
    # # @classmethod
    # # def _generator(cls, n):
        
        # # #try:
            # # #convert any not integer type to an integer
            # # #n = n if type n is IntType else int(n)
        # # isNegativeThrow(n)
        
        # # for i in range(n):
            # # yield cls.element(i)
        
        # # #except as e:
            # # #print(e.error)
        
    # # @classmethod
    # # def _list(cls, n):
        # # #assert type(n) is IntType
        # # #print("_gen of class:{c}, n:{var}".format(c=cls, var=n))
        # # #print('in gen')
        
        # # return [f for f in cls._generator(n)]
    
    # # @classmethod
    # # def _tuple(cls, n):
        # # return tuple(f for f in cls._generator(n))
    # # #
    # # #public methods
    # # #
    # # #@timeCall
    # # @classmethod
    # # def series(cls, n):
        # # return cls._tuple(n)
        
        
##@class IntegerSequenceBase NumericSequence.py
#@brief abstract base class for numeric sequences
#
#class RecursiveIterativeBase(metaclass=ABCMeta):
    # """abstract base class for numeric sequences which can be calculated both recursively or iteratively"""
class IntegerSequenceBase(metaclass=ABCMeta):
    """abstract base class for numeric sequences"""
    #static interface to be overridden by derived classes
    def __new__(cls, *args, **kwargs):
        raise NotImplementedError('static interface can not be instantiated')
        
    def __init__(self):
        raise NotImplementedError('static interface can not be instantiated')
    
    # ##overloading [] to retrieve an element at in the series at the specified index I, do not work for ABCMeta
    # @classmethod
    # def __getitem__(cls, index):
        # return cls.elementIt(index)
    #
    #Recursive Functions
    #
    @classmethod
    @abstractmethod
    def element(cls, n, unbound = False):
        """returns a discrete value of N"""
        raise NotImplementedError('function not implemented')
        #pass
    
    # @classmethod
    # def __call__(cls, N, unbound = False):
        #Fibonaci(10) returns the 10th fibonacci number
        # return cls.elementIt(N, unbound)
        
    # @classmethod    
    # def out(cls, arg):
        # print("executing class_foo({c},{a})".format(c=cls,a=arg))
    @classmethod
    def _generator(cls, n):
        
        #try:
            #convert any not integer type to an integer
            #n = n if type n is IntType else int(n)
        isNegativeThrow(n)
        
        for i in range(n):
            yield cls.element(i)
        
        #except as e:
            #print(e.error)
        
    @classmethod
    def _list(cls, n):
        #assert type(n) is IntType
        #print("_gen of class:{c}, n:{var}".format(c=cls, var=n))
        #print('in gen')
        
        return [f for f in cls._generator(n)]
    
    @classmethod
    def _tuple(cls, n):
        return tuple(f for f in cls._generator(n))
    #
    #public methods
    #
    #@timeCall
    @classmethod
    def series(cls, n):
        return cls._tuple(n)
    #
    #Iterative functions
    #
    @classmethod
    @abstractmethod
    def elementIt(cls, n, unbound = False):
        """returns a discrete value of N"""
        raise NotImplementedError('function not implemented')
        
    @classmethod
    def _generatorIt(cls, n):
        
        #try:
            #convert any not integer type to an integer
            #n = n if type n is IntType else int(n)
        isNegativeThrow(n)
        
        for i in range(n):
            yield cls.elementIt(i)
        
        #except as e:
            #print(e.error)
        
    @classmethod
    def _listIt(cls, n):
        #assert type(n) is IntType
        #print("_gen of class:{c}, n:{var}".format(c=cls, var=n))
        #print('in gen')
        
        return [f for f in cls._generatorIt(n)]
    
    @classmethod
    def _tupleIt(cls, n):
        return tuple(f for f in cls._generatorIt(n))
    #
    #public methods
    #
    #@timeCall
    @classmethod
    def seriesIt(cls, n):
        return cls._tupleIt(n)
        
        
    #@classmethod
    #def _set(cls, n):
    #    """arg n: number of elemenets in the sequence
    #    lists can have repeated values however,
    #    sets only contain unique sequences of values
    #    therefor it is convenient to construct sets aswell
    #    for additional functionality"""

    #    return set(f for f in cls._generator(n))     #[f for f in genFib(n)])
    #
    #@classmethod
    #def _frozenSet(cls, n):
    #    return frozenset(f for f in cls._generator(n))
    #
    # @sclassmethod
    #def set(cls, n):
        """creates 1:1 mapping between N : val(N)
        NOTE: there is no aurentee values will be in numeric order"""
        #s = cls.series(n)
        #return {i : cls.element(i) for i in range(n)}
    
    
    
# def intSeqIter(f):
    # #function decorator to ensure args n, unbound =False are applied to function
    # def r(n, unbound = False):
        # # isNegativeThrow(n)
        
        # f(n)
        
    # return r

    
# # def even(n, incZero=False):
    # #for i in range(2, n, 2):
    
# # def even(n, incZero=False):
    # #for i in range(1, n, 2):
    

#@intSeqIter
# def LazyCaterer(n):
    # #as a decorated iterator
    # yield ((n * (n + 1)) >> 1) + 1 if n > 0 else 1

# def Cake(n, unbound = False):
    # #isNegativeThrow(n)
    # yield Cake(n - 1,unbound) + LazyCaterer(n - 1,unbound) if n > 0 else 1
    
# def Pronic(n, unbound = False):
    # """#a(n) = n*(n+1) or n^2 + n"""
    # #inRange(n, , unbound)
    # if n == 0:
        # yield 0
    # elif n == 1:
        # yield 2
        
    # yield n ** 2 + n


# def Catalan(n, unbound = False):
    # inRange(n, 11, unbound)
    
    # D = fact.element(n) * fact.element(n + 1)
    
    # yield fact.element(2 * n) // D
    
# def Collatz(N, unbound = False):
    # #inRange(N, , unbound)
        
    # if N == 0:
        # yield 0

    # r = 0
    # #if N is odd  N & 0x00000001 will be true, else is even and is 0
    # if N & 1 == 0:
        # r = N // 2   #performs integer division rounding down, note: bitshift is faster, >> 1
    # else:
        # r = (N * 3 + 1) // 2    #>> 1
    
    # #print(r)
    
    # yield r

##@class LazyCaterer
#series [A000129](https://oeis.org/A000129)
#
class LazyCaterer:
    @classmethod
    def element(cls, n, unbound = False):
        #inRange(n,,unbound)
        isNegativeThrow(n)
        
        return ((n * (n + 1)) >> 1) + 1 if n > 0 else 1

##@class Cake
#series [A000125](https://oeis.org/A000125)
#      
class Cake:
    @classmethod
    def element(cls, n, unbound = False):
        #isNegativeThrow(n)
        return Cake.element(n - 1) + LazyCaterer.element(n - 1) if n > 0 else 1
    
##@class Pronic
#series [A002378](https://oeis.org/A002378)
#
class Pronic:
    """#a(n) = n*(n+1) or n^2 + n"""
    @classmethod
    def element(cls, n, unbound = False):
        #inRange(n, , unbound)
        if n == 0:
            return 0
        elif n == 1:
            return 2
            
        return n ** 2 + n
        
##@class Catalan
#series [A000108](https://oeis.org/A000108)
#
class Catalan:
    @classmethod
    def element(cls, n, unbound = False):
        inRange(n, 11, unbound)
        
        D = fact.element(n) * fact.element(n + 1)
        
        return fact.element(2 * n) // D

##@class Collatz
#@brief series [A014682](https://oeis.org/A014682)
#
class Collatz:
    @classmethod
    def element(cls, N, unbound = False):
        #inRange(N, , unbound)
        
        if N == 0:
            return 0

        r = 0
        #if N is odd  N & 0x00000001 will be true, else is even and is 0
        if N & 1 == 0:
            r = N // 2   #performs integer division rounding down, bitshift is faster, >> 1
        else:
            r = (N * 3 + 1) // 2    #>> 1
        
        #print(r)
        
        return r
        
    # class Inverse(Base):
        # """where the Collatz equation is f(N) =  N / 2 if N is EVEN, otherwise 3N + 1 / 2
        # this sequence returns where the Collatz equation isf(N) =  N / 2 if N is ODD, otherwise 3N + 1 / 2
        # """
        # @classmethod
        # def element(cls, N, unbound = False):
            # #inRange(N, , unbound)
            
            # if N == 0:
                # return 0

            # r = 0
            # #if N is odd  N & 0x00000001 will be true, else is even and is 0
            # if N & 1 == 1:
                # r = N // 2   #performs integer division rounding down, bitshift is faster, >> 1
            # else:
                # r = (N * 3 + 1) // 2    #>> 1
            
            # #print(r)
            
            # return r