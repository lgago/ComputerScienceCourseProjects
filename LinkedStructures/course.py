'''By Luis Gago collaborated with Ryan Balog. CS2420 Summer Block1.'''
class Course():
    '''Node Class'''
    def __init__(self, course_no=0, course_name="", course_credit_hours=0.0, course_grade=0.0, next=None):
        '''init function for Course'''
        if not isinstance(course_no, int):
            raise ValueError('error, course number must be an integer')
        if course_no < 0:
            raise ValueError('error, course number must be greater than zero')
        if not isinstance(course_name, str):
            raise ValueError('error, course name must be a string')
        if not isinstance(course_grade, float):
            raise ValueError('error, course grade must be a float')
        if course_grade < 0:
            raise ValueError('error course grade must be greater than zero')
        if not isinstance(course_credit_hours, float):
            raise ValueError('error, course credit hours must be a float')
        if course_credit_hours < 0:
            raise ValueError('error, credit hours must be greater than zero')
        self.course_no = course_no
        self.course_name = course_name
        self.course_credit_hours = course_credit_hours
        self.course_grade = course_grade
        self.next = next

    def number(self):
        '''returns number'''
        return self.course_no

    def name(self):
        '''returns name'''
        return self.course_name

    def credit_hr(self):
        '''returns credit hours'''
        return self.course_credit_hours

    def grade(self):
        '''returns grade'''
        return self.course_grade

    def __str__(self):
        '''returns string'''
        return f"cs{self.course_no} {self.course_name} Grade:{self.course_grade} Credit Hours: {self.course_credit_hours}"
