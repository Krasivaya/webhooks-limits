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
