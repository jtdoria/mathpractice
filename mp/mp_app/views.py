from django.http import HttpResponse
from django.shortcuts import render

from .models import Subject


def index_view(request):
    subject_list = Subject.objects.all()
    context = {'subject_list': subject_list}
    return render(request, 'mp_app/home.html', context)


def arithmetic_view(request):
    context = {}
    return render(request, 'mp_app/arithmetic.html', context)


# class HomePageView(ListView):
#
#     model = Subject
#     template_name = 'mp_app/home.html'
#     subjects = [subj.subject_name for subj in Subject.objects.all()]
#
#     def get_context_data(self, **kwargs):
#         context = {subj.subject_name: subj for subj in Subject.objects.all()}
#         return context

