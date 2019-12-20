from django import forms
from news.models import News

class NewsCreationForm(forms.ModelForm):
    cover_image = forms.ImageField(required=False)
    class Meta:
        model = News
        fields = ("title", "category", "article","cover_image")


class NewsUpdateForm(forms.ModelForm):
    # title= forms.CharField()
    # article= forms.CharField(widget=forms.Textarea)
    title = forms.CharField(
        
        widget=forms.TextInput(attrs={'placeholder': 'Title',"class":"form-control"})
    )
    article = forms.CharField(
        
        widget=forms.Textarea(attrs={'placeholder': 'Article',"class":"form-control"})
    )
    category= forms.ChoiceField( widget = forms.Select(attrs={'placeholder': 'Article',"class":"form-control"}),choices=News.CHOICES)
    class Meta:

        model = News
        fields = ('title','article','category')
