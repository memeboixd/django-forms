from django.shortcuts import render
from django.views import View
from .forms import CourseForm
from django.utils import timezone
from .models import Course
from django.http import HttpResponse
# Create your views here.

def main(request):

    list = Course.objects.order_by('enroll_date')[:5]
    context = {

        'objects' : list
    }
    return render(request,'index.html', context)

def form_view(request):
    if request.method == 'POST':

        form = CourseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            city = form.cleaned_data['city']
            etc = form.cleaned_data['etc']
            gender = form.cleaned_data['gender']
            postcode = form.cleaned_data['gender']

            obj, created = Course.objects.get_or_create(enroll_date=timezone.now(), name=name,surname=surname, email=email, city=city, etc = etc, gender = gender, post_code=postcode )

            if created:
                context = {'end_credit' : 'thanks for taking part: ' + name}
                return render(request, 'End_Credit.html', context)
            else:
                return HttpResponse("Some error occured please fill out the form again")


    else:
        form = CourseForm()
    return render(request,'Form.html', {'form':form})



