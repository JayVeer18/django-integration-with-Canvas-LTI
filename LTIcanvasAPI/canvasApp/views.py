from django.http import HttpResponse
from canvasApp.canvas_api import CanvasAPI

import dotenv
import os
dotenv.load_dotenv()

# Canvas API URL
API_URL = "https://canvas.instructure.com/"
# Canvas API key
API_KEY = api_key = os.environ.get('CANVAS_API_KEY')


# Create your views here.
def index(request):
    canvas = CanvasAPI(API_URL,API_KEY)

    # current course
    course_id = request.POST["custom_course_id"]
    course = canvas.get_course(course_id)
    course_name = course.name

    # current user
    user_id = request.POST["custom_user_id"]
    user = canvas.get_user(user_id)
    user_name = user.name

    # Welcome message
    welcome_message = f"<p>Welcome <b>{user_name}</b> to the course : <b>{course_name}</b>, Its good to see you here.</p>"

    # all the users enrolled in current course
    user_dict = {}
    user_names=[]
    users = canvas.get_users(course_id)
    for user in users:
        user_dict[user.id] = user.name
        user_names.append(user.name)
    user_message = f"<p>The following users are enrolled in this course, <b>Try to find your name in the list!!!</b><br><br>{'<br>'.join([user.name for user in users])}</p>"

    # All the assignments in the course
    assignments = canvas.get_assignments(course_id)
    if assignments:
        assignment_message = "<p>This course has following assignments and details of student submissions are as below<br></p>"
        for assignment in assignments:
            assignment_message += f"--------------------------------------<b>{assignment.name}</b>--------------------------------------<br>"
            assignment_message += "<table>"
            for submission in assignment.get_submissions():
                if submission and submission.workflow_state == 'unsubmitted':
                    assignment_message += f"<tr><td>{user_dict.get(submission.user_id)}</td><td>&nbsp;&nbsp;&nbsp;&nbsp;Not Submitted</td></tr>"
                else:
                    assignment_message += f"<tr><td><b>{user_dict.get(submission.user_id)}</b></td><td>&nbsp;&nbsp;&nbsp;&nbsp;<b>Submitted</b>({submission.workflow_state})</td></tr>"
            assignment_message += "</table>"
    else:
        assignment_message = "This course has no assignments so far<br>"

    response_message = welcome_message + user_message + assignment_message
    return  HttpResponse(response_message)