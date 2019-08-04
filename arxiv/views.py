# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Researcher, Paper, Author, Category, Classification
from .lib.scraping import search
import datetime


def index(request):
    entries = search(keyword="consciousness")
    for entry in entries:
        paper = Paper()
        if Paper.objects.filter(url=entry.id.text):
            continue
        paper.url = entry.id.text
        paper.title = entry.title.text
        paper.summary = entry.summary.text[:-1]
        date = entry.published.text[:10]
        [year, month, day] = list(map(int, date.split('-')))
        paper.pub_date = datetime.date(year=year, month=month, day=day)
        authors = [author.text[1:-1] for author in entry.find_all('author')]
        paper.authors = ', '.join(authors)
        paper.save()
        category_name = entry.category.get('term')
        cats = Category.objects.filter(name=category_name)
        if cats:
            cat = cats[0]
        else:
            cat = Category()
            cat.name = category_name
            cat.save()
        classification = Classification()
        classification.paper = paper
        classification.category = cat
        classification.save()
        for rname in authors:
            rs = Researcher.objects.filter(name=rname)
            if rs:
                researcher = rs[0]
            else:
                researcher = Researcher()
                researcher.name = rname
                researcher.save()
            author = Author()
            author.paper = paper
            author.researcher = researcher
            author.save()
    latest_papers_list = Paper.objects.order_by('-pub_date')
    # titles = [
    #     "<h2>{}-{}</h2><p>{}</p>".format(
    #         paper.title, paper.authors, paper.summary)
    #     for paper in latest_papers_list
    #     ]
    dic = {'latest_papers_list': latest_papers_list}
    response = render(request, 'arxiv/index.html', dic)
    return response
