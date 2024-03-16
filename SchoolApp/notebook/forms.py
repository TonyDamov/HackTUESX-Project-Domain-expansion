from django.forms import ModelForm
from .models import Material,Grade
from users.models import User

class MaterialForm(ModelForm):
    class Meta:
        model=Material
        fields = ['title','description','file','groups']

class GradeForm(ModelForm):
    class Meta:
        model=Grade
        fields='__all__'
        exclude=['teacher']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(role='Student')
    
class EditGradeForm(ModelForm):
    class Meta:
        model=Grade
        fields=['grade']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(role='Student')