from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime as dt

# News View
def welcome(request):
    return render(request, 'welcome.html')

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
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)