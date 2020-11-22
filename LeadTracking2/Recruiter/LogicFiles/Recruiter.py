def GetRecruiterList():
    query = """
        SELECT 
            ID,
            first_name FirstName,
            last_name LastName,
            email Email,
            STRFTIME('%d/%m/%Y, %H:%M', date_joined) DateJoined
        FROM
            auth_user
        WHERE
            is_superuser = 0 AND
            is_staff = 1 AND
            is_active = 1
    """

    return query