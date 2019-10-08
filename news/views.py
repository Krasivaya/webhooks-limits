from django.http import HttpResponse
import datetime as dt

# News View
def welcome(request):
    return HttpResponse('Welcome To The Moringa Tribune')

#News view for particular day
def news_of_day(request):
    date = dt.date.today()

    #Function to convert date number to exact day name
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1> News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

#Getting Date of a week
def convert_dates(dates):
    #function to get weekdays for date
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    #Return days
    day = days[day_number]
    return day

#Passt days News View
def past_days_news(request, past_date):
        #convert data from url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    day = convert_dates(date)
    hrml = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)