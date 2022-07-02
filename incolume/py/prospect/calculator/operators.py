from decimal import DivisionByZero
from functools import reduce
from typing import Iterable
import logging
from operator import sub, mul
from functools import reduce


logging.basicConfig(level=logging.DEBUG)


def somar(*args, **kwargs):
    logging.debug(f'{args} {kwargs}')
    lista = list()
    if not args and not kwargs:
        return 0

    try:
        if len(args) == 1 and isinstance(args[0], Iterable):
            lista = (0. if x is None else float(x) for x in args[0])
        else:
            lista = (0. if x is None else float(x) for x in args)
        return sum(lista)
    except ValueError as e:
        logging.debug(e)


def subtrair(*args, **kwargs):
    logging.debug(f'{args} {kwargs}')
    lista = []

    try:
        if len(args) == 1 and isinstance(args[0], Iterable):
            lista = (0. if x is None else float(x) for x in args[0])
        else:
            lista = (0. if x is None else float(x) for x in args)
        return reduce(sub, lista)
    except ValueError as e:
        logging.debug(e)
    except TypeError as e:
        logging.debug(e)


def multiplicar(*args, **kwargs):
    logging.debug(f'{args} {kwargs}')
    if not args and not kwargs:
        return 0
    try:
        if len(args) == 1 and isinstance(args[0], Iterable):
            lista = (0. if x is None else float(x) for x in args[0])
        else:
            lista = (0. if x is None else float(x) for x in args)
        return reduce(mul, lista)
    except TypeError as e:
        logging.debug(e)


def dividir(*args, **kwargs):
    logging.debug(f'{args} {kwargs}')
    # if (not args or all(args)) and not kwargs:
    #     return 0
    lista = []
    try:
        if len(args) == 1 and isinstance(args[0], Iterable):
            lista = (float(x) for x in args[0])
        else:
            lista = (float(x) for x in args)
        return reduce(lambda a, b: a/b, lista)
    except TypeError as e:
        logging.debug(e)
    except DivisionByZero as e:
        logging.debug(e)

