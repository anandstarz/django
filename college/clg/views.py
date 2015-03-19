from django.shortcuts import render
# from clg.form import loginform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as auth_login, logout
from django.shortcuts import render_to_response, redirect, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.template import RequestContext, Context


def login_page(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        return render_to_response('App/Alogin.html',{},context)
    
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                print username
                return render_to_response('App/Alogin.html',{},context)
            else:
                state = "Your account is not active, please contact the site admin."
                return HttpResponse("Your Emp account is disabled.")
        else:
            state = "Your username and/or password were incorrect."
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('App/login.html',{},context)






def logout_view(request):
    logout(request)
    return redirect('App/login.html')

from endless_pagination.decorators import page_template

@page_template('App/Alogin.html')
def entry_index(request, template='App/login.html', extra_context=None):
    print "hi"
    context = {
        'entries': User.objects.all(),
    }
    print context
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(
        template, context, context_instance=RequestContext(request))





import json
from django.contrib.auth.models import User

def autos(request):
    print "dfdf"

    q = User.objects.filter(username__istartswith=request.GET['term'])[:3]

    data =  json.dumps([qq.username for qq in q])
    print data
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
def result(request):

    if request.method=='POST':
        x=request.POST.get('query')
        qu = User.objects.filter(username__contains=x)
        for q in qu:
            print q.username, q.email
            return HttpResponse(q.username)