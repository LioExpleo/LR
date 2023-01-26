from django.forms import ModelForm
from .models import Ticket, Review, UserFollows
from django import forms

from .forms_settings import (
    CHOICES_REVIEW_FORM
)


class TicketForm(ModelForm):
    # Une class meta est une classe qui utilise une classe, cela va indiquer à django quelle classe utiliser
    # pour le formulaire

    # Le modèle Ticket doit être utilisé pour créer le formulaire
    # Précision des champs uniquement utiles du modèle à utiliser dans le formulaire ensuite
    class Meta:
        model = Ticket
        # exclude = ['user']
        exclude = ['image']
        fields = ['title', 'description', 'image', 'user'] #
        enctype = "multipart/form-data"
        widgets = {
                'title': forms.TextInput(
                    attrs={
                        'class': 'ticket_form_title'
                    }
                ),
                'description': forms.Textarea(
                    attrs={
                        'class': 'ticket_form_description'
                    }
                ),
                'image': forms.TextInput(
                    attrs={
                        'class': 'ticket_form_image'
                    }
                )
            }

class ReviewForm(ModelForm):
    # Une class meta est une classe qui utilise une classe, cela va indiquer à django quelle classe utiliser
    # pour le formulaire

    # Le modèle Review doit être utilisé pour créer le formulaire
    # Précision des champs uniquement utiles du modèle à utiliser dans le formulaire ensuite
    class Meta:
        model = Review

        fields = ['ticket','rating', 'user', 'headline', 'body']
        # enctype = "multipart/form-data"

        widgets ={
                'headline': forms.TextInput(
                attrs={
                    'class': 'review_form_headline'
                }
                ),
                'body': forms.Textarea(
                attrs={
                    'class': 'review_form_body'
                }
                ),
                'rating': forms.RadioSelect(
                choices=CHOICES_REVIEW_FORM,
                attrs={

                    'class': 'review_form_rating'
                }
            ),
        }

class UserFollowsForm(ModelForm):
    # Une class meta est une classe qui utilise une classe, cela va indiquer à django quelle classe utiliser
    # pour le formulaire

    # Le modèle UserFollows doit être utilisé pour créer le formulaire
    # Précision des champs uniquement utiles du modèle à utiliser dans le formulaire ensuite
    class Meta:
        model = UserFollows
        fields = ['user', 'followed_user']
        '''enctype = "multipart/form-data"

        widgets ={
                'followsUser': forms.Textarea(
                attrs={
                    'class': 'UserFollows_form_followsUser'
                }
                )
        }
'''
