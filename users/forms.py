from django import forms
from .models import Trip,Event,Wingie
from django.contrib.auth.models import User

class create_trip_form(forms.ModelForm):
    
    dest = forms.CharField(label = 'Destination')
    date_start = forms.DateField(label = 'Start Date',widget=forms.DateInput(attrs = {'type':'date'}))
    date_end = forms.DateField(label = 'End Date',widget=forms.DateInput(attrs = {'type':'date'}))
    est_exp = forms.IntegerField(label = 'Estimated Expense')

    class Meta:
        model = Trip
        fields = ['dest','date_start','date_end','est_exp']
        
class events_form(forms.ModelForm):

    def __init__(self,user_email,*args, **kwargs):
        user_email = kwargs.pop('user_email',None)
        super(events_form,self).__init__(*args, **kwargs)
        if user_email:
            self.fields['trip'] = forms.ModelChoiceField(label = 'Trip (Destination)', queryset = Trip.objects.filter(creator_email = user_email))
    

    #trip = forms.ModelChoiceField(label = 'Trip (Destination)',queryset = None)
    name = forms.CharField(label = 'Event Name')
    start = forms.DateTimeField(label = 'Date & Time',widget=forms.DateTimeInput(attrs={'type':'datetime-local'}),required=False)
    desc = forms.CharField(label = 'Description',required=False)
    exp = forms.IntegerField(label = 'Event Expense',required = False)

    class Meta:
        model = Event
        fields = ['trip','name','start','desc','exp']
    

class wingies_form(forms.ModelForm):
    
    trip = forms.ModelChoiceField(label = 'Trip (Destination)', queryset=Trip.objects.all())
    bits_id = forms.CharField(label = 'BITS ID',max_length = 13)

    class Meta:
        model = Wingie
        fields = ['trip','bits_id']














