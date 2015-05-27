from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, render_to_response
from .forms import form_for_edit
from .models import Report
from datetime import datetime


def index(request):
    latest_report_list = Report.objects.order_by('id').reverse()[:5]
    context = {'latest_report_list': latest_report_list}
    return render(request, 'write_reports/index.html', context)

"""
def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            print('disabled account error message')
    else:
        print('invalid login error message')
"""

def edit_report(request, report_id=None):
    #投稿ボタンが押されたら
    if request.method == "POST":
        if request.user.is_authenticated():
            report = Report(date=datetime.now(), user=request.user)
            form = form_for_edit(request.POST, instance=report)
            form.save()
            return render(request, 'write_reports/show_detale_of_report.html', {'form': form})

        #else :
        return render(request, 'write_reports/index.html')

    #新規作成・修正
    else:
        #修正画面
        if report_id:
            report = Report.objects.get(pk=report_id)
            form = form_for_edit(report)
        else:
            form = form_for_edit()

        return render(request, 'write_reports/edit_report.html', {'form': form})

def push_report(request):
    pass

def show_detale_of_report(request):
    form = form_for_edit(request.POST)
    return render(request, 'write_reports/show_detale_of_report.html', {'form': form})

def delete_report(request, report_id=None):
    pass
