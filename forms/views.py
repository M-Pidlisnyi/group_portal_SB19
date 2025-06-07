from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from forms.models import Subject, Mark
from forms.forms import MarkForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import UserIsOwnerMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
class MarkList(ListView):
    model = Mark
    template_name = 'forms/marks.html'
    paginate_by = 2
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
class MarkCreate(LoginRequiredMixin, CreateView):
    model = Mark
    form_class = MarkForm
    template_name = 'forms/mark_create.html'
    success_url = reverse_lazy('marks')
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)

class MarkEdit(UserIsOwnerMixin, UpdateView):
    model = Mark
    form_class = MarkForm
    template_name = 'forms/mark_update.html'

    def get_success_url(self):
        return reverse('mark-detail', kwargs={"pk": self.get_object().pk})
class MarkDelete(UserIsOwnerMixin, DeleteView):
    model = Mark
    context_object_name = 'mark'
    success_url = reverse_lazy('marks')
    template_name = 'forms/mark_delete.html'