from django import forms

class NameForm(forms.Form):#input TAG를 자동으로 만들어 줌
    your_name = forms.CharField(label='ship name',max_length=100)