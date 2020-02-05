"""ООП в Python"""

#Создаем класс car
class Apartment:
    #создаем атрибуты класса
    city = "Moskow"
    rooms = 3
    price = 5.5

    #создаем методы класса
    def buy(self):
        print("Квартира куплена")
    def sold(self):
        print("Квартира продана")

#Создаем два обьекта класса apartment
apartment1 = Apartment()
apartment2 = Apartment()

#протестируем тип
print(type(apartment1))

#протестируем вызовы методов
apartment1.buy()
apartment2.sold()

#Протестируем вызов атрибутов класса
print(apartment1.city)
print(apartment1.rooms)
print(apartment1.price)

#Создадим массив из объектов класса
a = [apartment1, apartment2]
b = []

#считаем данные
for i in range(len(a)):
    a[i].city = input()
    a[i].rooms = int(input())
    a[i].price = float(input())
    print(a[i].city, a[i].rooms, a[i].price)
    if a[i].price > 4:
        b.append(a[i])


for i in range(len(b)):
    print(b[i].price, b[i].city, b[i].rooms)

#Задачи для самостоятельной работы
"""             Задача 1

1.Описать класс с именем STUDENT, содержащую следующие поля:
• NAME – фамилия и инициалы;
• GROUP – номер группы;
• SES - успеваемость (массив из пяти элементов).

2. Написать программу, выполняющую следующие действия :
• ввод с клавиатуры данных в список STUD1, состоящий из десяти объектов класса STUDENT; 
• вывод на дисплей фамилий и номеров групп для всех студентов, включенных в массив, если средний балл студента \
больше 4,0;
• если таких нет, вывести соответствующее сообщение."""

"""             Задача 2

1. Описать класс с именем NOTE, содержащую следующие поля:
• NAME — фамилия, имя;
• TELE — номер телефона;
• BDAY — день рождения (массив из трех чисел).

2. Написать программу, выполняющую следующие действия:
• ввод с клавиатуры данных в массив BLOCKNOTE, состоящий из восьми элементов типа NOTE; 
• вывод на экран информации о людях, чьи дни рождения приходятся на месяц, значение которого введено с клавиатуры;
• если таких нет, выдать на дисплей соответствующее сообщение"""

""" Задача 3
1. Описать класс с именем PRICE, содержащую следующие поля:
• TOVAR — название товара;
• MAG — название магазина, в котором продается товар;
• STOIM — стоимость товара в руб.

2. Написать программу, выполняющую следующие действия:
• ввод с клавиатуры данных в массив SPISOK, состоящий из восьми элементов типа PRICE; 
записи должны быть размещены в порядке возрастания стоимости, сортировка должна происходить в момент ввода с клавиатуры
• вывод на экран полного списка товаров по возрастанию цены"""