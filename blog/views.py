from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm,UpdateForm
from django.urls import reverse_lazy
from django.views.generic import View


class HomeView(ListView):
    # import pdb
    # pdb.set_trace()
    model=Post
    template_name='Blog/blog_home.html'
    ordering=['-publish']

# template = 'our-blog.html'
#     def get(self,request):
#         # import pdb
#         # pdb.set_trace()
#         social = ManageSocialAccount.objects.all()
#         logo = AddHeaderLogo.objects.all()
#         # number = AddPhoneNumber.objects.all()
#         number = ManageHeaderContent.objects.all()
#         post_list=Post.objects.filter(status="published")
#         post_date=post_list[0].updated.month
#         paginator= Paginator(post_list,2)
#         page_number = request.GET.get('page')
#         try:
#             post_list =paginator.page(page_number)
#         except PageNotAnInteger:
#             post_list=paginator.page(1)
#         except EmptyPage:
#             post_list=paginator.page(paginator.num_pages)
#         return render(request,'our-blog.html',{'id':id,'post_list':post_list,'logo':logo,'number':number,'social':social,'post_date':post_date })


class BlogHomeView(View):
    def get(self, request):
        data=Post.objects.all()
        return render(request,'Blog/blog_home.html')


class BlogDetail(DetailView):
    model=Post
    template_name='Blog/blog_detail.html'


class AddPost(CreateView):
    model=Post
    form_class=PostForm
    template_name='Blog/add_post.html'
    #fields='__all__'
    #fields={'title','author','body','image'}


class UpdatePost(UpdateView):
    model=Post
    template_name='Blog/update.html'
    form_class=UpdateForm


class DeletePost(DeleteView):
    model=Post
    template_name='Blog/delete.html'
    success_url=reverse_lazy('bloghome')