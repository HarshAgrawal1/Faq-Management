from django.shortcuts import render
from googletrans import Translator
from django.http import HttpResponse
from .models import FAQ
from django.utils.translation import gettext as _
from django.utils import translation
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from datetime import datetime

import asyncio
from asgiref.sync import sync_to_async

@sync_to_async
def translate_text(text, lang):
    translator = Translator()
    try:
        # Synchronously translate text from English to selected language
        translated = translator.translate(text, src='en', dest=lang)
        return translated.text
    except Exception as e:
        print(f"Translation error: {e}")
        return text  # Fallback to original text if there's an error

def home(request):
    lang = request.GET.get('lang', 'en')  

   
    faqs = FAQ.objects.all()

   
    translated_faqs = []
    for faq in faqs:
        if lang != 'en':  
            translated_question = translate_text(faq.question, lang)
            translated_answer = translate_text(faq.answer, lang)
        else:
            translated_question = faq.question
            translated_answer = faq.answer

        translated_faqs.append({'question': translated_question, 'answer': translated_answer})

    # Render the home page with translated FAQ entries

    return render(request, 'home.html', {'faqs': translated_faqs, 'lang': lang})



def admin_login(request):
    return render(request,'login.html')

def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_superuser:  # Allow only superusers
                faqs=FAQ.objects.all()

                return render(request,'dashboard.html',{'faqs':faqs})
            # Redirect to the admin page (dashboard)

            else:
                
                return redirect("/dashboard/")
            
    else:
        form = AuthenticationForm()
    # messages.error(request,"Incorrect Attempt!!")

    return redirect("/admin_login/")


def newfaq(request):
    return render(request,'newfaq.html')


def newpost(request):
    if request.method=="POST":
        question=request.POST["question"]
        answer=request.POST["answer"]


        faq=FAQ(question=question,answer=answer,created_at=datetime.now())
        faq.save()
        messages.success(request,"Successfully posted your FAQ!!")
        return redirect("/dashboard/newfaq")

    return redirect("/dashboard/newfaq/")