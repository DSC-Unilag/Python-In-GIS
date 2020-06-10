def course(course_no):
    course_room = {'CS101': '3004', 'CS102': '4501', 'CS103': '6755', 'NT110': '1244', 'CM241': '1411'}
    course_instructor = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}
    course_time = {'CS101': '8:00 a.m.', 'CS102': '9:00 a.m.', 'CS103': '10:00 a.m.', 'NT110': '11:00 a.m.', 'CM241': '1:00 p.m.'}
    return f'Course room: {course_room.get(course_no)}\nInsructor: {course_instructor.get(course_no)}\nMeeting time: {course_time.get(course_no)}'
print(course('CS101'))