from django.db.models import F
from django.shortcuts import render,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.decorators.http import require_http_methods
from news.models import News,Feedback
from news.forms import NewsCreationForm, NewsUpdateForm
# Create your views here.

class NewsCreateView(LoginRequiredMixin,CreateView):
    model = News
    template_name = "news/create_news.html"
    form_class = NewsCreationForm
    success_url='/'


    def form_valid(self, form):
        news = form.save(commit=False)
        news.author =self.request.user
        news.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form)
        return super(NewsCreateView, self).form_invalid(form)


class NewsList(ListView):
    model = News
    queryset = News.objects.all()
    
    context_object_name = 'news_list'
    template_name='index.html'

class NewsDetail(DetailView):
    model = News
    
    template_name='news/news_detail.html'
    context_object_name='news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments']= Feedback.objects.filter(news=self.object)
        self.object.count = self.object.count + 1
        # self.object_count= F('self.object') + 1
        self.object.save()
        return context

class NewsDeleteView(DeleteView):
    model = News
    template_name = "news/delete_news.html"
    success_url = reverse_lazy("home")



class ModelView(TemplateView):
    template_name = "index.html"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = News.objects.filter()
        context["latest_news"] = query.order_by('-created_at')[:5]
        context["list_news"] = query.order_by('-created_at')
        context["list_top_news"] = News.objects.filter().order_by('-count')

        return context
    

class CategoryListView(ListView):
    model =News
    
    template_name = 'news/news_by_category.html'
    context_object_name = 'category'
    ordering =['-created_at']

    def get_queryset(self):
        # category = get_object_or_404(News, category=)
        # print(category)
        return News.objects.filter(category=self.kwargs.get('category')).order_by('-created_at')

class NewsUpdateView(UpdateView):
    model= News
    form_class =NewsUpdateForm
    template_name = "news/update_news.html"
    # fields = ('title','article','category')




@login_required
@require_http_methods(["POST"])
def comment(request, *args, **kwargs):
    request_data = request.POST
    comment = request_data.get('comment')
    news = get_object_or_404(News, pk=kwargs.get('post_id'))
    commentator =  request.user
    comment_object = Feedback(comment=comment, news=news, commentator=commentator)
    data = comment_object.save()
    print(data)
    return render(request, "news/comment.html", {'comment': comment_object})


