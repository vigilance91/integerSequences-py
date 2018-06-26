##@package integerSequence
#
#@file
#@author Tyler R. Drury
#@copyright 2017-present, Tyler R. Drury. All Rights Reserved
#@brief package initialization file
#

#
__author__ = 'Tyler R. Drury'
__copyright__ = 'Copyright (C) 2017-present, Tyler R. Drury. All Rights Reserved'
__license__ = 'Apache 2.0'
#
__maintainer__ = 'Tyler R. Drury'
__email__ = 'that_canadianguy@hotmail.com'
#
__version__ = '0.1.1'
__status__ = 'Development'
#
# __credits__ = [
# ]
#
from .integerSequence import *
from .factorial import *
from .prime import *
from .horadam import *
from .polygonal import *
from .polyhedral import *
from .pellLucas import *
from .hofstadter import *
from .padovan import *
#
__all__ = [
    'integerSequence',
    'prime',
    'factorial',
    'polygonal',
    'polyhedral',
    'horadam',
    'pellLucas',
    'hofstadter',
    'padovan'
]