from django.http import HttpResponse
import datetime as dt

# News View
def welcome(request):
    return HttpResponse('Welcome To The Moringa Tribune')

#News view for particular day
def news_of_day(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
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