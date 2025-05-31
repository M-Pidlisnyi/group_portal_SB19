from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import Material
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MaterialForm

# Create your views here.

class MaterialListView(ListView):
    model = Material
    template_name = "material_list.html"
    context_object_name = "materials"

    def get_queryset(self):
        return Material.objects.all()
    
class MaterialDetailView(DetailView):
    model = Material
    template_name = 'material_detail.html'
    context_object_name = "materials"

class MaterialCreateView(LoginRequiredMixin,CreateView):
    model = Material
    fields = "__all__"
    template_name = "material_create.html"
    success_url = reverse_lazy("material-list")
    
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)
    
class MaterialEditView(LoginRequiredMixin,UpdateView):
    model = Material
    form_class = MaterialForm
    template_name = "material_edit.html"
    success_url = reverse_lazy("material-list")
    context_object_name = "material"

    def get_success_url(self):
        url = reverse("material-detail", kwargs={"pk": self.get_object().pk})
        return url

class MaterialDeleteView(LoginRequiredMixin,DeleteView):
    model = Material
    template_name = "material_delete.html"
    success_url = reverse_lazy("material-list")
    context_object_name = "material"