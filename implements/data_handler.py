# (Data format)
# 이름: (experiment)-(step).txt
# 첫번째 줄: 최종 V값
# 두번째 줄: step별 loss (띄어쓰기로 구분)
# experiment: DP, MC, TD 1step, TD 3step
# step: 100, 1000, 10000, 100000
# (경우의수 총 16개)

class LossReader:
    pass

class LossWriter:
    pass