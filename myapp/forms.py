from django import forms 
from .models import User

GENDER_CHOICE=[
    ('Male', 'Male'),
    ('Female', 'Female'),
]

JOB_CITY_AREA=[
     ('Dhaka', 'Dhaka'),
    ('Chattogram', 'Chattogram'),
    ('Rajshahi', 'Rajshahi'),
    ('Sylhet', 'Sylhet'),
    ('Bogura', 'Bogura'),
    ('Jessore', 'Jessore'),
    ('Khulna', 'Khulna'),

]


class StudentRegistration(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICE,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(label='Preferred Job City',choices=JOB_CITY_AREA,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = User
        fields =  ['name', 'dob', 'gender', 'city', 'locality', 'pin', 'division','mobile', 'email', 'job_city', 'profile_image', 'my_file']
        
        labels={'name':'User Name', 'dob':'Date Of Birth', 'pin':'PIN Code', 'mobile':'Mobile NO', 'email':'Email ID', 'job_city':'Job City', 'profile_image':'Profile Image', 'my_file':'Document'} 
        
        
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'division':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }