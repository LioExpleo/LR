from django.forms import ModelForm
from .models import Ticket, Review, UserFollows
from django import forms
# from .forms_settings import ( CHOICES_REVIEW_FORM)


class TicketForm(ModelForm):
    # Une class meta est une classe qui utilise une classe, cela va indiquer à django quelle classe utiliser
    # pour le formulaire
    # Le modèle Ticket doit être utilisé pour créer le formulaire
    # Précision des champs uniquement utiles du modèle à utiliser dans le formulaire ensuite
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        labels = {"title": "Titre", "description": "", "image": "Image"}

        widgets = {
                'title': forms.TextInput(
                    attrs={
                        'class': 'cl_ticket_form_title'
                    }
                ),
                'description': forms.Textarea(
                    attrs={
                        'class': 'cl_ticket_form_description'
                    }
                ),
            }


class ReviewForm(ModelForm):
    # Une class meta est une classe qui utilise une classe, cela va indiquer à django quelle classe utiliser
    # pour le formulaire
    # Le modèle Review doit être utilisé pour créer le formulaire
    # Précision des champs uniquement utiles du modèle à utiliser dans le formulaire ensuite
    rating = forms.IntegerField(
        widget=forms.RadioSelect(attrs={'class': 'cl_review_form_rating'},
                                 choices=((i, i) for i in range(0, 6)))
    )

    class Meta:
        model = Review
        fields = ['headline', 'rating',  'body']
        # enctype = "multipart/form-data"
        labels = {"headline": "Titre", "rating": "Note", "body": ""}

        widgets = {'headline': forms.TextInput(
                attrs={'class': 'cl_review_form_headline'}
                ),
                'body': forms.Textarea(
                attrs={'class': 'cl_review_form_body'}
                ),
        }


class UserFollowsForm(ModelForm):
    # Une class meta est une classe qui utilise une classe, cela va indiquer à django quelle classe utiliser
    # pour le formulaire
    # Le modèle UserFollows doit être utilisé pour créer le formulaire
    # Précision des champs uniquement utiles du modèle à utiliser dans le formulaire ensuite.
    class Meta:
        model = UserFollows
        fields = ['followed_user']
        enctype = "multipart/form-data"
        labels = {"followed_user": "followed_user"}
