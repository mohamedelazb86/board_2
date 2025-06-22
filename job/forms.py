from django import forms
from .models import Job,ApplyUser

class JobForm(forms.ModelForm):
    class Meta:
        model=Job
        # fields='__all__'
        fields=['job_type','title','descriptions','vacany','salary','experience','image','category','location']
        # exclude=['user','slug','publish_date','title']

class ApplyForm(forms.ModelForm):
    class Meta:
        model=ApplyUser
        # fields='__all__'
        exclude=('user','created_at','job')


