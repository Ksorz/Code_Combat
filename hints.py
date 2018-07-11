Positions = [ {'x':20,'y':24}, {'x':28,'y':24}, {'x':36,'y':24}, {'x':44,'y':24}, {'x':52,'y':24} ]

list.append(x)                 # Добавляет элемент в конец массива.
list.extend(L)                 # Расширяет массив list, добавляя в конец все элементы массива L.
list.insert(i, x)              # Вставляет на i-ый элемент значение x.
list.remove(x)                 # Удаляет первый элемент в массиве, имеющий значение x. ValueError, если такого элемента не существует.
list.pop(i)                    # Удаляет и ВОЗВРАЩАЕТ элемент (i) массива. () - последний элемент.
list.index(x, start , end)     # ВОЗВРАЩАЕТ ПОЛОЖЕНИЕ первого элемента x (поиск ведется от start (включительно) до end (НЕ включительно)).
list.count(x)                  # ВОЗВРАЩАЕТ количество элементов со значением x.
list.sort([key=функция])       # Сортирует массив на основе функции.
list.reverse()                 # Разворачивает массив.
list.copy()                    # Поверхностная копия массива.
list.clear()                   # Очищает массив.

event.speaker.id # Наименование, имя объекта.

celadia = findByName("Celadia", friends)

event.message.toLowerCase() # Перевод текста в нижний регистр, (toUpperCase - верхний).

words = event.message.split(" ") # Разделение текста в массив (words) по ключевым символам: " ", "X" итд.

unitType = words[-1] # Последний элемент массива, ([-2] предпоследний итд).

hero.built # Массив построенных героем юнитов

for x in range(40, 81, 20): # От 40 до 81 с шагом 20.
    hero.moveXY(x, 60) # x1 - 40; x2 - 60; x3 - 80

target = targets.pop(0) # Удаляет и возвращает (target) элемент (0) массива (targets). () - последний элемент.
