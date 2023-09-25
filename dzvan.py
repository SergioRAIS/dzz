from random import randint
m_set = set(randint(1, 19) 
            for i in range(int(input('Введите кол-во  первого множества:'))))
print(m_set)
m_set = set(randint(1, 19) 
            for i in range(int(input('Введите кол-во  второго множества:'))))
print(m_set)
sc_set = sorted(m_set.intersection(m_set))
print(*sc_set)