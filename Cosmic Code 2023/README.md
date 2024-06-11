# Cosmic Code 2023
Решение 15 задач на алгоритмы, связанных с освоением и развитием космоса, в рамках соревнования: "Cosmic Code 2023".  
*Ты сможешь самостоятельно рассчитать время полёта Гагарина на корабле «Восток», создать секретную космическую программу Советского Союза по запуску спутников, управлять межпланетным аппаратом «Луноход-1», создать симуляцию системы управления кораблем «СОЮЗ-1» и многое-многое другое.*  
<https://codenrock.com/contests/cosmic-code-2023/>

1. [Сортировка космонавтов](#сортировка-космонавтов-по-длительности-полета)
2. [Полет Гагарина](#время-полета-гагарина)
3. [Секретные спутники](#секретные-спутники)

## Сортировка космонавтов по длительности полета
### Задание
У вас есть список космонавтов Советского Союза с указанием длительности их космических полетов в днях. Ваша задача - написать программу, которая будет сортировать этот список по убыванию длительности полета.

**Входные данные:** На вход программе подается число N - количество космонавтов в списке; N строк, каждая из которых содержит имя космонавта и длительность его полета в днях (целое число)  
**Пример входных данных:**  
3  
Yuri Gagarin 1  
Valentina Tereshkova 3  
Alexei Leonov 4  
**Выходные данные:** Программа должна вывести отсортированный список космонавтов по убыванию длительности полета  
**Пример выходных данных:**  
Alexei Leonov 4  
Valentina Tereshkova 3  
Yuri Gagarin 1  

### Код (astronaut_sorting.py)
```python
def insertion_sort(array):
    for step in range(1, len(array)):
        current = step
        for i in range(step-1, -1, -1):
            if int(array[current][2]) > int(array[i][2]):
                array[current], array[i] = array[i], array[current]
                current = i
    return array

def main():
    number = int(input())
    cosmonauts = []
    for n in range(number): 
        cosmonauts.append(input().split())
    insertion_sort(cosmonauts)
    cosmonauts = [' '.join(item) for item in cosmonauts]
    for cosmonaut in cosmonauts: 
        print(cosmonaut)
 
if __name__ == "__main__":
    main()
```

## Время полета Гагарина
### Задание
12 апреля 1961 года Советский Союз совершил первый пилотируемый космический полет на корабле "Восток" с Юрием Гагариным на борту. Полет длился 108 минут. Ваша задача - написать программу, которая будет определять время возврата космонавта на Землю, если известно время его старта.  

**Входные данные:** Ввод состоит из двух чисел h и m (0 ≤ h ≤ 23; 0 ≤ m ≤ 59) - час и минута старта "Восток" с Юрием Гагариным на борту  
**Пример входных данных:** 9 7  
**Выходные данные:** Выведите два числа - час и минуту возвращения "Восток" на Землю  
**Пример выходных данных:** 10 55  

### Код (flight_time.py)
```python
def get_landing_time(h,m):
    h = (h + 1 + (m + 48) // 60) % 24
    m = (m + 48) % 60
    return h, m

def main():
    h, m = input().split()
    h, m = get_landing_time(int(h),int(m))
    print(h, m)

if __name__ == "__main__":
    main()
```

## Секретные спутники
### Задание
Секретная космическая программа Советского Союза запускает спутники для исследования космоса. Вам необходимо создать программу, которая будет определять, сколько спутников можно запустить в космос на основе заданных параметров. Для каждого спутника известны его масса и объем. Ракета-носитель может вывести определенную максимальную массу и объем в космос. Необходимо определить, сколько спутников можно запустить в один полет, чтобы не превысить грузоподъемность и объем ракеты-носителя.  

**Входные данные:**  В первой строке два числа M и V  - максимальная грузоподъемность и объем ракеты-носителя; во второй строке число N (1 <= N <= 1000) - количество спутников; далее N строк, содержащих два числа m и v (1 <= m, v <= 10000) - масса и объем каждого спутника  
**Пример входных данных:**  
1000 1000  
4  
250 250  
300 300  
350 350  
200 200  
**Выходные данные:** Выведите одно число - максимальное количество спутников, которые могут быть запущены одновременно  
**Пример выходных данных:** 3  

### Код (secret_satellites.py)
```python
def selection_sort(array, M_or_V):
    for step in range(len(array)-1):
        for i in range(step, len(array)-1):
            if array[step][M_or_V] > array[i+1][M_or_V]:           
                array[step], array[i+1] = array[i+1], array[step]
    return array

def get_max_count(satellites, max_M, max_V, M_or_V):
    satellites = selection_sort(satellites, M_or_V)
    current_M, current_V, count = 0, 0, 0
    while (current_M < max_M and current_V < max_V and count < len(satellites)):
        current_M += satellites[count][0]
        current_V += satellites[count][1]
        count += 1
    return count - 1

def main():
    max_M, max_V = input().split()
    number = int(input())
    satellites = []
    for n in range(number):
        satellites.append(input().split())
    satellites = [[int(item[0]),int(item[1])] for item in satellites] 
    count_M = get_max_count(satellites, int(max_M), int(max_V), 0)
    count_V = get_max_count(satellites, int(max_M), int(max_V), 1)
    print(max(count_M, count_V))

if __name__ == "__main__":
    main()
```

