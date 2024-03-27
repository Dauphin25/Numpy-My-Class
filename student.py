import subjects
import random as rnd
import data
import numpy as np


class Student:
    def __init__(self, name=None, surname=None, subject_points=None):
        self.name = np.random.choice(data.geo_names) if name is None else name
        self.surname = np.random.choice(data.geo_surnames) if surname is None else surname
        if subject_points is None:
            self.subject_points = {subject: rnd.randint(0, 100) for subject in subjects.SUBJECTS.names()
                                   if subject != 'NOTHING'}

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_grades(self):
        my_grades = list(self.subject_points.values())
        ans = []
        for grade in my_grades:
            ans.append([grade])
        return ans

    def __repr__(self):
        return f'{self.get_full_name()} - {self.subject_points}'
