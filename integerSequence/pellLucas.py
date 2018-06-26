##@file
#@author Tyler R. Drury
#@copyright 2017 Tyler R. Drury, All Rights Reserved
#

#
#module containing sequences which utilize both Pell and Lucas Numbers
#
from integerSequence import IntegerSequenceBase as Base
from integerSequence import isNegativeThrow as isNegThrow
#
from integerSequence import Pell as pell
#from pellCompanion import Recursive as pellCompR
from integerSequence import Lucas as lucas
#
class Recursive:
    #_l = lucasR.series
    #_p = pellR.series
    @staticmethod
    def sum(N):
        """http://oeis.org/A060405
        f(n) = L(n) + P(n)
        """
        for n in range(0, N):
            yield lucas.element(n) + pell.element(n)
    
    @staticmethod
    def difLP(N):
        """http://oeis.org/A060405
        f(n) = L(n) - P(n)"""
        for n in range(0, N):
            yield lucas.element(n) - pell.element(n)
    
    @staticmethod
    def difPL(N):
        """http://oeis.org/A228748
        Difference between Pell and Lucas series
        f(n) = P(n) - L(n)
        NOTE: some values are negative!"""
        for n in range(0, N):
            yield pell.element(n) - lucas.element(n)
    
    @staticmethod
    def product(N):
        """http://oeis.org/A226638
        f(n) = L(n) * P(n)"""
        
        #if not unbound:
            #if N > 13:
                #raise InvalidArg
            
        for n in range(0, N):
            yield lucas.element(n) * pell.element(n)
    
    # @staticmethod
    # def productCompanion(N):
        # """https://oeis.org/A085293
        # f(n) = L(n) * P(n) where P(n) is the Pell Companion Series A002203"""
        # #if N > 12:
            # #raise InvalidArg
            
        # for n in range(0, N):
            # yield lucasR.element(n) * pellR.element(n)
    
    def pellAtLucas(N, unbound = False):
        #if not unbound:
            #if N > 7:
                #raise InvalidArg
            
        for n in range(0, N):
            yield pell.element(lucasR.element(n))
            
    def lucasAtPell(N):
        #if not unbound:
            #if N > 6:
                #raise InvalidArg
            
        for n in range(0, N):
            yield lucas.element(pell.element(n))
    
    #@timeCall
    @staticmethod
    def test():
        N = 15
        print('Pell-Lucas Series')
        print('sum')
        print([x for x in Recursive.sum(N)])
        print('L - P')
        print([x for x in Recursive.difLP(N)])
        print('P - L')
        print([x for x in Recursive.difPL(N)])
        print('product')
        print([x for x in Recursive.product(N)])
        print('P(L(N))')
        print([x for x in Recursive.pellAtLucas(7)])
        print('L(P(N))')
        print([x for x in Recursive.lucasAtPell(6)])
# #TODO

    
# lucasAtPellIt = lambda n:
    # lucasIt.element(pellIt.element(n))
    

    
# pellAtLucasIt = lambda n:
    # pellIt.element(lucasIt.element(n))