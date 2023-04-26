from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.


class AddPost(PermissionRequiredMixin, CreateView):
    permission_required = ('rest.add_post', )