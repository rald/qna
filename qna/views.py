from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

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
    subject_list = Subject.objects.all()
    return render (request=request,template_name="qna/homepage.html",context={"subject_list":subject_list})



def subject(request,subject_id):
    subject = Subject.objects.get(id=subject_id)
    question_list = Question.objects.filter(subject__id=subject_id)
    choice = Choice.objects.all()
    context = {
        "subject": subject,
        "question_list": question_list,
        "choice_list": choice,
    }
    return render (request=request,template_name="qna/subject.html",context=context)

