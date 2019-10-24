import math

# Функция создание массива
def input_array(row, column):
    array = []
    for i in range(0, row):
        sub_array = []
        for j in range(column):
            if j == 0:
                print('Введите число [ ', i, ' ]', '[ ', j, ' ]:')
                number = int(input())
                sub_array.append(number)
            if j == 1:
                sub_array.append(0)
        array.append(sub_array)
    return array

# Функция вывода массива
def output_array(array):
    print()
    for i in array:
        for j in i:
            print("%d\t" % j, end='')
        print('')

def output_arrayAns(array):
    print()
    for i in range(len(array)):
        print('[', array[i][0], ']', '\t', '{:.4f}'.format(array[i][1]))

def main():
    array = input_array(10, 2)
    output_array(array)
    sum = 0
    proiz = int(1)

    for i in range(0, 10):
        if array[i][0] == 0:
            answer = 0
        else:
            proiz *= array[i][0]
            sum += array[i - 1][0]
            chislitel = ((proiz - sum) / (math.factorial(i) + math.sin(array[i][0]))) ** (1/2)
            znam = math.sin(array[i][0] + array[i-1][0]) **2

            try:
                answer = chislitel/znam
            except ValueError:
                print("В python нельзя  возвести %d" % answer, end='')
                print("в дробную степень. Число будет пропущено")
                continue
        array[i][1] = answer
    print()
    output_arrayAns(array)

if __name__ == '__main__':
    main()