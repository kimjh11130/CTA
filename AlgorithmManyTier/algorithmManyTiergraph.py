import matplotlib.pyplot as plt

plt.rc('font', family='Pretendard')

if __name__ == '__main__':
    bronze2 = {'구현': 594,
               '수학': 354,
               '문자열': 265,
               '사칙연산': 201,
               '브루트포스 알고리즘': 117,
               '시뮬레이션': 78,
               '기하학': 27,
               '정수론': 24,
               '정렬': 22,
               '많은 조건 분기': 19,
               '그리디 알고리즘': 17,}
    silber1 = {'수학': 197,
               '구현': 170,
               '브루트포스 알고리즘': 142,
               '그리디 알고리즘': 97,
               '정렬': 84,
               '그래프 이론': 79,
               '그래프 탐색': 75,
               '문자열': 73,
               '자료 구조': 67,
               '다이나믹 프로그래밍': 66,
               '정수론': 55,
               '너비 우선 탐색': 53,
               '깊이 우선 탐색': 47,
               '시뮬레이션': 46,
               '기하학': 37,
               '이분 탐색': 31,
               '백트래킹': 29,
               '해시를 사용한 집합과 맵': 27,
               '애드 혹': 26}
    gold4 = {'수학': 199,
             '구현': 189,
             '그래프 이론': 189,
             '브루트포스 알고리즘': 172,
             '그래프 탐색': 156,
             '다이나믹 프로그래밍': 156,
             '그리디 알고리즘': 123,
             '너비 우선 탐색': 108,
             '정렬': 95,
             '자료 구조': 93,
             '문자열': 88,
             '시뮬레이션': 61,
             '백트래킹': 56,
             '깊이 우선 탐색': 53,
             '정수론': 50,
             '이분 탐색': 45,
             '누적 합': 43,
             '애드 혹': 37,
             '기하학': 35,
             '해시를 사용한 집합과 맵': 32, }
    platinum5 = {'다이나믹프로그래밍': 220,
                 '그래프 이론': 193,
                 '수학': 189,
                 '자료 구조': 148,
                 '그래프 탐색': 119,
                 '구현': 87,
                 '그리디 알고리즘': 73,
                 '정렬': 72,
                 '기하학': 64,
                 '이분 탐색': 58,
                 '너비 우선 탐색': 57,
                 '정수론': 53,
                 '세그먼트 트리': 52,
                 '브루트포스 알고리즘': 51,
                 '비트마스킹': 51,
                 '트리': 50,
                 '애드 혹': 48,
                 '데이크스트라': 41,
                 '깊이 우선 탐색': 40,
                 '비트필드를 이용한 다이나믹 프로그래밍': 34}
    dia5 = {'자료 구조': 223,
            '수학': 179,
            '다이나믹 프로그래밍': 173,
            '그래프 이론': 144,
            '세그먼트 트리': 131,
            '트리': 91,
            '기하학': 65,
            '이분 탐색': 62,
            '그리디 알고리즘': 61,
            '그래프 탐색': 57,
            '정수론': 56,
            '애드 혹': 46,
            '최대 유량': 45,
            '구현': 42,
            '조합론': 37,
            '해 구성하기': 36,
            '문자열': 35,
            '느리게 갱신되는 세그먼트 트리': 34,
            '분리 집합': 32,
            '스위핑': 32}
    ruby5 = {'자료구조': 77,
             '다이나믹 프로그래밍': 62,
             '그래프 이론': 60,
             '수학': 56,
             '트리': 48,
             '세그먼트 트리': 40,
             '기하학': 26,
             '분할 정복': 25,
             '애드 혹': 24,
             '구현': 23,
             '그리디 알고리즘': 21,
             '많은 조건 분기': 18,
             '트리에서의 다이나믹 프로그래밍': 18,
             '그래프 탐색': 16,
             '이분 탐색': 16,
             '느리게 갱신되는 세그먼트 트리': 14,
             '조합론': 14,
             '깊이 우선 탐색': 13,
             '문자열': 12,
             '분리 집합': 12}

    topics = list(bronze2.keys())
    values = list(bronze2.values())
    plt.pie(values, labels=topics, autopct='%1.1f%%')
    plt.title('브론즈 티어의 유형 분포')
    plt.savefig('./img/bronze.png', format='png', dpi=200)
    plt.cla()
    plt.clf()

    topics = list(silber1.keys())
    values = list(silber1.values())
    plt.pie(values, labels=topics, autopct='%1.1f%%')
    plt.title('실버 티어의 유형 분포')
    plt.savefig('./img/silber.png', format='png', dpi=200)
    plt.cla()
    plt.clf()

    topics = list(gold4.keys())
    values = list(gold4.values())
    plt.pie(values, labels=topics, autopct='%1.1f%%')
    plt.title('골드 티어의 유형 분포')
    plt.savefig('./img/gold.png', format='png', dpi=200)
    plt.cla()
    plt.clf()

    topics = list(platinum5.keys())
    values = list(platinum5.values())
    plt.pie(values, labels=topics, autopct='%1.1f%%')
    plt.title('플래티넘 티어의 유형 분포')
    plt.savefig('./img/platinum.png', format='png', dpi=200)
    plt.cla()
    plt.clf()

    topics = list(dia5.keys())
    values = list(dia5.values())
    plt.pie(values, labels=topics, autopct='%1.1f%%')
    plt.title('다이아 티어의 유형 분포')
    plt.savefig('./img/dia.png', format='png', dpi=200)
    plt.cla()
    plt.clf()

    topics = list(ruby5.keys())
    values = list(ruby5.values())
    plt.pie(values, labels=topics, autopct='%1.1f%%')
    plt.title('루비 티어의 유형 분포')
    plt.savefig('./img/ruby.png', format='png', dpi=200)
    plt.cla()
    plt.clf()