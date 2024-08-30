from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login as LogIN
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def perform_task(request):
    # Check if the HTTP request method is GET
    if request.method == 'GET':
        # Logic to perform when the button is clicked
        # For example, printing a message to the server's console
        print("Button was clicked and task is performed!")
        
        # Load the 'Token.html' template
        template = loader.get_template('Token.html')
        # Define the context for rendering the template
        # Here, 'data' is set to None
        context = {'data': None}
        # Render the template with the given context and return it as an HttpResponse
        return HttpResponse(template.render(context, request))
    
    # If the request method is not GET (e.g., POST), still render 'Token.html'
    # Set 'data' in the context to '12345688'
    template = loader.get_template('Token.html')
    context = {'data': '12345688'}
    # Render the template with the given context and return it as an HttpResponse
    return HttpResponse(template.render(context, request))

def Home(request):
    # Render the 'index.html' template and return it as an HttpResponse
    return render(request, 'index.html')




def login(request):
    if request.method == 'POST':
        # Retrieve the username and password from the POST data
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If authentication is successful, log the user in
            auth_login(request, user)
            # Display a success message
            messages.success(request, 'You are now logged in.')
            # Redirect to the homepage or another page
            return redirect('index')
        else:
            # If authentication fails, display an error message
            messages.error(request, 'Invalid username or password.')

    # If the request method is not POST or authentication fails, render the login page
    return render(request, 'login.html')

def signup(request):
    # Render the 'registration.html' template and return it as an HttpResponse
    return render(request, 'registration.html')
