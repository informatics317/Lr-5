from ЛР3 import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort
import pytest

def test_bubble_sort():
    a = [7, 2, 0, 3, 1, 4, 12]
    b = [0, 1, 2, 3, 4, 7, 12]
    assert bubble_sort(a) == b

def test_selections_sort():
    a = [3, 5, 1, 8, 2, 14]
    b = [1, 2, 3, 5, 8, 14]
    assert selection_sort(a) == b

def test_quick_sort():
    a = [3, 5, 1, 8, 2, 14]
    b = [1, 2, 3, 5, 8, 14]
    assert quick_sort(a) == b

def test_insertion_sort():
    a = [7, 33, 14, 276, 9, 0]
    b = [0, 7, 9, 14, 33, 276]
    assert insertion_sort(a) == b

def test_merge_sort():
    a = [7, 33, 14, 276, 9, 0]
    b = [0, 7, 9, 14, 33, 276]
    assert merge_sort(a) == b


x = 1
@pytest.mark.skipif(x > 0, reason='Тестовый пропуск')
def test_skipped_if():
    pass

@pytest.mark.xfail(reason='Намеренный провал')
def test_xfailed():
    assert False


'''1 Перевод чисел в троичную систему'''
def cc3(x):
    st = ''
    d = '012'
    while x>0:
        st = d[x%3] + st
        x = x//3
    return int(st)

def test_cc3():
    assert cc3(8) == 22
    assert cc3(1) == 1
    assert cc3(3) != 3
    print('\nРабота функции cc3:')
    print('8 в троичной сс =', cc3(8))
    print('1 в троичной сс =', cc3(1))
    print('3 в троичной сс =', cc3(3), ', а не 3')


'''2 Сумма цифр в числе'''
def sum_numbers(a):
    return sum(map(int, a))

def test_sum_numbers():
    assert sum_numbers('547') == 16
    assert sum_numbers('1000') == 1
    assert sum_numbers('0') == 0
    print('\nРабота функции sum_numbers:')
    print('Сумма цифр 547 =', sum_numbers('547'))
    print('Сумма цифр 1000 =', sum_numbers('1000'))
    print('Сумма цифр 0 =', sum_numbers('0'))


'''3 Делители числа'''
def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x%i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

def test_div():
    assert div(12) == [1, 2, 3, 4, 6, 12]
    assert div(13) == [1, 13]
    assert div(1) == [1]
    assert div(2) == [1, 2]
    print('\nРабота функции div:')
    print(div(12))


'''4 Треугольник'''
def treug(a, b, c):
    if a+b > c and a+c > b and b+c > a:
        ans = 'Треугольник существует'
    else:
        ans = 'Нет треугольника'
    return ans

def test_treug():
    assert treug(7, 4, 12) == 'Нет треугольника'
    assert treug(6, 6, 12) == 'Нет треугольника'
    assert treug(8, 10, 12) == 'Треугольник существует'
    assert treug(6, 6, 6) == 'Треугольник существует'
    print('\nРабота функции treug:')
    print('Стороны 7, 4, 12: ', treug(7, 4, 12))
    print('Стороны 6, 6, 12: ', treug(6, 6, 12))
    print('Стороны 8, 10, 12: ', treug(8, 10, 12))
    print('Стороны 6, 6, 6: ', treug(6, 6, 6))


'''5 Проверка палиндрома'''
def palindrome(text):
    text = text.lower().replace(' ', '')
    return text == text[::-1]

def test_palindrome():
    assert palindrome('шалаш') == True
    assert palindrome('А роза упала на лапу азора') == True
    print('\nРабота функции palindrome:')
    print('А роза упала на лапу азора'.lower().replace(' ', ''),
          'А роза упала на лапу азора'[::-1].lower().replace(' ', ''))
    assert palindrome('Привет') == False
    assert palindrome('a') == True
    assert palindrome('') == True


'''6 Количество слов в строке'''
def count_words(text):
    words = text.split()
    return len(words)

def test_count_words():
    assert count_words('Привет') == 1
    assert count_words('Тест номер два') == 3
    assert count_words('') == 0
    assert count_words('    ') == 0
    assert count_words('Солнце медленно опускалось за горизонт, окрашивая небо в яркие цвета.') == 10
    print('\nРабота функции count_words:')
    print('"Привет":', count_words('Привет'), 'слово в строке')






















