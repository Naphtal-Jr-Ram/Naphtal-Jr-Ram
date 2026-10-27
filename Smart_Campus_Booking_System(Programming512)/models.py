class User:

    def __init__(
            self,
            username,
            password,
            campus):

        self._username = username
        self._password = password
        self._campus = campus


class Lecturer(User):

    role = "Lecturer"


class CampusAdministrator(User):

    role = "Admin"


class SystemOperator(User):

    role = "Operator"


class Resource:

    def __init__(
            self,
            code,
            name,
            campus):

        self.code = code
        self.name = name
        self.campus = campus


class Booking:

    def __init__(
            self,
            lecturer,
            resource,
            date,
            time,
            duration):

        self.lecturer = lecturer
        self.resource = resource
        self.date = date
        self.time = time
        self.duration = duration