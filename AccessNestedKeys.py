data = {
  'students': [
    {
      'name': 'Josephine',
      'subjects': [
        {
          'name': 'English',
          'teacher': 'Mr. Hoover'
        }
      ]
    },
    {
      'name': 'Luke',
      'subjects': [
        {
          'name': 'History',
          'teacher': 'Mrs. Peters'
        }
      ]
    },
    {
      'name': 'Julia',
      'subjects': [
        {
          'name': 'Chemistry',
          'teacher': 'Mrs. Fauci'
        }
      ]
    }
  ]
}



def get(data1,string):

  if int(string[9])<4 and int(string[9])>=0:
    number = string[9]
  else:
    print('out of range!')

  students=data1['students']
  studentNumber=students[int(number)]
  # studentName=studentNumber['name']
  if string[22]=='n':
    subjectName=studentNumber['subjects'][0]['name']
    print(subjectName)
  if string[22]=='t':
    teacherName=studentNumber['subjects'][0]['teacher']
    print(teacherName)
number=int(input('Enter the number of the student: '))
case1=input('Which case do you want to check? subject name: "n" or teacher of this subject "t": ')
example=f'students.{number-1}.subjects.0.{case1}'
get(data,example)
get(data, 'students.0.subjects.0.teacher')