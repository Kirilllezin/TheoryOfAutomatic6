from prettytable import PrettyTable


class Automat:
    def __init__(self, vertex, zero, one):
        self.vertex = vertex
        self.zero = zero
        self.one = one

        self.include = []


def add(i, graphTable, eIndx, alphabetQ):
    res = []
    for k in graphTable[i][eIndx]:
        if k == '0':
            res.append('0')
            break
        res.append(k)
        nextIndx = alphabetQ.index(k)
        res2 = add(nextIndx, graphTable, eIndx, alphabetQ)
        for j in res2:
            if j == '0':
                continue
            res.append(j)
    return res


def countValue(alphabet, alphabetQ, graphTable, q, val):
    res = []
    stop = False
    isGo = False
    indxQ = alphabetQ.index(q)
    indxVal = alphabet.index(val)
    for a in alphabet:
        if a == 'E' or a == 'E':
            eIndx = alphabet.index(a)

    # 1
    if graphTable[indxQ][indxVal] != '0':
        res.append(graphTable[indxQ][indxVal])
        indxQ = alphabetQ.index(graphTable[indxQ][indxVal])
        isGo = True
    if isGo:
        tempRes = add(indxQ, graphTable, eIndx, alphabetQ)
        for k in tempRes:
            if k == '0':
                continue
            res.append(k)

    # 2
    indxQ = alphabetQ.index(q)
    indxVal = alphabet.index(val)
    isGo1 = False
    isGo = False

    for d in graphTable[indxQ][eIndx]:
        if d != '0':
            indxQ = alphabetQ.index(d)
            isGo1 = True
        if isGo1:
            if graphTable[indxQ][indxVal] != '0':
                res.append(graphTable[indxQ][indxVal])
                isGo = True
        if isGo:
            for s in graphTable[indxQ][eIndx]:
                while True:
                    if s == '0':
                        break
                    res.append(s)
                    indxQ = alphabetQ.index(s)
    return res


def countValueForP(i, val, sTable, alphabet2):
    res = set()
    tempRes = sTable[i][alphabet2.index(val)]
    for i in tempRes:
        res.add(i)
    return res


# Ввод алфавита входных символов
flag = False
while True:
    inputData = input("Введите все символы алфавита подряд без пробелов:")
    alphabet = list(inputData) + ['E']

    # Проверки алфавита

    if len(alphabet) < 2:
        print("Алфавит содержит менее 2 элементов. Повторите ввод:")
        continue

    flag = False
    for i in alphabet:
        if i == 'q':
            print("Алфавит не должен содержать q, т.к. через него обозначаются состояния. Повторите ввод:")
            flag = True
            break
        if i == ' ':
            print("Алфавит содержит пробел. Повторите ввод:")
            flag = True
            break
        if alphabet.count(i) > 1:
            print("Алфавит содержит повторяющиеся элементы. Повторите Ввод:")
            flag = True
            break
    if flag:
        continue

    flag3 = True
    for i in alphabet:
        if i == 'E' or i == "Е":
            flag3 = False
    if flag3:
        print("В алфавите нет Е. Повторите ввод:")
        continue

    flag2 = False
    print(alphabet[:-1])
    while True:
        isContinue = input("Продолжить с этим алфавитом? Введите 1, чтобы продолжить, или 0, чтобы повторить ввод.\n")
        if isContinue == "1":
            break
        if isContinue == "0":
            flag2 = True
            break
        else:
            print("Можно ввести только 1 или 0. Повторите выбор:")
            continue
    if flag2:
        continue

    if int(isContinue):
        break

# Ввод состояний q

while True:
    inputData = input("Введите все состояния q подряд через пробел:")
    alphabetQ = inputData.split()

    # Проверки
    if len(alphabetQ) < 2:
        print("Алфавит содержит менее 2 элементов. Повторите ввод:")
        continue

    flag = False
    for i in alphabetQ:
        if len(i) < 2:
            print("Состояния должны начинаться с q и заканчиваться цифрой. Повторите ввод:")
            flag = True
            break
        elif not i[1].isnumeric():
            print("Состояния должны начинаться с q и заканчиваться цифрой. Повторите ввод:")
            flag = True
            break
        if i[0] != 'q':
            print("Состояния должны начинаться с q и заканчиваться цифрой. Повторите ввод:")
            flag = True
            break
        if alphabetQ.count(i) > 1:
            print("Алфавит содержит повторяющиеся элементы. Повторите Ввод:")
            flag = True
            break
    if flag:
        continue

    flag2 = False
    print(alphabetQ)
    while True:
        isContinue = input("Продолжить с этим алфавитом? Введите 1, чтобы продолжить, или 0, чтобы повторить ввод.\n")
        if isContinue == "1":
            break
        if isContinue == "0":
            flag2 = True
            break
        else:
            print("Можно ввести только 1 или 0. Повторите выбор:")
            continue
    if flag2:
        continue

    if int(isContinue):
        break

# ВЫбор начальной и конечной вершин

startVertex = []
while True:
    inputDt = input("Укажите какая вершина является начальной:")
    startVertex.append(inputDt)

    flag = True
    for i in alphabetQ:
        if i == inputDt:
            flag = False
            break
    if flag:
        print("Данной вершины нет в указанном графе. Повторите ввод этой вершины")
        continue
    while True:
        choice = input("Закончить ввод начальных вершин? Да - 1, Нет - 0: ")
        if choice == "1":
            break
        if choice == "0":
            flag2 = True
            break
        else:
            print("Можно ввести только 1 или 0. Повторите выбор:")
            continue
    if choice == '1':
        break

endVertex = []
while True:
    inputDt2 = input("Укажите какая вершина является конечной:")
    endVertex.append(inputDt2)

    flag = True
    for i in alphabetQ:
        if i == inputDt2:
            flag = False
            break
    if flag:
        print("Данной вершины нет в указанном графе. Повторите ввод этой вершины")
        continue
    while True:
        choice = input("Закончить ввод конечных вершин? Да - 1, Нет - 0: ")
        if choice == "1":
            break
        if choice == "0":
            flag2 = True
            break
        else:
            print("Можно ввести только 1 или 0. Повторите выбор:")
            continue
    if choice == '1':
        break

#Создаем массив, который хранит граф
graphTable = []
for i in range(len(alphabetQ)):
    graphTable.append([0] * len(alphabet))

# Заполнение таблицы, которая описывает граф
for (i, a) in zip(alphabetQ, range(len(alphabetQ))):
    for (j, b) in zip(alphabet, range(len(alphabet))):
        while True:
            if j != 'E':
                currentValue = input \
                    ("Введите в какое состояние можно пойти из {} по {} :".format(i,j) )
            elif j == 'E':
                currentValue = '0'
            if ((inputData.find(currentValue) == -1) and (currentValue != '0')) or currentValue == 'q':
                print("Данной вершины нет в графе. Введите корректную вершину:")
                continue
            break
        if j == 'E' or j == 'Е':
            if currentValue == '0':
                graphTable[a][b] = ['0']
            else:
                graphTable[a][b] = currentValue.split()
        else:
            graphTable[a][b] = currentValue


# Вывод таблицы графа
mytable = PrettyTable()
columns = alphabet.copy()  # list
columns.insert(0, "Состояние")
mytable.field_names = columns[:len(columns) - 1]
for i in range(len(alphabetQ)):
    strName = alphabetQ[i]
    string = graphTable[i].copy()  #
    string = string[:len(string) - 1]  #
    string.insert(0, strName)
    mytable.add_row(string)
print(mytable)

# Создание массива для Е-замыканий
eTable = []
for i in range(len(alphabetQ)):
    eTable.append([])

# Нахождение Е-замыканий (Дописать в начале проверку на наличие эпсилонов)
for a in alphabet:
    if a == 'E' or a == 'E':
        eIndx = alphabet.index(a)

for i in range(len(alphabetQ)):
    eTable[i].append(alphabetQ[i])
    j = i
    if graphTable[j][eIndx][0] == '0':
        continue
    else:
        res = add(i, graphTable, eIndx, alphabetQ)
        for k in res:
            eTable[i].append(k)

#  Создание масиива для хранения таблицы с S
sTable = []
for i in range(len(eTable)):
    sTable.append([0] * (len(alphabet) - 1))

# Подсчет значений для таблицы S
tempData = set()
res = []
curElem = []
for i in range(len(alphabetQ)):
    for k in alphabet:
        if k == "E":
            continue
        for j in range(len(eTable[i])):
            res.append(countValue(alphabet, alphabetQ, graphTable, eTable[i][j],
                                  k))
        for f in res:
            for g in f:
                tempData.add \
                    (g)

        # Проверка на вложенность
        column = alphabet.index(k)
        if len(tempData) == 0:
            curElem.append('0')
            sTable[i][column] = curElem
        else:
            for w in range(len(eTable)):
                is_subset = False
                is_subset = set(eTable[w]).issubset(tempData)
                if is_subset:
                    curElem.append("S" + str(w))
            sTable[i][column] = curElem
        res = []
        curElem = []
        tempData = set()

# Вывод таблицы с S
alphabet2 = alphabet.copy()
alphabet2.remove('E')
mytable2 = PrettyTable()
columns2 = alphabet2.copy()
columns2.insert(0, "Состояние")
mytable2.field_names = columns2
for i in range(len(alphabetQ)):
    strName2 = "S" + str(i)
    string2 = sTable[i].copy()
    string2.insert(0, strName2)
    mytable2.add_row(string2)
print(mytable2)

# Определение начального состояния

# Добавление начальных вершин, которые можно достичь по Е-переходу
startVertex = set(startVertex)
tempRes = []
for j in startVertex:
    elem = j
    indx = alphabetQ.index(elem)
    for i in eTable[indx]:
        tempRes.append(i)
for i in tempRes:
    startVertex.add(i)

# Добавление конечных вершин, которые можно достичь по Е-переходу
endVertex = set(endVertex)
tempRes = []
for j in endVertex:
    elem = j
    indx = alphabetQ.index(elem)
    for i in eTable[indx]:
        tempRes.append(i)
for i in tempRes:
    endVertex.add(i)

# Определение начальных S
startS = set()
for i in startVertex:
    for j in eTable:
        for k in j:
            if k == i:
                startS.add("S" + str(eTable.index(j)))

# Определение конечных S
endS = set()
for i in endVertex:
    for j in eTable:
        for k in j:
            if k == i:
                endS.add("S" + str(eTable.index(j)))

# Создание начального списка, который будет хранить из чего состоят элементы P
pByS = []
pByS.append(list(startS))

# Создание начальной таблицы для хранения P
pTable = []
pTable.append([0] * len(alphabet2))

# Нахождение элементов таблицы P
res = set()
count = 0
for i in pByS:
    i = pByS.index(i)
    for k in alphabet2:
        for j in pByS[i]:
            tempRes = countValueForP(int(j[-1]), k, sTable, alphabet2)
            for w in tempRes:
                if w == '0':
                    continue
                res.add(w)
        for t in res:
            if t == '0':
                count += 1
        if count == len(res):
            curElem = '0'
        else:
            localFlag = True
            for w in pByS:
                if set(w) == res:
                    localFlag = False
                    curElem = "P" + str(pByS.index(w))
            if localFlag:
                curElem = "P" + str(len(pByS))
                pByS.append(list(res))
                pTable.append([0] * len(alphabet2))
        pTable[i][alphabet2.index(k)] = curElem  # Заполнение таблицы P
        res = set()

# Вывод таблицы P
MinimizeAlphabet = []
AutomatVertex = []
mytable3 = PrettyTable()
columns3 = alphabet2.copy()
columns3.insert(0, "Состояние")
mytable3.field_names = columns3
for i in range(len(pByS)):
    strName3 = "P" + str(i)
    string3 = pTable[i].copy()
    string3.insert(0, strName3)
    mytable3.add_row(string3)
    MinimizeAlphabet.append(strName3)  # Новый алфавит для 6 задания (После минимизации исходного автомата)
    strName3 = Automat(("P" + str(i)), string3[1], string3[2])  # Заполнение класса для 6 задания
    AutomatVertex.append(strName3)
print(mytable3)
# Определение начальных P
counter = 0
for j in pByS:
    if set(j) == startS:
        startP = "P" + str(counter)
    else:
        counter += 1

# Определение конечных P
endP = set()
for i in endS:
    for j in pByS:
        for k in j:
            if k == i:
                endP.add("P" + str(pByS.index(j)))

print("Начальные состояния q:", startVertex)
print("Конечные состояния q:", endVertex, '\n')
print("Начальные состояния S:", startS)
print("Конечные состояния S:", endS, '\n')
print("Начальные состояния Р:", startP)
print("Конечные состояния P:", endP)

# Первый класс
previous_class = ([list(endP), (list(set(MinimizeAlphabet) - endP))])
class_metka = 0
print("\nКласс эквиваленции {}{}".format(str(class_metka), ':'), previous_class)
# Устанавливаем названия подклассам первого класса
subcls_names = []


equal = False
while (not equal):
    # Обработка нечётных классов
    next_class = []
    rebuild_class = []
    slice_class = []
    all_slice_class = []
    all_rebuild_class = []
    # Cмотрим нечетный класс
    # Выбираем подкласс класса
    for subcls in previous_class:
        # Если в подклассе 1 элемент, то его не надо разбивать
        if len(subcls) > 1:
            for element in subcls:
                for current in range(len(AutomatVertex)):
                    # Ищем вершину вершину из подкласса в Automat
                    if AutomatVertex[current].vertex == element:
                        # Проверяем, полученные элементы по путям 0/1 принадлежат этому же классу
                        if ((AutomatVertex[current].zero) in subcls) and ((AutomatVertex[current].one) in subcls):
                            rebuild_class.append(element)

                        # Иначе отправляем в класс срез
                        else:
                            slice_class.append(element)



                    else:
                        continue

        else:
            rebuild_class.append(subcls[0])

        # Перестроенный класс
        if len(rebuild_class) > 0:
            next_class.append(rebuild_class)
            all_rebuild_class.append(rebuild_class)
        if len(slice_class) > 0:
            next_class.append(slice_class)
            all_slice_class.append(slice_class)


        # Очищаем массивы под новые итеррации
        rebuild_class = []
        slice_class = []


    class_metka += 1
    print("Класс эквиваленции {}{}".format(str(class_metka), ':'), next_class)

    # Обработка чётных классов next_class
    new_next_class = []

    # Добавляем все неразбитые классы
    for i in range(len(all_rebuild_class)):
        new_next_class.append(all_rebuild_class[i])

    # Пересобираем разбитые классы
    for subcls in all_slice_class:
        notsliced = []
        if len(subcls) > 1:
            for element in subcls:  # Элемент разбитого класса

                # Ищем данный элемент во всех вершинах
                for current in range(len(AutomatVertex)):
                    if AutomatVertex[current].vertex == element:

                        # Проверяем, что данный элемент, полученный при разбитии по 0/1, принадлежит одному начальному классу (ДО КАКОГО ЛИБО РАЗБИТИЯ)
                        for subcls2 in previous_class:
                            if (AutomatVertex[current].zero in subcls2) and (AutomatVertex[current].one in subcls2):
                                notsliced.append(element)

                            elif (AutomatVertex[current].zero in subcls2 and AutomatVertex[
                                current].one not in subcls2) or (
                                    AutomatVertex[current].zero not in subcls2 and AutomatVertex[
                                current].one in subcls2):
                                new_next_class.append([element])
                            else:
                                continue
                    else:
                        continue



        else:
            new_next_class.append(subcls)
            continue

        if len(notsliced) > 0:
            new_next_class.append(notsliced)

    # Убираем повторные доваления классов, которые были разбиты ни раз
    unique_subcls = []

    for subcls in new_next_class:
        if subcls not in unique_subcls:
            unique_subcls.append(subcls)

    new_next_class = []
    for i in range(len(unique_subcls)):
        new_next_class.append(unique_subcls[i])

    # Сравниваем классы эквиваленции. Если последние два класса равны, то завершаем цикл
    if new_next_class == next_class:
        class_metka += 1
        print("Класс эквиваленции {}:".format(str(class_metka)),next_class)
        print("Класс эквиваленции {} и класс эквиваленции {} равны".format(str(class_metka), str(class_metka - 1)))
        equal = True
        last_class = new_next_class

    else:
        class_metka += 1
        previous_class = new_next_class

# Выдаём новые имена вершинам автомата
new_vertexes = []
for subcls in last_class:
    new_vertexes.append('[' + subcls[0] + ']')
print("\nНовые вершины {}".format(','.join(map(str, new_vertexes))))

# Задаём новым вершинам пути старых
new_AutomatVertex = []
for current in range(len(new_vertexes)):
    for current2 in range(len(AutomatVertex)):
        if '[' + AutomatVertex[current2].vertex + ']' == new_vertexes[current]:
            new_AutomatVertex.append(
                Automat(new_vertexes[current], AutomatVertex[current2].zero, AutomatVertex[current2].one))
# Прописываем какие ещё "cтарые" вершины содержат в себе "новые" вершины
# Выбираем класс из которого мы извлекли вершину для нового класса
for subcls in last_class:
    # Cмотрим, чтобы его длинна была > 0
    if len(subcls) > 0:
        for element in subcls:
            #Переменная для проверки правильной вершины
            check = subcls[0]
            for newVertex in range(len(new_AutomatVertex)):
                #Проверка, чтобы добавить include нужной вершине новго автомата
                if new_AutomatVertex[newVertex].vertex == '['+check+']':
                    new_AutomatVertex[newVertex].include.append(element)
                else:
                    continue

    else:
        continue

#Вывод содержимого старых вершин в новых
print("\nСодержимое новых вершин:")
for i in range(len(new_AutomatVertex)):
    print("new_Vertex {} include {}".format(new_AutomatVertex[i].vertex,new_AutomatVertex[i].include))

#Построение новой таблицы графа
ways = [] #P0....Pj

for vertex in range(len(new_AutomatVertex)):
    buffer = [0,0]
    if (('[' + new_AutomatVertex[vertex].zero + ']') in new_vertexes) and (('[' + new_AutomatVertex[vertex].one + ']') in new_vertexes):
        ways.append(['['+new_AutomatVertex[vertex].zero+']', '['+new_AutomatVertex[vertex].one+']'])


    elif ('['+new_AutomatVertex[vertex].zero+']' not in new_vertexes) and ('['+new_AutomatVertex[vertex].one+']' in new_vertexes):
        for findVertexInclude in range(len(new_AutomatVertex)):
            if (new_AutomatVertex[vertex].zero) in (new_AutomatVertex[findVertexInclude].include):
                ways.append([new_AutomatVertex[findVertexInclude].vertex, '['+new_AutomatVertex[vertex].one+']'])


    elif ('[' + new_AutomatVertex[vertex].one + ']' not in new_vertexes) and ( '[' + new_AutomatVertex[vertex].zero + ']' in new_vertexes):
        for findVertexInclude in range(len(new_AutomatVertex)):
            if (new_AutomatVertex[vertex].one) in (new_AutomatVertex[findVertexInclude].include):
                ways.append(['[' + new_AutomatVertex[vertex].zero + ']',new_AutomatVertex[findVertexInclude].vertex])

    elif ('[' + new_AutomatVertex[vertex].one + ']' not in new_vertexes) and ( '[' + new_AutomatVertex[vertex].zero + ']' not in new_vertexes):
        for findVertexInclude in range(len(new_AutomatVertex)):
            if (new_AutomatVertex[vertex].zero) in (new_AutomatVertex[findVertexInclude].include):
                buffer[0]=(new_AutomatVertex[findVertexInclude])

            elif (new_AutomatVertex[vertex].one) in (new_AutomatVertex[findVertexInclude].include):
                buffer[1] = (new_AutomatVertex[findVertexInclude])
        ways.append(buffer)

#Вывод нового графа
mytable3 = PrettyTable()
columns3 = alphabet2.copy()
columns3.insert(0, "Состояние")
mytable3.field_names = columns3
for i in range(len(ways)):
    strName3 = new_vertexes[i]
    string3 = ways[i].copy()s
    string3.insert(0, strName3)
    mytable3.add_row(string3)
print(mytable3)


