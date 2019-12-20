from django.urls import path, include
from news.views import NewsCreateView,NewsDetail,NewsDeleteView,NewsUpdateView,CategoryListView,comment
urlpatterns = [
   
    path('create/', NewsCreateView.as_view(), name='create_news'),
    path('<str:category>/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('<int:pk>/delete', NewsDeleteView.as_view(), name='delete_news'),
    path('<int:pk>/update', NewsUpdateView.as_view(), name='update_news'),
    path('category/<str:category>', CategoryListView.as_view(), name='news-cat'),
    path('<str:category>/<int:post_id>/comment', comment, name='comment'),
    # path('<str:category>/<int:pk>', CategoryListView.as_view(), name='news-category'),

   
]