from django.shortcuts import render
def google_login(request):
    return render(request, 'oauth/google_login.html')