'''Created by Luis Gago collaborated with Ryan Balog. CS2420 Summer Block1.'''
from recursioncounter import RecursionCounter

class CourseList():
    def __init__(self):
        self.head = None

    def size(self):
        '''returns size of the linked list'''
        if self.head is None:
            return 0
        return self.__size_helper(self.head)

    def __size_helper(self, current):
        '''size helper'''
        RecursionCounter()

        if current is None:
            return 0
        return 1 + self.__size_helper(current.next)

    def calculate_gpa(self):
        '''calulates students overall gpa'''
        if self.head == None:
            return 0
        else:
            return self.__calculate_gpa_helper(self.head, 0, 0)

    def __calculate_gpa_helper(self, current, numerator, denominator):
        '''calculate gpa helper'''
        RecursionCounter()
        if current is None:
            return numerator / denominator
        numerator += current.grade() * current.credit_hr()
        denominator += current.credit_hr()
        return self.__calculate_gpa_helper(current.next, numerator, denominator)

    def is_sorted(self):
        '''determins if a linked list is sorted'''
        if self.head == None:
            return True
        return self.__is_sorted_helper(self.head)

    def __is_sorted_helper(self, current):
        '''is sorted helper'''
        RecursionCounter()
        if current.next is None:
            return True
        if current.course_no > current.next.course_no:
            return False
        return self.__is_sorted_helper(current.next)

    def insert(self, course):
        '''allows you to insert a course into the linked list'''
        if self.head == None: #if head is = to none
            self.head = course
            return None
        elif self.head.course_no > course.course_no: #if new course has a lower course #
            course.next = self.head
            self.head = course
        else:
            self.__insert_helper(self.head, self.head.next, course)

    def __insert_helper(self, prev, current, course):
        '''insert helper'''
        RecursionCounter()
        if current is None:
            prev.next = course
        elif course.course_no < current.course_no:
            prev.next = course
            course.next = current
        else:
            self.__insert_helper(current, current.next, course)

    def find(self, course_no):
        '''finds an instance of a course'''
        if self.head is None:
            return -1
        else:
            return self.__find_helper(self.head, course_no)

    def __find_helper(self, current, course_no):
        '''find helper'''
        RecursionCounter()
        if current.course_no is course_no:
            return current
        elif current.next is None:
            return -1
        else:
            return self.__find_helper(current.next, course_no)

    def remove(self, course_no):
        '''removes first occurrance of a class'''
        if self.head is None:
            return None
        elif self.head.course_no is course_no:
            self.head = self.head.next
            return None
        else:
            return self.__remove_helper(self.head, self.head.next, course_no)

    def __remove_helper(self, prev, current, course_no):
        '''remove helper function'''
        RecursionCounter()
        if current.course_no == course_no:
            prev.next = current.next
            return
        else:
            return self.__remove_helper(current, current.next, course_no)

    def remove_all(self, course_no):
        '''removes all instances of a course in linked list'''
        if self.head is None:
            return None
        if self.head.course_no is course_no:
            self.head = self.head.next
        return self.__remove_all_helper(self.head, self.head.next, course_no)

    def __remove_all_helper(self, prev, current, course_no):
        '''helper for the remove all function'''
        RecursionCounter()
        if current.course_no == course_no:
            prev.next = current.next
            if current.next is None:
                return None
            return self.__remove_all_helper(prev, current.next, course_no)
        elif current.next is None:
            return None
        else:
            return self.__remove_all_helper(current, current.next, course_no)

    def __iter__(self):
        '''allows for traversal of the linked list in a for loop'''
        cursor = self.head
        while cursor is not None:
            yield cursor
            cursor = cursor.next

    def __next__(self, current):
        '''returns the next item in the linked list'''
        return current.next

    def __str__(self):
        '''returns strings of each item in the linked list'''
        if self.head is None:
            return None
        else:
            return self.__str__helper(self.head)

    def __str__helper(self, current):
        '''str helper'''
        RecursionCounter()
        if current.next is None:
            return current.__str__()
        return current.__str__() + "\n" + self.__str__helper(current.next)
