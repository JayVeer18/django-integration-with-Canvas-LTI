import canvasapi

class CanvasAPI:
    """
    A class to interact with the Canvas LMS API securely.

    This class encapsulates the logic for interacting with the Canvas API,
    providing methods to access courses, users, and assignments.

    Attributes:
        api_url (str): The base URL of the Canvas API.
        api_key (str): The Canvas API access token. (**Store securely, not here!**)
    """

    def __init__(self, api_url, api_key):
        """
        Initializes the CanvasAPI object.

        Args:
            api_url (str): The base URL of the Canvas API.
            api_key (str): The Canvas API access token. (**Store securely, not here!**)
        """

        self.api_url = api_url
        self._api_key = api_key

    def get_course(self, course_id):
        """
        Retrieves a course by its ID.

        Args:
            course_id (int): The ID of the course to retrieve.

        Returns:
            canvasapi.course.Course: The retrieved course object.
        """

        canvas = canvasapi.Canvas(self.api_url, self._api_key)
        return canvas.get_course(course_id)

    def get_users(self, course_id):
        """
        Retrieves all users in a course.

        Args:
            course_id (int): The ID of the course to retrieve users from.

        Returns:
            list: A list of canvasapi.user.User objects.
        """

        course = self.get_course(course_id)
        return course.get_users()

    def get_assignments(self, course_id):
        """
        Retrieves all assignments in a course.

        Args:
            course_id (int): The ID of the course to retrieve users from.

        Returns:
            list: A List of all the assignments in this course.
        """

        course = self.get_course(course_id)
        return course.get_assignments()

    def get_user(self, user_id):
        """
        Retrieves a user by their ID.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            canvasapi.user.User: The retrieved user object.
        """

        canvas = canvasapi.Canvas(self.api_url, self._api_key)
        return canvas.get_user(user_id)

    def get_user_courses(self, user_id):
        """
        Retrieves a list of courses a user is enrolled in.

        Args:
            user_id (int): The ID of the user.

        Returns:
            list: A list of canvasapi.course.Course objects.
        """

        user = self.get_user(user_id)
        return user.get_courses()

    def get_user_assignments(self, user_id, course_id):
        """
        Retrieves a list of assignments for a user in a specific course.

        Args:
            user_id (int): The ID of the user.
            course_id (int): The ID of the course to retrieve assignments from.

        Returns:
            list: A list of canvasapi.assignment.Assignment objects.
        """

        user = self.get_user(user_id)
        return user.get_assignments(course_id)