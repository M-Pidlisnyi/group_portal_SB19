from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from forms.models import Subject, Mark
from forms.forms import MarkForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
class MarkList(ListView):
    model = Mark
    template_name = 'forms/marks.html'
    #paginate_by = 2
    context_object_name = 'marks'
class MarkDetail(DetailView):
    model = Mark
    template_name = 'forms/mark_detail.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['form'] = MarkForm()
        return context
    def post(self, request : HttpRequest, *args, **kwargs):
        if request.user.is_authenticated:
            form = MarkForm(request.POST, request.FILES)
            print("------------------------")
            print(request.FILES)
            print("------------------------")
            if form.is_valid():
                new_mark: Mark = form.instance
                new_mark.grade = self.get_object()
                new_mark.user = self.request.user
                new_mark.save()
            return redirect(request.path_info)
        else:
            return HttpResponse(content='Not authenticated', status=403)