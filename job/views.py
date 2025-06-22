from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .myfilter import JobFilter
from .models import Job
from .forms import JobForm,ApplyForm
from django.contrib.auth.decorators import login_required

from .models import Job
from django.core.paginator import Paginator

@login_required
def job_list(request):
    jobs=Job.objects.all().order_by('-id')
    jobs_recent=Job.objects.all().order_by('-id')[:5]
    jobs_count=Job.objects.all().count()

    myfilter=JobFilter(request.GET,queryset=jobs)
    jobs=myfilter.qs




    paginator = Paginator(jobs, 5)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context={
        'jobs':page_obj,
        'myfilter':myfilter,
        'jobs_count':jobs_count,
        'jobs_recent':jobs_recent
    }
    return render(request,'job/job_list.html',context)

@login_required
def job_detail(request,slug):
    job=Job.objects.get(slug=slug)
    
    if request.method == 'POST':
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.job=job
            myform.save()
            return redirect(f'/job/{slug}')
    else:
        form=ApplyForm()

    

    context={
        'job':job,
        'form':form
    }
    return render(request,'job/job_detail.html',context)
@login_required
def add_job(request):
    
    if request.method == 'POST':
        form=JobForm(request.POST,request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.save()
            return redirect('/job/')
    else:
           form=JobForm()
    
    return render(request,'job/add_job.html',{'form':form})