##@file
#@author Tyler R. Drury
#@copyright 2017 Tyler R. Drury, All Rights Reserved
#

#
from integerSequence import IntegerSequenceBase as Base
from integerSequence import inRange as inRange
#
##@class Factorial
#series [A000142](https://oeis.org/A000142)
#
class Factorial(Base):
    
    @classmethod
    def element(cls, n, unbound = False):
        """recursive function which returns the value of !n"""
        #assert type(n) is IntType, 'arg n must be a non-negative integer value'
        
        inRange(n, 20, unbound)
        
        if n == 0 or n == 1:
           return 1

        return n * cls.element(n - 1)
        
    @classmethod
    def elementIt(cls, n, unbound = False):
        """iterative function which returns the value of !n"""
        #assert type(n) is IntType, 'arg n must be a non-negative integer value'
        inRange(n, 20, unbound)
        
        if n == 0 or n == 1:
            return 1
            
        ret = 2
        
        for i in range(2, n):
            #print(ret)
            #print(i)
            ret *= (i + 1)
        
        return ret
    
    #class Prime
    
    #@class Double
    #double factorial N!!, series [A006882](https://oeis.org/A006882)
    #
    #class Double:
        # @classmethod
        # def elementIt(cls, n, unbound = False):
            #inRange(n, 16)
            #return Factorial.element(Factorial.element(n))
            
        # @classmethod
        # def elementIt(cls, n, unbound = False):
            #inRange(n, 16)
            #return Factorial.elementIt(factorial.elementIt(n))

#def _set(n):
#    """arg n: number of elemenets in the sequence
#    lists can have repeated values however,
#    sets only contain unique sequences of values
#    therefor it is convenient to construct sets aswell
#    for additional functionality"""

#    return set(_list(n))     #[f for f in genFib(n)])
##
#def _frozenSet(n):
#    return frozenset(_list(n))