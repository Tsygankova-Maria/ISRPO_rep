# Geometric ISRPO_rep

## Общее описание

**Geometric ISRPO_rep** — учебная библиотека для вычисления площади и периметра
базовых геометрических фигур: круга, квадрата, прямоугольника и треугольника.

## Возможности

- Площадь и периметр **круга** — `circle.py`
- Площадь и периметр **квадрата** — `square.py`
- Площадь и периметр **прямоугольника** — `rectangle.py`
- Площадь и периметр **треугольника** - `triangle.py`


Каждая фигура вынесена в отдельный модуль:

| Модуль          | Фигура         | Функции                    |
|-----------------|----------------|----------------------------|
| `circle.py`     | Круг           | `area(r)`, `perimeter(r)`  |
| `square.py`     | Квадрат        | `area(a)`, `perimeter(a)`  |
| `rectangle.py`  | Прямоугольник  | `area(a, b)`, `perimeter(a, b)` |
| `triangle.py`   | Треугольник    | `area(a, h)`, `perimeter(a, b, c)` |



## Установка

```bash
git clone https://github.com/<ваш_логин>/geometric_lib.git
cd geometric_lib
```

## Быстрый старт

```python
import circle
import square
import rectangle
import triangle

print(circle.area(5))               # 78.53981633974483
print(circle.perimeter(5))          # 31.41592653589793
print(square.area(4))               # 16
print(square.perimeter(4))          # 16
print(rectangle.area(3, 4))         # 12
print(rectangle.perimeter(3, 4))    # 14
print(triangle.area(4, 3))          # 6.0
print(triangle.perimeter(3, 4, 5))  # 12
```

## Структура проекта

```
geometric_lib/
├── circle.py          # площадь и периметр круга
├── square.py          # площадь и периметр квадрата
├── rectangle.py       # площадь и периметр прямоугольника
├── triangle.py        # площадь и периметр треугольника
├── docs/
│   └── README.md      # подробная документация проекта
├── README.md          # этот файл
└── .gitignore         # исключения для Git
```

## Документация

Подробная документация находится в файле [`docs/README.md`](docs/README.md)
и включает:

- общее описание решения;
- описание каждой функции с примерами вызова;
