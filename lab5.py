## 11.	F(1) = 1, F(n) = F(n–1) * (2*n + 1), при n > 1

import timeit
import matplotlib.pyplot as plt

a = []
b = []


def paf(n):
    if n == 1:
        return 1
    elif n > 1:
        return paf(n - 1) * (2 * n + 1)


def pav(n):
    result = 1
    for i in range(2, n + 1):
        result *= (2 * i + 1)
    return result


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 994]
print('№' + '       ' + 'Рекурсивно' + '        ' + 'Итеративно')
for i in nums:
    a.append(timeit.timeit(lambda: paf(i), number=20000))
    print(paf(i))
    b.append(timeit.timeit(lambda: pav(i), number=20000))
    print(i, ' ', a[-1], '|', b[-1])
plt.xlabel('Числовые значения')
plt.ylabel('Время поиска')
plt.plot(nums, a, label='Рекурсивно')
plt.plot(nums, b, label='Итеративно')
plt.legend()
plt.show()
