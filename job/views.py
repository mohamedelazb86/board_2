from django.shortcuts import render
from .models import Job


def job_list(request):
    jobs=Job.objects.all()
    context={
        'jobs':jobs
    }
    return render(request,'job/job_list.html',context)
