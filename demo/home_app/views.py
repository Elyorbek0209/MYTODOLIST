from django.shortcuts import render # we use render when we work with templates
from . models import Page

def index(request, pagename):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title' : pg.title,
        'content' : pg.bodytext,
        'last_updated' : pg.update_date,
        'page_list': Page.objects.all(),
    }

    #assert False
    return render(request, 'home_app/page.html', context)