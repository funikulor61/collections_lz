import numpy as np                                        #Импорты библиотек
import matplotlib.pyplot as plt
x = np.linspace(-10,15,25)                                #Задаем диапазон x и количество точек
y = x**3 - (6 * x**2) + (11 * x) - 6                      #Сама функция
plt.plot(x, y)                                            #Создание графика
plt.show()                                                #Показ графика