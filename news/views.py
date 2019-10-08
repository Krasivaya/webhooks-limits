from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt


#News view for particular day
def news_of_day(request):
    date = dt.date.today()
    return render(request,'all-news/today-news.html', {"date":date,})

#Passt days News View
def past_days_news(request, past_date):
    try:
        #convert data from url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        #raise 404 error when valueError is thrown
        raise Http404()
        assert False
    
    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'all-news/past-news.html',{"date":date})