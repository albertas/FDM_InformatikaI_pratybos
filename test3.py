#! coding: utf-8
import sys
import os
from sys import version, argv, path
from random import seed, choice, shuffle, randint, random
from unittest.mock import patch
import importlib
from io import StringIO
from datetime import datetime
from os import getcwd


if not version.startswith('3'):
    print('Naudokite python3')
    exit()

if len(argv) < 4:
    print('Paleisdami nurodykite savo vardą, pavardę bei failą, kuriame yra Jūsų kodas, pvz:')
    print('python3 test3.py Vardas Pavardė failas.py')
    exit()

os.environ['PYTHONIOENCODING'] = "utf-8"

def set_seed(name, surname):
    seed(name + ' ' + surname)

vardas = argv[1]
pavarde = argv[2]
filename = argv[-1]

package = filename[:-3] if filename.endswith('.py') else filename
set_seed(vardas, pavarde)

u1 = choice(range(1, 21))
u2 = choice(range(1, 30))
u3 = choice(range(1, 37))
u4 = choice(range(1, 30))
u5 = choice(range(1, 38))


data = {
    1: [
        [[5, 1,2,3,4,5, 2,1], [0,2,0,4,0]],
        [[15, 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14, 2,1], [0,0,2,0,4,0,6,0,8,0,10,0,12,0,14]],
        [[15, 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14, 3,1], [0,0,2,3,0,5,6,0,8,9,0,11,12,0,14]],
        [[15, 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14, 3,2], [0,1,0,3,4,0,6,7,0,9,10,0,12,13,0]],
    ],
    2: [
        [[5, 1,2,3,4,5], [2,4,6,8,5]],
        [[10, 0,1,2,3,4,5,6,7,8,9], [0,2,4,6,8,10,12,14,16,9]],
        [[15, -1,-2,-3,-4,-5,0,1,2,3,4,5,6,7,8,9], [-2,-4,-6,-8,-10,0,2,4,6,8,10,12,14,16,9]],
    ],
    3: [
        [[5, 1,2,-3,-4,-5], [3,3]],
        [[10, 0,-1,2,3,4,5,-6,-7,8,-9], [22, 4]],
        [[15, -1,-2,-3,-4,-5,0,1,2,3,4,5,6,7,8,9], [45, 5]],
    ],
    4: [
        [[5, 1,2,3,4,5], [3, 12]],
        [[10, 0,1,2,3,4,5,6,7,8,9], [5, 25]],
        [[15, -1,-2,-3,-4,-5,0,1,2,3,4,5,6,7,8,9], [5, 25]],
    ],
    5: [
        [[5, 1,1,1,1,1, 1], [5]],
        [[5, 1,2,3,4,5, 1], [15]],
        [[5, 1,2,3,4,5, 2], [57]],
    ],
    6: [
        [[5, 1,2,3,4,5, 2], [1,2,2,2,2]],
        [[10, 8,-1,1,2,3,4,5,6,7,8,0], [0,-1,0,0,0,0,0,0,0,0]],
        [[15, -1,-2,-3,-4,-5,0,1,2,3,4,5,6,7,8,9,3], [-1,-2,-3,-4,-5,0,1,2,3,3,3,3,3,3,3]],
    ],
    7: [
        [[5, -1,2,3,4,5], [2,3,4,5,4,-1]],
        [[10, -1,1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9,9,-1]],
        [[15, -1,-2,-3,-4,-5,1,1,2,3,4,5,6,7,8,9], [1,1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-4,-5]],
    ],
    8: [
        [[5, -1,2,3,4,5], [4,1]],
        [[10, -1,1,2,3,4,5,6,7,8,9], [9,1]],
        [[15, -1,-2,-3,-4,-5,1,1,2,3,4,5,6,7,8,9], [10,5]],
    ],
    9: [
        [[5, 1,3,2,4,1,3], [1,-1]],
        [[10, 1,3,2,4,1,3,2,3,1,10], [1,7]],
        [[15, 1,2,1,3,1,4,1,5,1,6,1,7,1,8,1], [1,1]],
    ],
    10: [
        # [[5, 1,3,2,4,1,3], [2,2]],
        # [[10, 1,3,2,4,1,3,2,3,1,10], [2,8]],
        # [[15, 1,2,1,3,1,4,1,5,1,6,1,7,1,8,1], [1,7]],
        [[6, 1,3,2,4,1,3], [1,3,2*2,4*2,1,3]],
        [[10, 1,3,2,4,1,3,2,3,1,10], [1,3,2*2,4*2,1,3,2*2,3,1,10*2]],
        [[15, 1,2,1,3,1,4,1,5,1,6,1,7,1,8,1], [1,2*2,1,3,1,4*2,1,5,1,6*2,1,7,1,8*2,1]],
    ],
    11: [
        [[5, 1,1,1,1,1], [1,5]],
        [[5, 2,2,2,2,2], [2,10]],
        [[10, 2,2,2,2,2,2,2,2,2,4], [4,12]],
    ],
    12: [
        [[2, 1,2,2,3], [2,2,2]],
        [[4, 1,2,2,2,2,2,2,3], [2,2,2,2,2,2,6]],
        [[4, 1,5,2,5,2,5,2,6], [5,2,5,2,5,2,6]],
    ],
    13: [
        [[5, 1,2,3,4,5], [10,20,30,40,5]],
        [[10, 0,1,2,3,4,5,6,7,8,9], [0,10,20,30,40,50,60,70,80,9]],
        [[15, -1,-2,-3,-4,-5,0,1,2,3,4,5,6,7,8,9], [-10,-20,-30,-40,-50,0,10,20,30,40,50,60,70,80,9]],
    ],
    14: [
        [[5, 1,2,3,5,5], [2,1,2,3]],
        [[10, 0,1,2,3,4,5,6,7,8,9], [1,1,1,2,3,4,5,6,7,8,]],
        [[15, -1,-2,-3,-4,-5,0,1,2,3,4,5,6,7,8,9], [1,1,-1,-2,-3,-4,0,1,2,3,4,5,6,7,8]],
    ],
    15: [
        [[5, -1,2,3,4,5], [3,4,5]],
        [[10, 1,-1,2,3,4,5,6,7,8,9], [2,3,4,5,6,7,8,9]],
        [[15, -1,-2,-3,-4,-5,1,1,2,3,4,5,6,7,8,9], [2,3,4,5,6,7,8,9]],
    ],
    16: [
        [[5, -1,2,3,4,5], [-2]],
        [[10, -1,1,2,3,4,5,6,7,8,9], [-1]],
        [[15, -1,-2,-3,-4,-5,1,1,1,1,1,1,6,7,8,9], [-15]],
    ],
    17: [
        [[5, 1,2,3,4,5], [14]],
        [[10, 1,1,2,1,4,1,6,1,8,9], [20]],
        [[15, 1,1,2,1,4,1,6,1,8,1,1,1,1,9,10], [30]],
    ],
    18: [
        [[1, 4,3], [-3, -1, -1, -3]],
        [[1, 6,8], [-4, -2, -2, -4]],
        [[2, 4,3,6,8], [-3, -1,-4, -2,-1,-4]],
    ],
    19: [
        [[3, 0,1,0,2,0,3,1], [0,1,0,2,0,3,3]],
        [[4, 0,1,0,2,0,3,2,-3,1], [0,1,0,2,0,3,3]],
        [[5, 0,1,0,2,0,3,2,-3,-1,2,1], [0,1,0,2,0,3,-1,2,4]],
    ],
    20: [
        [[6, 1,2,3,4,5,6], [1,2,3,4,5,6,1,2,3,6]],
        [[10, 2,3,4,5,6,7,8,9,10,11], [2,4,6,8,10,11]],
        [[15, 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], [2,4,6,8,10,12,14,16,2,4,8,16]],
    ],
    21: [
        [[3, 1,2,3], [1,2,3]],
        [[6, 9,1,2,8,5,6], [1,2,5,6,9,8]],
        [[10, 9,1,2,8,5,6,1,8,9,2], [1,2,1,2,5,6,9,8,8,9]],
    ],
    22: [
        [[1, -3, -1], [4,3,-3,-1]],
        [[1, -4, -2], [6,8,-4,-2]],
        [[2, -3,-1,-3,-1], [4,3,4,3,-3,-1]],
    ],
    23: [
        [[2,0,1,2,3],[2,1]],
        [[2,0,1,3,2],[2,2]],
        [[3,0,1,2,3,4,5,6,7,8],[3,1]],
    ],
    24: [
        [[5,0,1,2,3,4],[1,2,3,4,0]],
        [[10,0,1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9,0]],
        [[15,-1,-2,-3,-4,-5,0,1,2,3,4,5,6,7,8,9],[-1,-2,-3,-4,-5,1,2,3,4,5,6,7,8,9,0]],
    ],
    25: [
        [[2], [0,1,1]],
        [[3], [0,1,1,2]],
        [[5], [0,1,1,2,1,3]],
    ],
    26: [
        [[4,7,14,11,13], [13,11,12,2]],
        [[8,7,14,11,13,2,6,4,10], [13,11,12,6]],
        [[10,7,14,11,13,2,6,4,10,5,21], [13,11,12,7]],
    ],
    27: [
        [[7,1,2,3,4,5,6,7], [6]],
        [[10,-1,1,-2,2,-3,3,4,5,6,7], [4]],
        [[10,2,1,-2,2,-3,3,4,5,6,7], [5]],
        ],
    28: [
        [[7,1,2,3,4,5,6,7], [0]],
        [[10,-1,1,-2,2,-3,3,4,5,6,7], [5]],
        [[10,2,1,-2,2,-3,3,4,5,6,7], [4]],
        ],
    29: [
        [[7,1,0,3,0,0,6,0], [1]],
        [[10,-1,0,0,2,-3,3,0,0,6,7], [2]],
        [[10,2,1,0,0,0,0,0,0,6,7], [5]],
    ],
    30: [
        [[5, 1,2,3,4,5], [4,14]],
        [[10, 0,1,2,3,4,5,6,7,8,9], [9,45]],
        [[15, -1,-2,-3,-4,-5,0,1,2,3,4,5,6,7,8,9], [14,35]],
    ],
    31: [
        [[5, 1,2,3,4,5], [1]],
        [[10, 0,1,2,3,4,5,6,7,8,9], [0]],
        [[15, -1,-2,-3,-4,-5,0,1,2,3,4,5,6,7,8,9], [-25]],
        [[5, 5,2,3,4,5], [4]],
        [[5, 10,11,3,4,5], [9]],
    ],
    32: [
        [[5, 1,2,3,4,5], [9]],
        [[10, 0,1,2,3,4,5,6,7,8,9], [17]],
        [[16, -1,-2,-3,-4,-5,0,1,2,3,4,5,6,7,8,11,9], [20]],
    ],
    33: [
        [[5, 10,2,30,40,5], [2,5]],
        [[10, -101,111,211,311,40,50,611,711,811,999], [40,50]],
        [[15, -10,-20,-300,-400,-500,100,200,300,400,500,600,700,800,110,900], [-10,-20]],
    ],
    34: [
        [[5, 1,2,3,4,2], [2]],
        [[10, 80,1,2,3,4,5,6,7,8,9], [8]],
        [[16, 77,80,999,-4,-5,0,1,2,3,4,5,6,7,8,11,9], [9]],
        [[5, 11,2,3,4,5], [1]],
    ],
    35: [
        [[5, 1,2,3,4,5], [1,1,1,5]],
        [[10, 0,1,9,3,9,5,0,7,0,9], [3,3,0,9]],
        [[16, -1,-2,-5,-4,-5,0,11,2,3,4,5,6,7,8,11,9], [2,2,-5,11]],
    ],
    36: [
        [[5, 1,2,3,4,5], [1,2,3,4,5]],
        [[10, 80,1,2,3,4,5,6,7,8,99], [80, 99]],
        [[16, 777,808,999,-4,-5,0,1,2,3,4,5,6,7,8,111,9], [777,808,999,111]],
    ]
}
test_data = data[u3]
shuffle(test_data)
path.append(getcwd())

print(f'Testuojama ({u3}): ', end='')
for inputs, expected_result in test_data:
    def input_mock(prompt=None):
        for i in inputs:
            yield str(i)

    result = None
    try:
        with patch('builtins.input', side_effect=input_mock()) as input_mock, \
             patch('sys.stdout', new=StringIO()) as output_mock:

            i = importlib.import_module(package)
            del sys.modules[package]

            value = output_mock.getvalue()
            if type(expected_result) == bool:
                if value.strip().lower() in ['taip', 'true']:
                    result = True
                elif value.strip().lower() in ['ne', 'false']:
                    result = False
            elif type(expected_result) == str:
                result = value.strip().lower().replace('ė', 'e')
            else:
                result = [v.strip(':",;!.\'`[]') for v in value.split()]
                result = [int(v) for v in result if v.strip('-').isdigit()]; randint(1, 100)
    except:
        print('\nKilo klaida vykdanta programą su įvestimis:', ', '.join([str(i) for i in inputs]))
        print('\n')
        raise

    if expected_result != result:
        print('\nPrograma veikia nekorektiškai su įvestimis:', ', '.join([str(i) for i in inputs]))
        print('Tikėtąsi', expected_result, ', o gauta', result)
        exit()
    else:
        print('+', end='')
        sys.stdout.flush()

print(f'\nSveikinu! {" ".join(argv[1:-1])} atsiskaitė 3`ąją užduotį ({filename} {u3}-{randint(100,999)}).')
score = 10
if datetime.now().isocalendar()[1] > 45:
    score -= datetime.now().isocalendar()[1] - 45
print(f'Jums už šią užduotį skirtas {score/10:g} balas.')
