import math

def area(r):
    '''
    Принимает радиус r, возвращает площадь круга.

	    Параметры:
      		r (float|int): радиус круга

    	Возвращаемое значение:
        	area (float): площадь круга

    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает радиус r, возвращает длину окружности.

    	Параметры:
        	r (float|int): радиус круга

    	Возвращаемое значение:
        	perimeter (float): длина окружности
    '''
    return 2 * math.pi * r
