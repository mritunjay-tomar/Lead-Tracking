from Recruiter.models import Student


def GetStudentSQL():
    query = """
        SELECT 
            student.ID, 
            student.FirstName || ' ' || student.LastName Name, 
            student.Email, 
            student.PhoneNumber, 
            CASE student.Status 
                WHEN 1 THEN 'INITIAL' 
                WHEN 2 THEN 'CONVERTED' 
                ELSE 'BLANK' 
            END Status,
            student.statusChangedBy StatusChangedBy,
            student.country Country,
            0 Button
        FROM 
            Recruiter_student student;
    """

    return query


def GetPhoneNumberWithAltNumber(PhoneNo, AltNumber):
    if AltNumber == '':
        return PhoneNo
    else:
        return PhoneNo + ', ' + AltNumber


def ConvertStudent(studentID, user_name):
    student = Student.objects.filter(ID=studentID).first()
    student.Status = 2
    student.StatusChangedBy = user_name
    student.save()


def ReInitializeStudent(studentID):
    student = Student.objects.filter(ID=studentID).first()
    student.Status = 1
    student.StatusChangedBy = ''
    student.save()
    return "'"+student.FirstName + ' ' + student.LastName+"'"


def DeleteStudent(studentID):
    student = Student.objects.filter(ID=studentID).first()
    student.delete()