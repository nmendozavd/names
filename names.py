
"""
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def show_students(arr):
     for key, data in students.keys():
          for value in data:
               print "first_name", "last_name"


def show_all(users):
    for role in users:
        counter = 0
        print role
        for person in users[role]:
            counter += 1
            first_name = person['first_name'].upper()
            last_name = person['last_name'].upper()
            length = len(first_name) + len(last_name)
            print "{} - {} {} - {}".format(counter, first_name, last_name, length)

show_students(students)
show_all(users)

"""


students = [
     {'first_name': 'Michael', 'last_name' : 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'},
]


def show_students(list):
     for val in len(students):
          for val in students[0].itervalues():
               print val
               #print "first_name", "last_name"
               #print "{}, {}".format(first_name, last_name)

show_students(students)


users = {
     'Students': [
         {'first_name': 'Michael', 'last_name': 'Jordan'},
         {'first_name': 'John', 'last_name': 'Rosales'},
         {'first_name': 'Mark', 'last_name': 'Guillen'},
         {'first_name': 'KB', 'last_name': 'Tonel'},
     ],
     'Instructors': [
         {'first_name': 'Michaek', 'last_name': 'Choi'},
         {'first_name': 'Martin', 'last_name': 'Puryear'},
     ]
}

def show_all(arr):
     for role in users:  
          counter = 0
          print role
          for person in users[role]:
               counter += 1
               first_name = person['first_name'].upper()
               last_name = person['last_name'].upper()
               length = len(first_name) + len(last_name)
               print "{} - {} {} - {}".format(counter, first_name, last_name, length)
  
#show_all(users)
