from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import NewUserForm,UpdateUserForm
from .models import Choice, Question, Subject, Score

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("qna:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="qna/register.html", context={"register_form":form})



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			me = user
			if user is not None:
				login(request, user)
				messages.info(request,f"You are now logged in as {username}.")
				return redirect("qna:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="qna/login.html", context={"login_form":form})



def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("qna:homepage")



def homepage(request):
    return render (request=request,template_name="qna/homepage.html")



def subjects(request):
    subject_list = Subject.objects.all()
    return render (request=request,template_name="qna/subjects.html",context={"subject_list":subject_list})



def update_user_request(request):
    if request.method == "POST":
        form = UpdateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Update user successful.")
            return redirect("qna:homepage")
        messages.error(request, "Unsuccessful update user. Invalid information.")
    if request.user.is_authenticated:
        form = UpdateUserForm(initial={
                    "username":   request.user.username,
                    "first_name": request.user.first_name,
                    "last_name":  request.user.last_name,
                    "email":      request.user.email,
        })
    else:
        form = UpdateUserForm()
    return render (request=request, template_name="qna/update_user.html", context={"update_user_form":form})



def questions(request,subject_id):
    subject = Subject.objects.get(id=subject_id)
    question_list = Question.objects.filter(subject__id=subject_id)
    choice = Choice.objects.all()
    context = {
        "subject": subject,
        "question_list": question_list,
        "choice_list": choice,
    }
    return render (request=request,template_name="qna/questions.html",context=context)
