# Python Integer Sequences
# Copyright (C) June 2018-present, Tyler R. Drury. All Rights Reserved.

Developed and maintained by Tyler R. Drury,


----

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/vigilance91/integerSequences-py/graphs/commit-activity)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![PyPI version fury.io](https://badge.fury.io/py/ansicolortags.svg)](https://pypi.python.org/project/integerSequence/)
[![PyPI download total](https://img.shields.io/pypi/dt/ansicolortags.svg)](https://pypi.org/project/integerSequence/)

[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/vigilance91/integerSequences-py.svg)](http://isitmaintained.com/project/vigilance91/integerSequences-py "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/vigilance91/integerSequences-py.svg)](http://isitmaintained.com/project/vigilance91/integerSequences-py "Percentage of issues still open")

----

This project is a pure python package,
allowing users to conveniently represent and generate common integer sequences, including:

* Factorials
* Prime numbers
* Catalan numbers
* Horadam numbers
* Padovan numbers
* Hofstadter numbers
* Collatz numbers
* Pronic numbers
* Lazy Caterer and Cake Numbers
* Geometric numbers(polygonal, polyhedral)

---

## Target Platform

Python 3.6, 64-bit

---

## Use

~~~~
from integerSequence import Horadam
from integerSequence import Fibonacci as fib
from integerSequence import getPrimes

p = getPrimes(1000) #calculate all primes up to 1000
print(p)

h = Horadam(2,3,1,2)    #unnamed Horadam sequence
s = h.series(10)
print(s)

s = fib.series(20)
print(s)

~~~~

---

## Download

Latest compiled python files/wheels can be found on the Python Package Index [here](),
or developers can find the current Source Code at the GitHub repo [here](),
if you wish to contribute.
    
---

## Primary Developer

* Tyler R. Drury


## Additional Contributors



---

## Related Projects

Similar or related projects for various platforms can also be found here

### Libraries

* [IntegerSequences-cpp]()  a compiled C/C++ library for generating common sequences of integers
* [IntegerSequences-js]()  a Javascript library for generating common sequences of integers, for front-end web browsers use
* [IntegerSequences-php]()  a PHP library for generating common sequences of integers, for back-end server use


---

## Additional Online References and Resources

* The Official [integerSequences-py Reference]()
* The [Online Encyclopaedia of Integer Sequences](https://oeis.org)

---

## Acknowledgements

* [Neil Sloane](http://neilsloane.com/), founder of the Online Encyclopaedia of Integer Sequences

---