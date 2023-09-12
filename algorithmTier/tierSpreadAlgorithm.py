import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family='Pretendard')

if __name__ == '__main__':
    array = np.zeros((31,), dtype=int)
    math = [24, 57, 137, 342, 339, 268, 159, 223, 217, 221, 199, 208, 240, 231, 223, 158, 235, 208, 243, 176, 184, 180,
            172, 104, 100, 71, 56, 39, 27, 6, 7]
    implement = [49, 95, 117, 387, 558, 444, 368, 290, 250, 163, 172, 182, 140, 127, 118, 101, 97, 89, 76, 65, 48, 42,
                 35, 37, 33, 24, 22, 11, 6, 9, 6]
    dp = [10, 0, 0, 0, 2, 4, 14, 20, 59, 70, 113, 153, 208, 245, 220, 217, 255, 208, 220, 214, 157, 149, 151, 117, 69,
          58, 59, 31, 13, 5, 2]
    graph = [33, 0, 0, 0, 0, 1, 6, 14, 28, 90, 134, 186, 277, 276, 253, 191, 227, 186, 164, 180, 118, 133, 121, 88, 57,
             63, 58, 28, 8, 7, 5]
    datastruct = [9, 0, 0, 0, 8, 14, 56, 95, 79, 64, 75, 81, 130, 130, 127, 114, 163, 189, 196, 160, 182, 179, 186, 140,
                  73, 72, 66, 42, 17, 7, 8]
    sort = [3, 0, 1, 4, 20, 58, 141, 158, 126, 88, 78, 98, 92, 76, 76, 34, 85, 74, 55, 51, 35, 30, 18, 13, 10, 5, 7, 2,
            2, 2, 3]
    greedy = [12, 0, 0, 12, 15, 46, 89, 116, 99, 100, 100, 127, 122, 140, 105, 123, 52, 90, 100, 101, 76, 61, 67, 37,
              26, 27, 21, 14, 5, 4, 5]
    bruteforce = [20, 0, 2, 53, 110, 117, 136, 122, 129, 147, 158, 176, 141, 111, 69, 68, 53, 22, 35, 29, 15, 19, 13, 3,
                  8, 5, 3, 3, 0, 0, 1]
    geometry = [18, 1, 12, 29, 33, 32, 20, 31, 31, 39, 30, 38, 62, 47, 54, 49, 45, 74, 72, 75, 71, 65, 55, 57, 47, 33,
                26, 12, 9, 5, 2]
    manyIf = [8, 0, 3, 15, 16, 23, 18, 31, 30, 20, 34, 28, 27, 29, 22, 20, 25, 35, 22, 37, 29, 31, 25, 23, 21, 9, 18, 8,
              5, 4, 3]
    tier = ['Unrated', 'Bronze V', 'Bronze IV',
            'Bronze III', 'Bronze II', 'Bronze I', 'Silver V', 'Silver IV',
            'Silver III', 'Silver II', 'Silver I', 'Gold V', 'Gold IV', 'Gold III', 'Gold II', 'Gold I', 'Platinum V',
            'Platinum IV', 'Platinum III', 'Platinum II', 'Platinum I', 'Diamond V', 'Diamond IV', 'Diamond III',
            'Diamond II', 'Diamond I', 'Ruby V', 'Ruby IV', 'Ruby III', 'Ruby II', 'Ruby I']

    plt.figure(figsize=(15, 5))
    plt.bar(range(len(tier)), math, width=0.5)
    plt.title('알고리즘 \'수학\' 유형의 난이도 분포도')
    plt.ylabel('티어별 문제 수')
    plt.xticks(range(len(tier)), tier, rotation=90)
    plt.ylim([0, 500])
    plt.tight_layout()
    plt.savefig('./img/math.png', format='png', dpi=200)
    plt.cla()
    plt.clf()

    plt.figure(figsize=(15, 5))
    plt.bar(range(len(tier)), implement, width=0.5)
    plt.title('알고리즘 \'구현\' 유형의 난이도 분포도')
    plt.ylabel('티어별 문제 수')
    plt.xticks(range(len(tier)), tier, rotation=90)
    plt.ylim([0, 600])
    plt.tight_layout()
    plt.savefig('./img/implement.png', format='png', dpi=200)
    plt.cla()
    plt.clf()

    plt.figure(figsize=(15, 5))
    plt.bar(range(len(tier)), dp, width=0.5)
    plt.title('알고리즘 \'다이나믹 프로그래밍\' 유형의 난이도 분포도')
    plt.ylabel('티어별 문제 수')
    plt.xticks(range(len(tier)), tier, rotation=90)
    plt.ylim([0, 300])
    plt.tight_layout()
    plt.savefig('./img/dp.png', format='png', dpi=200)
    plt.cla()
    plt.clf()

    plt.figure(figsize=(15, 5))
    plt.bar(range(len(tier)), manyIf, width=0.5)
    plt.title('알고리즘 \'많은 조건 분기\' 유형의 난이도 분포도')
    plt.ylabel('티어별 문제 수')
    plt.xticks(range(len(tier)), tier, rotation=90)
    plt.ylim([0, 100])
    plt.tight_layout()
    plt.savefig('./img/manyIf.png', format='png', dpi=200)
    plt.cla()
    plt.clf()

    plt.figure(figsize=(15, 5))
    plt.bar(range(len(tier)), graph, width=0.5)
    plt.title('알고리즘 \'그래프 이론\' 유형의 난이도 분포도')
    plt.ylabel('티어별 문제 수')
    plt.xticks(range(len(tier)), tier, rotation=90)
    plt.ylim([0, 300])
    plt.tight_layout()
    plt.savefig('./img/graph.png', format='png', dpi=200)
    plt.cla()
    plt.clf()

    plt.figure(figsize=(15, 5))
    plt.bar(range(len(tier)), geometry, width=0.5)
    plt.title('알고리즘 \'기하학\' 유형의 난이도 분포도')
    plt.ylabel('티어별 문제 수')
    plt.xticks(range(len(tier)), tier, rotation=90)
    plt.ylim([0, 100])
    plt.tight_layout()
    plt.savefig('./img/geometry.png', format='png', dpi=200)
    plt.cla()
    plt.clf()

    plt.figure(figsize=(15, 5))
    plt.bar(range(len(tier)), greedy, width=0.5)
    plt.title('알고리즘 \'그리디\' 유형의 난이도 분포도')
    plt.ylabel('티어별 문제 수')
    plt.xticks(range(len(tier)), tier, rotation=90)
    plt.ylim([0, 200])
    plt.tight_layout()
    plt.savefig('./img/greedy.png', format='png', dpi=200)
    plt.cla()
    plt.clf()

    plt.figure(figsize=(15, 5))
    plt.bar(range(len(tier)), sort, width=0.5)
    plt.title('알고리즘 \'정렬\' 유형의 난이도 분포도')
    plt.ylabel('티어별 문제 수')
    plt.xticks(range(len(tier)), tier, rotation=90)
    plt.ylim([0, 200])
    plt.tight_layout()
    plt.savefig('./img/sort.png', format='png', dpi=200)
    plt.cla()
    plt.clf()

    plt.figure(figsize=(15, 5))
    plt.bar(range(len(tier)), bruteforce, width=0.5)
    plt.title('알고리즘 \'브루트포스\' 유형의 난이도 분포도')
    plt.ylabel('티어별 문제 수')
    plt.xticks(range(len(tier)), tier, rotation=90)
    plt.ylim([0, 200])
    plt.tight_layout()
    plt.savefig('./img/bruteforce.png', format='png', dpi=200)
    plt.cla()
    plt.clf()

    plt.figure(figsize=(15, 5))
    plt.bar(range(len(tier)), datastruct, width=0.5)
    plt.title('알고리즘 \'자료구조\' 유형의 난이도 분포도')
    plt.ylabel('티어별 문제 수')
    plt.xticks(range(len(tier)), tier, rotation=90)
    plt.ylim([0, 200])
    plt.tight_layout()
    plt.savefig('./img/datastruct.png', format='png', dpi=200)
    plt.cla()
    plt.clf()
