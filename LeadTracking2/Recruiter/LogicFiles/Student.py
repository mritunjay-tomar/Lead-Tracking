from Recruiter.models import Student, StudentArchives


def GetStudentSQL():
    query = """
        SELECT 
            student.ID, 
            student.FirstName || ' ' || student.MiddleName || '' ||student.LastName Name, 
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


def GetArchiveStudentSQL():
    query = """
        SELECT 
            student.ID, 
            student.FirstName || ' ' || student.MiddleName || '' ||student.LastName Name, 
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
            Recruiter_studentarchives student;
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


def StudentArchive(StudentID):
    student = Student.objects.filter(ID=StudentID).first()
    archive = StudentArchives()
    archive.FirstName = student.FirstName
    archive.MiddleName = student.MiddleName
    archive.LastName = student.LastName
    archive.Email = student.Email
    archive.PhoneNumber = student.PhoneNumber
    archive.UserSavedBy = student.UserSavedBy
    archive.country = student.country
    archive.StatusChangedBy = student.StatusChangedBy
    archive.save()
    student.delete()


def RemoveStudentFromArchive(StudentID):
    archive = StudentArchives.objects.filter(ID=StudentID).first()
    student = Student()
    student.FirstName = archive.FirstName
    student.MiddleName = archive.MiddleName
    student.LastName = archive.LastName
    student.Email = archive.Email
    student.PhoneNumber = archive.PhoneNumber
    student.UserSavedBy = archive.UserSavedBy
    student.country = archive.country
    student.StatusChangedBy = archive.StatusChangedBy
    student.save()
    archive.delete()
