##@file
#@author Tyler R. Drury
#@copyright 2017 Tyler R. Drury, All Rights Reserved
#@brief module for calculating primes numbers and relates series

#
#from timer import timeCall

##@todo A002110		Primorial numbers (first definition): product of first n primes.
##@todo A034386		Primorial numbers (second definition): n# = product of primes <= n. the product of two (not necessarily distinct) primes.
##@todo A014612		Numbers that are the product of exactly three (not necessarily distinct) primes.
##@todo A002385		Palindromic primes: prime numbers whose decimal expansion is a palindrome. 
##@todo A001043		Numbers that are the sum of 2 successive primes.
##@todo A002981		Numbers n such that n! + 1 is prime.

from math import sqrt
#
#@timeCall
def getPrimes(max, incOne = True):
    """this implementation includes 1 as the first prime number
    although this is technically incorrect, for the purposes
    of the hand evaluation algorithm, it is necessary"""
   
    class Check:
        def __init__(self, i = 0, remove = False):
            #asert(i >= 0)
           self._i = i
           self._remove = remove

        def __eq__(self, other):
           return self._i == other._i and self._remove == other._remove
           
        def __str__(self):
            return '_i:{I}, _remove:{R}\n'.format(I=self._i, R=self._remove)
            
        def __repr__(self):
            """defined for print to output something useful instead of object's memory address"""
            return self.__str__()

    """implements the Euler's sieve algorithm
    to get all prime numbers upto and including max(if prime)"""
    
    max = int(max)
    
    if max < 1:
        raise ValueError("no prime numbers less than 1")

    S = int(sqrt(float(max)))   #square root of max, cast to an integer
    #print('sqrt of max:{M}'.format(M=S))
    
    #list = ()  #
    primes = list()    #

    if incOne:
        primes.append(1)

    if max > 2:
        #used to filter through results
        #without modifying either containers
       
        sieve = list()
    
        sieve.append(Check(2))

        #early elimination of all multiples of 2
        # def gen():
            # for i in range(3, max + 1, 2):
                # yield Check(i)
            
        #sieve.append(x for x in gen(max))
        
        for i in range(3, max + 1, 2):
            sieve.append(Check(i))
        
        #if max <= 13:
            #for c in sieve:
                #primes.append(c._i)
        #else:
        
        startIndex = 1
        l = len(sieve)
        #print('values to be filtered:')
        #print(sieve)
        #print('max:{M}, sqrt max:{SM}'.format(M=max, SM=S))
        
        while sieve[startIndex]._i <= S:
            #print(sieve[startIndex]._i)
            
            for fIndex in range(1, l):
                #
                #print(sieve[fIndex]._i)
                #
                res = sieve[startIndex]._i * sieve[fIndex]._i
                
                if res < max:
                    #if i^2 < max, then value is prime
                    # print('calculating potential prime:{P}'.format(P=res))
                    #print('{S} * {F} = {R}'.format(R=res, S=sieve[startIndex]._i, F=sieve[fIndex]._i))
                    C = Check(res)

                    for i in range(0,l):
                        #print(sieve[i]._i)
                        if C == sieve[i]:
                            #if sieve[i]._remove == False:
                            #c = sieve[i]
                            #print('removing element:{E} from sieve'.format(E=c))
                            sieve[i]._remove = True
                            #break

               # #cUInt v = v[i];

               # #cUInt s = *start;

               # #if v != 2 and v % s == 0:
               # #    Iter next(it);
               # #    next--;
               # #    erase(it);
               # #    it = next;

            #fIndex = 0
            startIndex += 1

        #print(sieve)
        
        # def filter():
            # for e in sieve:
                # if e._remove == False:
                    # #print('adding prime number:{N}'.format(N=e._i))
                    # yield e._i
                    
        #primes.append(x for x in filter())
        
        for e in sieve:
            if e._remove == False:
                #print('adding prime number:{N}'.format(N=e._i))
                primes.append(e._i)

    else:
       primes.append(2)

    #tuples are immutable sequences and the return value shouldn't be modified
    return tuple(primes)
    
#def getLuckyNumbers(max):
    # """this implementation includes 1 as the first prime number
    # although this is technically incorrect, for the purposes
    # of the hand evaluation algorithm, it is necessary"""
   
    # class Check:
        # def __init__(self, i = 0, remove = False):
            # #asert(i >= 0)
           # self._i = i
           # self._remove = remove

        # def __eq__(self, other):
           # return self._i == other._i and self._remove == other._remove
           
        # def __str__(self):
            # return '_i:{I}, _remove:{R}\n'.format(I=self._i, R=self._remove)
            
        # def __repr__(self):
            # """defined for print to output something useful instead of object's memory address"""
            # return self.__str__()

    # """implements the Euler's sieve algorithm
    # to get all prime numbers upto and including max(if prime)"""
    
    # max = int(max)
    
    # if max < 1:
        # raise ValueError("no lucky numbers less than 1")

    # S = int(sqrt(float(max)))
    # #print('sqrt of max:{M}'.format(M=S))
    
    # lucky = list(x for x in range(max))    #

    # if max > 2:
        # #used to filter through results
        # #without modifying either containers
       
        # sieve = list()
    
        # sieve.append(Check(2))

        # #early elimination of all multiples of 2
        # #for(unsigned i(3); i <= max; i += 2):
        # for i in range(3, max + 1, 2):  
            # sieve.append(Check(i))
        
        # #if max <= 13:
            # #for c in sieve:
                # #primes.append(c._i)
        # #else:
        
        # startIndex = 1
        # l = len(sieve)
        # #print('values to be filtered:')
        # #print(sieve)
        # #print('max:{M}, sqrt max:{SM}'.format(M=max, SM=S))
        
        # while sieve[startIndex]._i <= S:
            # #print(sieve[startIndex]._i)
            
            # for fIndex in range(1, l):
                # #
                # #print(sieve[fIndex]._i)
                # #
                # res = sieve[startIndex]._i * sieve[fIndex]._i
                
                # if res < max:
                    # #if i^2 < max, then value is prime
                    # # print('calculating potential prime:{P}'.format(P=res))
                    # #print('{S} * {F} = {R}'.format(R=res, S=sieve[startIndex]._i, F=sieve[fIndex]._i))
                    # C = Check(res)

                    # for i in range(0,l):
                        # #print(sieve[i]._i)
                        # if C == sieve[i]:
                            # #if sieve[i]._remove == False:
                            # #c = sieve[i]
                            # #print('removing element:{E} from sieve'.format(E=c))
                            # sieve[i]._remove = True
                            # #break

               # # #cUInt v = v[i];

               # # #cUInt s = *start;

               # # #if v != 2 and v % s == 0:
               # # #    Iter next(it);
               # # #    next--;
               # # #    erase(it);
               # # #    it = next;

            # #fIndex = 0
            # startIndex += 1

        # #print(sieve)
        
        # for e in sieve:
            # if e._remove == False:
                # #print('adding prime number:{N}'.format(N=e._i))
                # primes.append(e._i)

    # else:
       # 

    # #tuples are immutable sequences and the return value shouldn't be modified
    # return tuple(lucky)

# @timeCall
# def PrimePi(max):
    # """A000720
    # pi(n), the number of primes <= n. Sometimes called PrimePi(n)"""
    # p = getPrimes(max)
    
    # return len(p)

#def _generator(N, callable):
    #isNegR(N)
    #for n in range 0, N):
        #yield callable(n)
    

# class Doubles:
    # """A014612
    # Numbers that are the product of exactly three (not necessarily distinct) primes"""
    # def _generator(max, unbound = False):
        # p = getPrimes(max)
        # l = len(p)
        # r = range(0, l)
        
        # for i in r:
            # for j in r:
                # yield p[i] * p[j]
                
    # def _list(max, unbound = False):
        # return list(x for x in Doubles._generator(max, unbound))
        
    # def _tuple(max, unbound = False):
        # return tuple(x for x in Doubles._generator(max, unbound))
        
    # def series(max, unbound = False):
        # return Doubles._tuple(max, unbound)

# class Triples:
    # """A014612
    # Numbers that are the product of exactly three (not necessarily distinct) primes"""
    # def _generator(max, unbound = False):
        # p = getPrimes(max)
        # l = len(p)
        # r = range(0, l)
        
        # for i in r:
            # for j in r:
                # for k in r:
                    # yield p[i] * p[j] * p[k]
                
    # def _list(max, unbound = False):
        # return list(x for x in Triples._generator(max, unbound))
        
    # def _tuple(max, unbound = False):
        # return tuple(x for x in Triples._generator(max, unbound))
        
    # def series(max, unbound = False):
        # return Triples._tuple(max, unbound)

#def getFactorialPrimes(N):
    """A002981		Numbers n such that n! + 1 is prime."""
    #5, 23, 719, 5039,
    #f = factorial(N)
    
    #p = getPrimes(f + 1)
    
    
#@timeCall
# class BinaryMersenne(isBase):
    #
    #""" series
    #1,2,4,16,64,1024.4096,65536,262144,4194304
    #"""
    #@classmethod
    # def _list(cls, M, unbound = False):
        # return list(x for x in cls._generator(M, unbound))
    
    #@classmethod
    # def _tuple(cls, M, unbound = False):
        # return tuple(x for x in cls._generator(M, unbound))
    
    #@staticmethod
    # def _generator(M, unbound = False):
    
        # #if not unbound:
            # #if max > 38:
                # #raise ValueError("Can not calculate Mersenne number beyond 38, value would exceed size of 32 unsigned integer".format(M=m))

        # p = getPrimes(M, False)

        # if not unbound:
            # l = len(p)
            # m = 11
            # if l > m:
                # raise ValueError("Can not calculate Mersenne number beyond {MX}, {L} numbers of primes generated, value would exceed size of 32 unsigned integer".format(L=l, MX=m))

        # #print(p)
        
        # for x in p:
            # y = 2 ** (x - 1)
            # #print('{R} = 2 ^ {X} - 1'.format(R=r - 1, X=x))
            # yield y

    #@classmethod
    # def series(M = 31, unbound = False):
        # return cls._tuple(M, unbound)

        
# class Base(metaclass=ABCMeta):
    # #static interface to be overridden by derived classes
    # def __new__(cls, *args, **kwargs):
        # raise NotImplementedError('static interface can not be instantiated')
        
    # def __init__(self):
        # raise NotImplementedError('static interface can not be instantiated')
    # #
    # #Recursive Functions
    # #
    # @classmethod
    # @abstractmethod
    # def element(cls, n, unbound = False):
        # """returns a discrete value of N"""
        # raise NotImplementedError('function not implemented')
        # #pass
    
    # @classmethod
    # def _generator(cls, n):
        
        # #try:
            # #convert any not integer type to an integer
            # #n = n if type n is IntType else int(n)
        # isNegativeThrow(n)
        
        # for i in range(n):
            # yield cls.element(i)
        
        # #except as e:
            # #print(e.error)
        
    # @classmethod
    # def _list(cls, n):
        # #assert type(n) is IntType
        # #print("_gen of class:{c}, n:{var}".format(c=cls, var=n))
        # #print('in gen')
        
        # return [f for f in cls._generator(n)]
    
    # @classmethod
    # def _tuple(cls, n):
        # return tuple(f for f in cls._generator(n))
    # #
    # #public methods
    # #
    # #@timeCall
    # @classmethod
    # def series(cls, n):
        # return cls._tuple(n)
    

##@class Mersenne
#[series](https://oeis.org/A000225)
#
class Mersenne:
    """Mersenne Numbers: f(N) = (2^N) - 1
    NOTE: M(12) = 2147483647 equals max value of 32 bit unsigned int in C++"""
    def _list(N, unbound = False):
        return list(x for x in Mersenne._generator(N, unbound))
        
    def _tuple(N, unbound = False):
        return tuple(x for x in Mersenne._generator(N, unbound))
        
    def _generator(N, unbound = False):
        inRange(N, 31, unbound)

        for x in range(0, N):
            r = 2 ** x
            #print('{R} = 2 ^ {X} - 1'.format(R=r - 1, X=x))
            yield r - 1

    def series(M = 31, unbound = False):
        return Mersenne._tuple(M, unbound)
    
##@class Primorial
#
#
# class Primorial(Base):
    # @staticmethod
    # def element(max, unbound = False):
        # #returns the product of all primes up to max
        # p = getPrimes(max)
        
        # r = 1
        
        # for n in p:
            # r *= n
            
        # return r
        
# ##@class MersennePrimes
# #@brief [series](https://oeis.org/A000668)
# #
# class MersennePrimes:
    # """Mersenne Primes:
    # f(n) = (2^p) - 1, where both p and f(n) is prime.
    # """
    # def _list(M, unbound = False):
        # return list(x for x in MersennePrimes._generator(M, unbound))
        
    # def _tuple(M, unbound = False):
        # return tuple(x for x in MersennePrimes._generator(M, unbound))
        
    # def _generator(M, unbound = False):
    
        # #if not unbound:
            # #if max > 38:
                # #raise ValueError("Can not calculate Mersenne number beyond 38, value would exceed size of 32 unsigned integer".format(M=m))

        # p = getPrimes(M, False)

        # if not unbound:
            # l = len(p)
            # m = 8
            # if l > m:
                # raise ValueError("Can not calculate Mersenne number beyond {MX}, {L} numbers of primes generated, value would exceed size of 32 unsigned integer".format(L=l, MX=m))

        # print(p)
        
        # for x in p:
            # r = 2 ** x
            # #print('{R} = 2 ^ {X} - 1'.format(R=r - 1, X=x))
            # yield r - 1

    # def series(M = 31, unbound = False):
        # return MersennePrimes._tuple(M, unbound)
 
 
    
# ##@class MersennePrimeIndices
# #@brief [series](https://oeis.org/A001348)
# #
# class MersennePrimeIndices:
    # """Mersenne Numbers whose indices are Prime:
    # f(n) = (2^p) - 1, where p is the n-th prime.
    # NOTE: M(12) = 2147483647 equals max value of 32 bit unsigned int in C++"""
    # def _list(M, unbound = False):
        # return list(x for x in MersennePrimeIndices._generator(M, unbound))
        
    # def _tuple(M, unbound = False):
        # return tuple(x for x in MersennePrimeIndices._generator(M, unbound))
        
    # def _generator(M, unbound = False):
    
        # #if not unbound:
            # #if max > 38:
                # #raise ValueError("Can not calculate Mersenne number beyond 38, value would exceed size of 32 unsigned integer".format(M=m))

        # p = getPrimes(M, False)

        # if not unbound:
            # l = len(p)
            # m = 11
            # if l > m:
                # raise ValueError("Can not calculate Mersenne number beyond {MX}, {L} numbers of primes generated, value would exceed size of 32 unsigned integer".format(L=l, MX=m))

        # print(p)
        
        # for x in p:
            # r = 2 ** x
            # #print('{R} = 2 ^ {X} - 1'.format(R=r - 1, X=x))
            # yield r - 1

    # def series(M = 31, unbound = False):
        # return MersennePrimeIndices._tuple(M, unbound)
 
 
# ##@class
#[series](https://oeis.org/A061286) 
#
# class smallestDivisor:
    # """Smallest integer for which the number of divisors is the n-th prime
    # NOTE: M(12) = 2147483647 equals max value of 32 bit unsigned int in C++"""
    # def _list(M, unbound = False):
        # return list(x for x in Mersenne._generator(M, unbound))
        
    # def _tuple(M, unbound = False):
        # return tuple(x for x in Mersenne._generator(M, unbound))
        
    # def _generator(M, unbound = False):
    
        # #if not unbound:
            # #if max > 38:
                # #raise ValueError("Can not calculate Mersenne number beyond 38, value would exceed size of 32 unsigned integer".format(M=m))

        # p = getPrimes(M)

        # if not unbound:
            # l = len(p)
            # m = 11
            # if l > m:
                # raise ValueError("Can not calculate Mersenne number beyond {MX}, {L} numbers of primes generated, value would exceed size of 32 unsigned integer".format(L=l, MX=m))

        # print(p)
        
        # for x in p:
            # r = 2 ** (x - 1 if x is not 0 else 0)
            # #print('{R} = 2 ^ {X} - 1'.format(R=r - 1, X=x))
            # yield r

    # def series(M = 30, unbound = False):
        # return Mersenne._tuple(M, unbound)

# ##@class PerrinPrimes
# series [A112881](https://oeis.org/A112881)
#
#class PerrinPrimes:


#@timeCall
def primeTest():
    """first primes under 10, 000"""
    # print('****')
    # print('Prime Numbers')
    # p = getPrimes(1000)
    # print(p)
    print('****')
    print('Mersenne Numbers')
    print(Mersenne.series())
    # print('Products of Two primes')
    # print(Doubles.series(11))
    # print('Products of Three primes')
    # print(Triples.series(11))
