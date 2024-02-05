from django.shortcuts import render
from django.http import HttpResponse

pojectsList = [
    {
        "id": "1",
        "title": "Haruki Murakami",
        "description":"FIRST PROJECT Completed"
    },
    {
        "id":"2",
        "title": "Oscar Wilde",
        "description": "The Picture of Dorian Gray",
    }
]

def projects(request):
    msg = " you are on the project page"
    number  = 1
    context = {'msg':msg, 'number':number, 'projects':pojectsList}
    # combine main+projects html files -> insert the value of msg
    # return the result inside HttpResponse ob to the browser   

    return render(request, 'projects/projects.html', context)
    # return HttpResponse("Here are our products")


def project(request, pk):
    projectObj = None
    for project in pojectsList:
        if str(project["id"]) == pk:
            projectObj = project

    return render(request, 'projects/single-project.html', {'project':projectObj})
    # return HttpResponse("Here is our products "+pk)

