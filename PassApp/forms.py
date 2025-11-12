from django import forms
from PassApp.models import CredentialModel

# Create forms here

class CredentialForm(forms.ModelForm):
    class Meta: 
        model = CredentialModel
        fields = ('platform_name', 'username', 'credential', 'login_link', 'backup_mail_num')

        widgets = {
            'platform_name' : forms.TextInput(attrs={'class':'form-control'}),
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'credential' : forms.TextInput(attrs={'class':'form-control'}),
            'login_link' : forms.TextInput(attrs={'class':'form-control'}),
            'backup_mail_num' : forms.TextInput(attrs={'class':'form-control'})
        }