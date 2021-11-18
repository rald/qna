from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

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

    sbjscr=[]
    for sbj in Subject.objects.all():
        try:
            quiz=Score.objects.filter(user__id=request.user.id,subject__id=sbj.id).order_by('-pub_date');
            sbjscr.append({"topic":sbj,"quiz":quiz[0],"percent":"{:.2f}%".format(float(quiz[0].score)/float(quiz[0].items)*100)})
        except:
            sbjscr.append({"topic":sbj,"quiz":None})


    context = {
        "subject_list":sbjscr,
    }

    return render (request=request,template_name="qna/subjects.html",context=context)



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
    if request.method == "POST":
        data=request.POST

        score=0;
        items=0;
        for key in data.keys():
            if str(key).startswith("group"):
                items+=1
                x=data[key].split(',')
                c=Choice.objects.get(id=x[1])
                if c.is_correct_answer:
                    score+=1

        usr=User.objects.get(pk=request.user.id)
        sbj=Subject.objects.get(pk=subject_id)
        scr=Score(user=usr,subject=sbj,score=score,items=items)
        scr.save()

        context={
            "type": "result",
            "score": score,
            "items": items,
            "percent": "{:.2f}%".format(float(score)/float(items)*100.0),
        }

    else:
        subject = Subject.objects.get(id=subject_id)
        question_list = Question.objects.filter(subject__id=subject_id)
        choice = Choice.objects.all()
        context = {
            "type": "quiz",
            "subject": subject,
            "question_list": question_list,
            "choice_list": choice,
        }
    return render (request=request,template_name="qna/questions.html",context=context)

