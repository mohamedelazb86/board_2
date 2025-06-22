from .models import Home

def get_contet_data(request):
    data=Home.objects.last()
    return({'data':data})