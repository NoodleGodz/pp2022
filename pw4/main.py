from pw4.input import *
from pw4.output import *
from pw4.domains.Lists import *


def main():
    a=student_list()
    b=course_list()
    while True:
        Switch(get_case())
