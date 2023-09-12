import matplotlib.pyplot as plt

plt.rc('font', family='Pretendard')

if __name__ == '__main__':
    bronze2 = [0, 131, 310, 158, 60, 16, 1]
    silber1 = [0, 271, 304, 187, 132, 52, 20, 2, 1]
    gold4 = [0, 237, 372, 257, 146, 65, 19, 14, 6]
    platinum5 = [0, 127, 263, 268, 151, 70, 37, 15, 4, 2]
    dia5 = [0, 62, 160, 181, 141, 96, 56, 28, 13, 5, 0, 0, 1]
    ruby5 = [0, 12, 27, 46, 35, 34, 19, 13, 11, 8, 6, 1, 0, 1]

    plt.barh(range(len(bronze2)), bronze2, color='red')
    plt.title('브론즈 문제의 한 문제당 유형 개수')
    plt.ylabel('문제별 유형 수')
    plt.yticks(range(len(bronze2)), [f'{i}개' for i in range(len(bronze2))])
    for i in range(len(bronze2)):
        if (bronze2[i]):
            name = f'{bronze2[i]}개'
            y = i - 0.2
            x = bronze2[i] + 0.2
            plt.text(x, y, name)
    plt.savefig('./img/bronze.png', format='png', dpi=200)
    plt.cla()
    plt.clf()

    plt.barh(range(len(silber1)), silber1, color='red')
    plt.title('실버 문제의 한 문제당 유형 개수')
    plt.ylabel('문제별 유형 수')
    plt.yticks(range(len(silber1)), [f'{i}개' for i in range(len(silber1))])
    for i in range(len(silber1)):
        if (silber1[i]):
            name = f'{silber1[i]}개'
            y = i - 0.2
            x = silber1[i] + 0.2
            plt.text(x, y, name)
    plt.savefig('./img/silber.png', format='png', dpi=200)
    plt.cla()
    plt.clf()

    plt.barh(range(len(gold4)), gold4, color='red')
    plt.title('골드 문제의 한 문제당 유형 개수')
    plt.ylabel('문제별 유형 수')
    plt.yticks(range(len(gold4)), [f'{i}개' for i in range(len(gold4))])
    for i in range(len(gold4)):
        if (gold4[i]):
            name = f'{gold4[i]}개'
            y = i - 0.2
            x = gold4[i] + 0.2
            plt.text(x, y, name)
    plt.savefig('./img/gold.png', format='png', dpi=200)
    plt.cla()
    plt.clf()

    plt.barh(range(len(platinum5)), platinum5, color='red')
    plt.title('플레티넘 문제의 한 문제당 유형 개수')
    plt.ylabel('문제별 유형 수')
    plt.yticks(range(len(platinum5)), [f'{i}개' for i in range(len(platinum5))])
    for i in range(len(platinum5)):
        if (platinum5[i]):
            name = f'{platinum5[i]}개'
            y = i - 0.2
            x = platinum5[i] + 0.2
            plt.text(x, y, name)
    plt.savefig('./img/platinum.png', format='png', dpi=200)
    plt.cla()
    plt.clf()

    plt.barh(range(len(dia5)), dia5, color='red')
    plt.title('다이아 문제의 한 문제당 유형 개수')
    plt.ylabel('문제별 유형 수')
    plt.yticks(range(len(dia5)), [f'{i}개' for i in range(len(dia5))])
    for i in range(len(dia5)):
        if (dia5[i]):
            name = f'{dia5[i]}개'
            y = i - 0.2
            x = dia5[i] + 0.2
            plt.text(x, y, name)
    plt.savefig('./img/dia.png', format='png', dpi=200)
    plt.cla()
    plt.clf()

    plt.barh(range(len(ruby5)), ruby5, color='red')
    plt.title('루비 문제의 한 문제당 유형 개수')
    plt.ylabel('문제별 유형 수')
    plt.yticks(range(len(ruby5)), [f'{i}개' for i in range(len(ruby5))])
    for i in range(len(ruby5)):
        if (ruby5[i]):
            name = f'{ruby5[i]}개'
            y = i - 0.2
            x = ruby5[i] + 0.2
            plt.text(x, y, name)
    plt.savefig('./img/ruby.png', format='png', dpi=200)
    plt.cla()
    plt.clf()
