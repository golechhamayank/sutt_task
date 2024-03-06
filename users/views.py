from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from .models import Trip,Event,Wingie
from .forms import create_trip_form, events_form, wingies_form
from django.contrib.auth.decorators import login_required


from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def register_trip(request):
    if request.method == 'POST':
        form = create_trip_form(request.POST)
        if form.is_valid():
            form.save()
            print(request.user)
    else:
        form = create_trip_form(request.POST)
    return render(request,'createtrip.html',{'form':form})

def register_event(request,*args, **kwargs):
    if request.method == 'POST':
        #user_obj = User.objects.get(username=request.user)
        add_wingie = request.POST["add_wingie"]
        form = events_form(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.creator_email = request.user.email
            a.save()
        if add_wingie.lower() == "yes":
            return redirect("wingies")
        else:
             return redirect("events")
            
    else:
        user_email = request.user.email
       
        form = events_form(user_email= user_email)

    return render(request,'events.html',{'form':form})

    
def register_wingies(request):
    if request.method == 'POST':
        form = wingies_form(request.POST)
        if form.is_valid():
            form.save()
            Wingie.creator_email = request.user.email
            
            Wingie.email_id = 'f' + Wingie.bits_id[0:4] + Wingie.bits_id[8:12] + '@pilani.bits-pilani.ac.in'

    else:
        form = wingies_form(request.POST)
    return render(request,'wingies.html',{'form':form})   

def logout_view(request):
    logout(request)
    return redirect('/')


def list_view(request):
    if request.user.is_authenticated:
        a = Wingie.objects.filter(email_id = request.user.email)
        context = {}
        
        for i in a:
            
            for j in Event.objects.filter(trip__dest = i.trip.dest):

                context = {
                    'i':i,
                    'j':j
                }
                

        return render(request,'home.html',context)
    else:
        return render(request,'home.html')

'''
    for i in a:
        for j in Event.objects.filter(trip__dest = i.trip.dest):
            for k in Expense.object.filter(event__name = j.event.name):

                context = {
                    'dest':i.trip.dest,
                    'date_start': i.trip.date_start,
                    'date_end': i.trip.date_end,

                    'name': j.name,
                    'start': j.start,
                    'desc' : j.dest,

                    'exp' : k.exp
                    }




    class TripListView(ListView):
        model = Trip
        template_name = 'blog/home.html' #app/model_viewtype
        context_object_name = 'posts'
        ordering = ['-date_posted']





























    class TripDetailView(DetailView):
        model = Trip



        
    class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        model = Trip
        fields = ['dest','date_started','date_end']

        #def form_valid(self,form):
        #    form.instance.author = self.request.user
        #    return super().form_valid(form)
        
        def test_func(self):
            if self.request.user.email == self.get_object().creator:
                return True
            return False
        

        

    class TripDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
        model = Trip
        success_url = '/'

        def test_func(self):
            if self.request.user.email == self.get_object().creator:
                return True
            return False
        




'''
