from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from .forms import form_for_edit
from .models import Report
from datetime import datetime
from django.db.models import Q


def index(request):
    latest_reports = Report.objects.order_by('id').reverse()[:20]
    context = {'reports': latest_reports}
    return render(request, 'write_reports/index.html', context)


def create_report(request):
    #投稿ボタンが押されたら
    if request.method == "POST":
        if request.user.is_authenticated():
            report = Report(date=datetime.now(), user=request.user)
            form = form_for_edit(request.POST, instance=report)
            form.save()
            return redirect('/write_reports/')

        #else :
        return render(request, '/write_reports/')

    else:
        form = form_for_edit()

        return render(request, 'write_reports/edit_report.html', {'form': form})


def edit_report(request, report_id=None):
    #投稿ボタンが押されたら
    if request.method == "POST":
        if request.user.is_authenticated():
            report = Report(id=report_id, date=datetime.now(), user=request.user)
            form = form_for_edit(request.POST, instance=report)
            form.save()
            return redirect('/write_reports/')

        #else :
        return render(request, 'write_reports/index.html')

    #新規作成・修正
    else:
        report = get_object_or_404(Report, id=report_id)
        form = form_for_edit(instance=report)

        return render(request, 'write_reports/edit_report.html', {'form': form})


def show_detail_of_report(request, report_id=None):
    report = get_object_or_404(Report, id=report_id)
    return render(request, 'write_reports/show_detail_of_report.html', {'report': report})


def delete_report(request, report_id=None):
    #return HttpResponse(str(report_id))
    report = get_object_or_404(Report, id=report_id)
    if request.user.id == report.user_id:
        report.delete()
        return redirect('/write_reports/')
    else:
        return redirect('/write_reports/', {'error_message': '権限がありません。'})#redirectだといったんindex()にいくからerror_messageが消えてしまう。


def search_reports(request):
    keyword = request.POST['keyword']
    reports_searched = Report.objects.filter(Q(title__contains=keyword) | Q(content__contains=keyword))

    #メッセージ処理をしたい。
    return render(request, 'write_reports/index.html', {'reports': reports_searched})
