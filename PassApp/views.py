from django.shortcuts import render, HttpResponse, redirect
from PassApp.models import CredentialModel
from PassApp.forms import CredentialForm

# Create your views here.

def profile_view(request):
    credentials = CredentialModel.objects.all().values()
    context =  {
        'credentials' : credentials,
        'title': 'Profile',
    }

    return render(request, 'PassApp/profile.html', context=context)


def credential_edit_view(request, id):
    credential = CredentialModel.objects.get(pk=id)
    form = CredentialForm(request.POST or None, instance=credential)
    if form.is_valid():
        form.save()
        return redirect('PassApp:profile')
    context =  {
        'credential' : credential,
        'form' : form,
        'top_text' : 'Update Credential Information',
        'title': 'Edit',
    }

    return render(request, 'PassApp/edit.html', context=context)


def credential_add_view(request):
    form = CredentialForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('PassApp:profile')
    context =  {
        'form' : form,
        'top_text' : 'Add New Credential Information',
        'title': 'Add New',
    }

    return render(request, 'PassApp/edit.html', context=context)


def credential_delete_view(request, id):
    credential = CredentialModel.objects.get(pk=id)
    credential.delete()
    return redirect('PassApp:profile')


def credential_detail_view(request, id):
    credential = CredentialModel.objects.get(pk=id)

    context =  {
        'credential' : credential,
        'top_text' : 'The Credential',
        'title' : 'Detail',
    }

    return render(request, 'PassApp/detail.html', context=context)