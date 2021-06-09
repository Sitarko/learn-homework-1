"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
scorebook = [
    {'school_class': '4a', 'scores': [3,4,4,5]},
    {'school_class': '3б', 'scores': [4,4,2,5,2]},
    {'school_class': '8г', 'scores': [3,1,4,5,2,3]},
    {'school_class': '1к', 'scores': [3,4,4,5,1,4,4]},
    {'school_class': '5е', 'scores': [3,4,4,5,2]},
    {'school_class': '5у', 'scores': [3,4,4,5,4,2,5,4]},
    {'school_class': '6г', 'scores': [3,4,4,5,5]}
]

def avg_school_score (classes):
    scores = []
    for school_class in scorebook:
        scores.extend(school_class['scores'])
    avg_school_scores = sum(scores)/len(scores)
    return (round(avg_school_scores,2))

def main():
    for i in range(len(scorebook)):
        class_name = scorebook[i]['school_class']
        avg_class_scores = sum(scorebook[i]['scores'])/(len(scorebook[i]['scores']))
        print ((f'Средний балл {class_name} класса: ' + str(round(avg_class_scores,2))))
    print ('Средний балл по всей школе: ' + str(avg_school_score(scorebook)))
   
if __name__ == "__main__":
    main()
