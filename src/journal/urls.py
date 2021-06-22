from django.conf.urls import url
from django.urls import path
from .views import (
    ClassBasedListView,
    FunctionBasedListView,
    JournalDetailView,
    JournalCreateView,
    JournalUpdateView,
    JournalDeleteView
)

app_name = 'journal'

urlpatterns = [
    path('class/', ClassBasedListView.as_view(template_name="journal_list_override.html"), name='Function View to Class'),
    path('', FunctionBasedListView, name='Function View'),
    path('create/', JournalCreateView.as_view(), name = 'Journal-create'),
    path('<int:id>/', JournalDetailView.as_view(), name = 'Journal-detail'),
    path('<int:id>/delete/', JournalDeleteView.as_view(), name = 'Journal-delete'),
    path('<int:id>/update/', JournalUpdateView.as_view(), name = 'Journal-update')
]