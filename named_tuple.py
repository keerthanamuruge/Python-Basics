from collections import namedtuple
import string

num = 5

sub ='ID         MARKS      NAME       CLASS'
for i in range(num):
    pt = namedtuple('pt', sub)
    pt = ['1','97','Raymond','7']