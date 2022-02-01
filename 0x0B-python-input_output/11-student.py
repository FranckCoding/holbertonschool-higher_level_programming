#!/usr/bin/python3
'''
module for the class student
'''


class Student():
    '''
    define a studen

    Attributes
    ----------
    first_name
        the first name of student
    last_name
        the last name of student
    age
        the age of student

    Methods
    -------
    to_json(self)
        return a dictionary representation of a Student instance
    reload_from_json(self, json)
        set new values for student
    '''

    def __init__(self, first_name, last_name, age):
        '''Init method for student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''return a dictionary representation of a Student instance'''
        if attrs is None:
            return vars(self)
        return dict((n, getattr(self, n)) for n in dir(self) if n in attrs)

    def reload_from_json(self, json):
        '''
        replaces all attributes of the Student instance

        Parameter
        ---------
        json : dict
            new values for the student
        '''

        for key in json:
            setattr(self, key, json[key])
