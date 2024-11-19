from django.shortcuts import render , redirect ,get_object_or_404
from .models import To_do_data
# Create your views here.
def home_page(request):
    Datas= To_do_data.objects.all()
    return render(request,'home.html',{'Datas':Datas})


# def add_task(request,input):
#     print(input)
#     return render(request,'add.html')

def add_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        task_details = request.POST.get('task_details')
        target_time = request.POST.get('target_time')
        if task_name and target_time:
                new_task = To_do_data(
                task_name=task_name,
                task_details=task_details,
                target_time=target_time)
                new_task.save()
        return redirect('home_page')  
    return render(request, 'add.html') 


def edit_task(request, pk):
    # Use pk to fetch the object
    update = get_object_or_404(To_do_data, pk=pk)

    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        task_details = request.POST.get('task_details')
        target_time = request.POST.get('target_time')

        if task_name and target_time:
            update.task_name = task_name
            update.task_details = task_details
            update.target_time = target_time
            update.save()

        return redirect('home_page')  # Redirect after updating the task

    return render(request, 'edit.html', {"update": update}) 



def delete_task(request,pk):
    ids=To_do_data.objects.get(id=pk)
    ids.delete()
    return redirect('home_page')




def view_task(request,pk):
    # Datas= To_do_data.objects.all()
    data=To_do_data.objects.get(id=pk)
    # data=get_object_or_404(To_do_data, id=pk)
    return render(request,'view.html',{'data':data})

