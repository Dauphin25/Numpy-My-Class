from enum import Enum


class SUBJECTS(Enum):
    NOTHING = 0
    MATH = 1
    SCIENCE = 2
    HISTORY = 3
    ENGLISH = 4
    ART = 5
    MUSIC = 6
    PHYSICAL_EDUCATION = 7
    SPANISH = 8
    FRENCH = 9
    GERMAN = 10

    @staticmethod
    def names():
        return [subject.name for subject in SUBJECTS]

    @staticmethod
    def list_names():
        ans = []
        for subject in SUBJECTS:
            ans.append([subject.name])
        return ans
