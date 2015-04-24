# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponseRedirect


from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from tg.arvore.models import Arvore
from django.contrib.auth.models import User
from tg.arvore.forms import FormArvore, UserCreateForm
from django.views.generic import TemplateView
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required

index = TemplateView.as_view(template_name='index.html')

@login_required
def arvore_list(request):
	return ListView.as_view(
		queryset = Arvore.objects.filter(usuario=request.user),
    	paginate_by=15,
		template_name='arvore_list.html')(request)

@login_required
def arvore_create(request):
    if request.method == 'POST': 
        form = FormArvore(request.POST, request.FILES)
        if form.is_valid():
            arvore = form.save(commit=False)
            arvore.usuario = request.user
            arvore.save()
            return HttpResponseRedirect("/")
    else:
        form = FormArvore()
    return render_to_response("arvore_form.html", {'form': form},
            context_instance=RequestContext(request))

@login_required
def arvore_update(request, nr_arvore):
    arvore = get_object_or_404(Arvore, usuario=request.user, id=nr_arvore)
    if request.method == "POST":
        form = FormArvore(request.POST, request.FILES, instance=arvore)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = FormArvore(instance=arvore)
    return render_to_response("arvore_form.html", {'form': form},
            context_instance=RequestContext(request))

@login_required
def arvore_delete(request, nr_arvore):
    arvore = get_object_or_404(Arvore, usuario=request.user, id=nr_arvore)
    if request.method == "POST":
        arvore.delete()
        return HttpResponseRedirect("/")
    return render_to_response("confirm_delete_arvore.html", {'object': arvore},
                context_instance=RequestContext(request))


'''arvore_create = CreateView.as_view(
    model=Arvore,
    success_url=reverse_lazy('arvore_list'),
    form_class=FormArvore
)

arvore_delete = DeleteView.as_view(
    template_name='confirm_delete_arvore.html',
    model=Arvore,
    success_url=reverse_lazy('arvore_list')
)
arvore_list = ListView.as_view(
    model=Arvore,
    paginate_by=15
)
arvore_update = UpdateView.as_view(
    model=Arvore,
    success_url=reverse_lazy('arvore_list')
)
'''
registrar = CreateView.as_view(
	template_name='registrar.html',
	model=User,
	success_url=reverse_lazy('arvore_list'),
	form_class=UserCreateForm
)
