from .views import indexTicket, indexReview, indexTicketReview, indexUserFollows, indexAbonnement, viewsPosts, \
    review_update, review_delete, ticket_delete, ticket_update, viewsFlux
from django.urls import path

# 1 nom affiché dans l'adresse navigateur
# 2 def views
# 3 html
urlpatterns = [path('CreatTicketReview/', indexTicketReview, name='creatTicketReview'),
               path('CreatTicket/', indexTicket, name='creatTicket'),
               path("<int:id>/CreatReview/", indexReview, name='creatReview'),
               path('CreatUserFollows/', indexUserFollows, name='abonnement'),
               path('posts/', viewsPosts, name='posts'),
               path('flux/', viewsFlux, name='flux'),
               path("<int:id>/review_delete/", review_delete, name='review_delete'),
               path("<int:id>/review_update/", review_update, name='review_update'),
               path("<int:id>/ticket_delete/", ticket_delete, name='ticket_delete'),
               path("<int:id>/ticket_update/", ticket_update, name='ticket_update'),
               path('CreatAbonnement/', indexAbonnement, name='indexAbonnement'), ]
