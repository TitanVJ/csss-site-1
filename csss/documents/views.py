from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from documents.forms import ContactForm
from django.views.generic import TemplateView

def index(request):
	print("constitution index")
	return render(request, 'documents/constitution.html')

def policies(request):
	print("policies index")
	return render(request, 'documents/policies.html')

class FormView(TemplateView):
  template_name = 'documents/photo_gallery.html'

  def get(self, request):
    form = ContactForm()
    return render(request, self.template_name, {'form': form})

  def post(self, request):
    form = ContactForm(request.POST)
    if form.is_valid():
      contact_name = form.cleaned_data['contact_name']
      print("contact_name=["+str(contact_name)+"]")
      content = form.cleaned_data['content']
      print("content=["+str(content)+"]")
      if form.cleaned_data['pics_from_event'] is not None:
        print("pictures detected")
        photos = form.cleaned_data['pics_from_event']
      else:
        print("no pictures detected")
      form = ContactForm()
      return redirect('document:document')

    return render(request, self.template_name, {'form': form})

def photos(request):
	print("photo gallery index")
	return render(request, 'documents/photo_gallery.html')
# Create your views here.
