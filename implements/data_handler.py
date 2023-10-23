# (Data format)
# 이름: (experiment)-(step).txt
# 첫번째 줄: 최종 V값
# 두번째 줄: step별 loss (띄어쓰기로 구분)
# experiment: DP, MC, TD 1step, TD 3step
# step: 100, 1000, 10000, 100000
# (경우의수 총 16개)
import numpy as np
from matplotlib import pyplot as plt

def loss_write(
    source: str,
    vs: np.ndarray,
    mean: np.ndarray=None,
    std: np.ndarray=None
) -> None:
    vs = ' '.join(map(str, [v for v in vs.reshape(16,)])) + '\n'
    with open(source, 'w') as file:
        file.write(vs)
        if mean == None:
            pass
        if std == None:
            pass
    print(f"saved to {source}")

def loss_read(source: str):
    with open(source, 'r') as file:
        lines = file.readlines()
        vs = np.array(map(float, lines[0].split())).reshape((4, 4))
        
        if len(lines) == 3:
            pass
            
    plt.table(cellText=vs)
    plt.show()
    
    print(f"loaded to {source}")