from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from . import models
from django.views.generic.base import TemplateView

from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token
from django.contrib.auth import login
# Create your views here.

#Function Views
@login_required
def index(request):
    print(dir(request))
    #metodo feo
    # if not request.user.is_authenticated():
        # return redirect('login')
    if request.method == 'GET':    
        greet = "hi"
        person = get_object_or_404(models.Person, pk=675)
        name = person.name
        lista = [1,2,3,4,5]
        diccio = {"elemento":"ninguno", "elemento2":"uno solo"}
        return render(request, 'index.html', 
                    {'object':greet, 
                    'name': name, 
                    'collection':lista, 
                    "diccionario":diccio}
                    )
    else:
        raise Http404("Uoops esto es embarazoso")

#baseview
from django.views import View

class BaseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {
                        "greet":"hola base view"
                        })

    
    def post(self, request):
        return render(request, 'index.html', {
                        "greet":"recibi el post"
                        })

    def update(self, request):
        return render(request, 'index.html', {
                        "greet":"update"
                        })

#Templateview
from django.views.generic.base import TemplateView

class HomeTemplateView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        context["greet"] = "hello desde template view"
        return context

#generic views
#detail view
from django.views.generic.detail import DetailView

class PersonDetailView(DetailView):
    model = models.Person
    template_name = 'detail.html'

#listview

from django.views.generic.list import ListView
class PersonList(ListView):
    model = models.Person
    template_name= 'list.html'

    # def get_context_data(self, **kwargs):
    #     context = super(PersonList, self).get_context_data(**kwargs)
    #     context["object_list"] = models.Person.objects.older()
    #     return context

#createview
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class PersonCreate(CreateView):
    model = models.Person
    fields = '__all__'  #['name', 'email']
    template_name = 'create.html'
    success_url = reverse_lazy('list')


#updateview
from django.views.generic.edit import UpdateView

class PersonUpdate(UpdateView):
    model = models.Person
    fields =  ['name', 'email']
    template_name = 'create.html'
    success_url = reverse_lazy('list')

#deleteview
from django.views.generic.edit import DeleteView

class PersonDelete(DeleteView):
    model = models.Person
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('list')

#forms
from . import forms

class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = forms.ContactForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = forms.ContactForm(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data['name'])
            form = forms.ContactForm()

        return render(request, 'form.html', {'form':form})

from django.views.generic.edit import FormView

class ContactFormView(FormView):
        template_name = 'form.html'
        form_class = forms.PersonModelForm
        success_url = reverse_lazy('list')

        def form_valid(self, form):

            return super(ContactFormView, self).form_valid(form)


from django.forms.formsets import formset_factory
from django.db import IntegrityError, transaction
from django.contrib import messages
#formset
def EventPersonFormset(request):

    event_formset = formset_factory(forms.DetailEventForm, formset=forms.BaseFormSet, extra=3)
    programs = models.Program.objects
    events = models.Event.objects

    if request.method == 'POST':
        person_form = forms.PersonForm(request.POST)
        detail_formset = event_formset(request.POST)

        if person_form.is_valid() and detail_formset.is_valid():
            person = models.Person()
            person.name = person_form.cleaned_data['name']
            person.email = person_form.cleaned_data['email']
            person.age = person_form.cleaned_data['age']
            person.program = programs.get(pk=person_form.cleaned_data["program"])
            person.save()

            new_events = []

            for event_form in detail_formset:
                event = events.get(pk=event_form.cleaned_data["event"])
                new_events.append(models.EventPerson(event = event, person=person))

            try:
                with transaction.atomic():
                    models.EventPerson.objects.bulk_create(new_events)
                    messages.success(request, "todo salio bien")
                
            except IntegrityError:
                message.error(request, 'hubo un pedo')
                return redirect(reverse_lazy('list'))
    else:
        person_form = forms.PersonForm()
        detail_formset = event_formset()

    return render(request, 'formset.html', {"person_form": person_form, 
                                            "detail_formset" : detail_formset
                                            })
#filters
from .filters import PersonFilter
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.core import serializers

def search_name(request):
    name = request.GET.get('name', None)
    person_list = models.Person.objects.all()
    
    person_filter = PersonFilter(request.GET, queryset=person_list)
    data = serializers.serialize("json", person_filter.qs)
    print(data)
    return JsonResponse(data, safe=False)

def Search(request):
        # print(request.url)
        person_list = models.Person.objects.all()
        person_filter = PersonFilter(request.GET, queryset=person_list)
        return render(request, 'search.html', {'filter': person_filter})

#--------------------------------------------

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('login')
    else:
        return render(request, 'account_activation_invalid.html')

class account_activation_sent(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'account_activation_email.html', {
                        "greet":"hola base view"
        }) 


