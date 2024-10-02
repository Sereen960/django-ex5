from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')

        # Store the username, email, and mobile in session
        request.session['username'] = username
        request.session['email'] = email
        request.session['mobile'] = mobile

        # Create response object
        response = HttpResponse(f"Logged in as {username}. Go to the <a href='/profile/'>profile</a>.")

        # Set the username, email, and mobile in cookies (expires in 1 hour - 3600 seconds)
        response.set_cookie('username', username, max_age=3600)
        response.set_cookie('email', email, max_age=3600)
        response.set_cookie('mobile', mobile, max_age=3600)

        return response
    return render(request, 'login.html')

def profile_view(request):
    # Get username, email, and mobile from session
    username_from_session = request.session.get('username', 'Guest')
    email_from_session = request.session.get('email', 'Not set')
    mobile_from_session = request.session.get('mobile', 'Not set')

    # Get username, email, and mobile from cookies
    username_from_cookie = request.COOKIES.get('username', 'Guest')
    email_from_cookie = request.COOKIES.get('email', 'Not set')
    mobile_from_cookie = request.COOKIES.get('mobile', 'Not set')

    # Construct messages for display
    session_message = f"Welcome {username_from_session}, Session created !!!!!"
    cookie_message = f"Cookie for {username_from_cookie} is set."

    # Render the profile page with the session and cookie data
    return render(request, 'profile.html', {
        'session_message': session_message,
        'cookie_message': cookie_message,
        'email_from_session': email_from_session,
        'mobile_from_session': mobile_from_session,
        'email_from_cookie': email_from_cookie,
        'mobile_from_cookie': mobile_from_cookie,
    })

# Add these functions if needed by your URL configuration
def set_session(request):
    request.session['name'] = 'Arthy'
    return HttpResponse('Session variable set')

def get_session(request):
    name = request.session.get('name', 'Guest')
    return HttpResponse(f'Session variable value: {name}')

def set_cookies(request):
    response = HttpResponse("Cookie data set")
    response.set_cookie('name', 'Dr.R. Arthy', max_age=3600)
    return response

def get_cookies(request):
    name = request.COOKIES.get('name', 'Guest')
    return HttpResponse(f'Cookie value: {name}')
