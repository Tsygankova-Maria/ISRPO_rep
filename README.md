# Geometric ISRPO_rep

## Общее описание

**Geometric ISRPO_rep** — учебная библиотека для вычисления площади и периметра
базовых геометрических фигур: круга, квадрата, прямоугольника и треугольника.

Каждая фигура вынесена в отдельный модуль:

| Модуль          | Фигура         | Функции                    |
|-----------------|----------------|----------------------------|
| `circle.py`     | Круг           | `area(r)`, `perimeter(r)`  |
| `square.py`     | Квадрат        | `area(a)`, `perimeter(a)`  |
| `rectangle.py`  | Прямоугольник  | `area(a, b)`, `perimeter(a, b)` |
| `triangle.py`   | Треугольник    | `area(a, h)`, `perimeter(a, b, c)` |


### Структура проекта	geometric_lib/
├── circle.py
├── square.py
├── rectangle.py
├── triangle.py
├── docs/
│ └── README.md
├── README.md
└── .gitignore


### Требования

- Python 3.8+
- Внешних зависимостей нет (используется только стандартная библиотека).

