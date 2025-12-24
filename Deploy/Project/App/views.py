from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import UserImageForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout as auth_logout
import numpy as np
import joblib
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth import authenticate,login,logout
from .models import UserImageModel
import numpy as np
from tensorflow import keras
from PIL import Image,ImageOps

# import pyttsx3
# import time


def home(request):
    return render(request, 'users/home.html')

@login_required(login_url='users-register')


def index(request):
    return render(request, 'app/index.html')

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality

class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')

from .models import Profile

def profile(request):
    user = request.user
    # Ensure the user has a profile
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)
    
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

from . models import UserImageModel
from . import forms
from .forms import UserImageForm


def Deploy_8(request): 
    print("HI")
    if request.method == "POST":
        form = forms.UserImageForm(files=request.FILES)
        if form.is_valid():
            print('HIFORM')
            form.save()
        obj = form.instance

        result1 = UserImageModel.objects.latest('id')
        models = keras.models.load_model('C:/Users/abhi/Desktop/Final_Year_Project/ITPML35-FINAL/ITPML35 - FINAL CODING/Deploy/Project/App/keras_model.h5')
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open("C:/Users/abhi/Desktop/Final_Year_Project/ITPML35-FINAL/ITPML35 - FINAL CODING/Deploy/Project/media/" + str(result1)).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        classes = ["Cirrhosis","Normal","Numerous septa without cirrhosis","Portal fibrosis with rare septa","Portal fibrosis without septa"]
        prediction = models.predict(data)
        idd = np.argmax(prediction)
        a = (classes[idd])
        if a == "Cirrhosis":
            b ='This Image Detected Cirrhosis'
        elif a == "Normal":
            b ='This Image Detected Normal'
        elif a == "Numerous septa without cirrhosis":
            b ='This Image Detected Numerous septa without cirrhosis'
        elif a == "Portal fibrosis with rare septa":
            b ='This Image Detected Portal fibrosis with rare septa'
        elif a == "Portal fibrosis without septa":
            b ='This Image Detected Portal fibrosis without septa'
       

        else:
            b = 'WRONG INPUT'

        data = UserImageModel.objects.latest('id')
        data.label = a
        data.save()

        # engine = pyttsx3.init()
        # rate = engine.getProperty('rate')
        # engine.setProperty('rate', rate - 10)  # Decrease rate by 50 (default rate is typically around 200)
        # engine.say(a)
        # engine.runAndWait()

        
        # text_to_speech(a, delay=7)

        
        return render(request, 'App/output.html',{'form':form,'obj':obj,'predict':a, 'predicted':b})
    else:
        
        form = forms.UserImageForm()
    return render(request, 'App/model.html',{'form':form})

import joblib

Model = joblib.load('App/Liver1.pkl')
import numpy as np
from django.shortcuts import render
from .forms import HealthAssessmentForm
from .models import HealthAssessment

def Deploy_9(request):
    form = HealthAssessmentForm()  # Initialize the form outside the if block
    
    if request.method == 'POST':
        form = HealthAssessmentForm(request.POST)
        
        if form.is_valid():
            cleaned_data = form.cleaned_data
            age = cleaned_data['age']
            gender = cleaned_data['gender']
            ALB_Level = cleaned_data['ALB_Level']
            ALP_Level = cleaned_data['ALP_Level']
            ALT_Level = cleaned_data['ALT_Level']
            AST_Level = cleaned_data['AST_Level']
            Liver_Fibrosis_Score = cleaned_data['Liver_Fibrosis_Score']
            Bilirubin_Level = cleaned_data['Bilirubin_Level']
            CHOL = cleaned_data['CHOL']
            CREA = cleaned_data['CREA']
            Alcohol_Consumption = cleaned_data['Alcohol_Consumption']
            Diabetes = cleaned_data['Diabetes']
            
            
            # Create a feature array for prediction
            feature = np.array([[
                age, gender, ALB_Level, ALP_Level, ALT_Level,AST_Level,
                Liver_Fibrosis_Score, Bilirubin_Level, CHOL,
                CREA, Alcohol_Consumption,Diabetes
            ]])
            
            predictions = Model.predict(feature)  # Call predict on your model instance

            output = predictions[0] 
            
            # if output == "Cirrhosis":
            #     result = "Affected The Disease Was Cirrhosis"
            # elif output == "Fatty liver":
            #     result = "Affected The Disease Was Fatty liver"
            # elif output == "Fibrosis":
            #     result = "Affected The Disease Was Fibrosis"
            # elif output == "Hepatitis":
            #     result = "Affected The Disease Was Hepatitis"
            # elif output == "Normal":
            #     result = "Affected The Disease Was Normal"

            if output==0:
                result = "Affected The Disease Was Cirrhosis"
            elif output==1:
                result = "Affected The Disease Was Fatty liver"
            elif output == 2:
                result = "Affected The Disease Was Fibrosis"
            elif output==3:
                result = "Affected The Disease Was Hepatitis"
            elif output==4:
                result = "Affected The Disease Was Normal"

            
            # Save the form data and result
            print('output',result)
            instance = form.save(commit=False)
            instance.label = result
            instance.save()
            
            return render(request, 'app/ml_output.html', {"prediction_text": result})
        else:
            print('Form is not valid')
        
    return render(request, 'app/9_deploy.html', {"form": form})


def ML_DB(request):
    predictions = HealthAssessment.objects.all()
    return render(request, 'app/ML_DB.html', {'predictions':predictions })

def Basic(request):
    return render(request,'app/Basic_report.html')

def Metrics(request):
    return render(request,'app/Metrics_report.html')

def Database(request):
    models = UserImageModel.objects.all()
    return render(request, 'app/Database.html', {'models': models})

from .models import Profile

def profile_list(request):
    # Fetch all profile objects from the database
    profiles = Profile.objects.all()
    
    # Pass the profiles data to the template
    return render(request, 'app/profile_list.html', {'profiles': profiles})


from django.shortcuts import render
from django.http import JsonResponse
# import random
# import json
import numpy as np
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer
#from .models import Response, models
from Chatbot.processor import chatbot_response
# Remove the comments to download additional nltk packages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@require_POST
@csrf_exempt
def chatbot_response_view(request):
    if request.method == 'POST':
        the_question = request.POST.get('question', '')

        response = chatbot_response(the_question)
        print(response)

        return JsonResponse({"response": response})
    else:
        
        return JsonResponse({"message": "This endpoint only accepts POST requests."})
 

               
def bott(request):
    return render(request, 'app/bott.html')




def logout_view(request):  
    auth_logout(request)
    return redirect('/')