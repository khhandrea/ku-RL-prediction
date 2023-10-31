# (Data format)
# 이름: (experiment)-(step).txt
# 첫번째 줄: 최종 V값
# 두번째 줄: step별 loss (띄어쓰기로 구분)
# experiment: DP, MC, TD 1step, TD 3step
# step: 100, 1000, 10000, 100000
# (경우의수 총 16개)
from typing import Tuple

import numpy as np
from matplotlib import pyplot as plt

def __file_path(experiment: str, step: int=0) -> None:
    return f'{experiment}-{step}.txt'

def write_result(
        experiment: str,
        step: int,
        vs: np.ndarray,
        mean: np.ndarray=None,
        std: np.ndarray=None
        ) -> None:
    path = __file_path(experiment, step)
    vs = ' '.join(map(str, [v for v in vs.reshape(16,)])) + '\n'
    with open(path, 'w') as file:
        file.write(vs)
        if mean == None:
            pass
        if std == None:
            pass
    print(f"saved to {path}")

def read_result(
        experiment: str,
        step: int=0,
        size: int=4
        ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    path = __file_path(experiment, step)
    line2np = lambda line: np.array(list(map(float, line.split()))).reshape(size * size)

    if experiment == 'DP':
        with open(path, 'r') as file:
            line = file.readline()
        vs = line2np(line)
        
        return vs, None, None
    else:
        if step != 0:
            experiments = ('MC', 'TD1', 'TD3')
            data = {}
            for experiment in experiments:
                with open(path) as file:
                    data[experiment] = file.readlines()

                # vs
                data[experiment][0] = line2np(data[experiment][0])
                # mean
                data[experiment][1]
                # bias
                data[experiment][2]
        else:
            print('invalid parameters')

def get_gridlike(state: np.ndarray, size=4) -> np.ndarray:
    return state.reshape((4, -1))