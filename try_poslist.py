#! /usr/bin/env python3


# Standard Library:
import random
import sys

# 3rd Party:
#from ch07.positional_list import PositionalList
sys.path.insert(0, r'C:\Working\GitHub\sockduct\AoC\2021')
from positional_list import PositionalList
from ch07.insertion_sort_positional import insertion_sort


if __name__ == '__main__':
    poslist = PositionalList()
    rng = random.SystemRandom()

    '''
    if poslist.is_empty():
        print('Positional list is empty.')
    '''

    for _ in range(6):
        poslist.add_last(rng.randrange(1, 100))
    '''
        match i:
            case 0:
                lastpos = poslist.add_last(newnum)
            case 1:
                lastpos = poslist.add_first(newnum)
            case 2:
                lastpos = poslist.add_after(lastpos, newnum)
            case 3:
                lastpos = poslist.add_before(lastpos, newnum)
            case 4:
                poslist.replace(lastpos, newnum)
            case 5:
                poslist.delete(lastpos)
                lastpos = poslist.add_last(newnum)
    '''

    print(f'Curent list:  {", ".join(str(e) for e in poslist)}')
    insertion_sort(poslist)
    print(f'Curent list:  {", ".join(str(e) for e in poslist)}')

    '''
    print(f'      First element in posotional list:  {poslist.first().element()}')
    print(f'       Last element in positional list:  {poslist.last().element()}')
    print(f'Element after first in positional list:  {poslist.after(poslist.first()).element()}')
    print(f'Element before last in positional list:  {poslist.before(poslist.last()).element()}')
    '''
