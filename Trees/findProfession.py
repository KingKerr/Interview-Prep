"""
Consider a family of Engineers and Doctors. This family has the following rules:
-- Everyone has two children
-- The first child of an Engineer is an Engineer and the second child is a Doctor.
-- The first child of an Doctor is a Doctor and the second child is an Engineer.
-- All generations of Doctors and Engineers start with an Engineer

"""

def findProfession(level, pos):

    if level == 1:
        return 'Engineer'
    else:
        parent = findProfession(level - 1, (pos + 1) // 2)

        if parent == 'Engineer' and (pos - 1) % 2 == 0:
            return 'Engineer'
        elif parent == 'Engineer' and (pos - 1) % 2 == 1:
            return 'Doctor'
        elif parent == 'Doctor' and (pos - 1) % 2 == 0:
            return 'Doctor'
        elif parent == 'Doctor' and (pos - 1) % 2 == 1:
            return 'Engineer'

