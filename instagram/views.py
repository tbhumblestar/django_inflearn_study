from django.http import HttpResponse,Http404
from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import ListView,DetailView

post_list = ListView.as_view(model=Post)

# Create your views here.
def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q','')
    #쿼리스트링에서 'q'라는 값에 저장된 값을 가져옴
    if q:
        qs = qs.filter(message__icontains=q)
        #q라는 검색어가 message에 포함되어 있는 것들만 가져옴
    return render(request,'instagram/post_list.html',{
        'post_list':qs,'q':q
    })


# def post_detail(request,pk):

#     #이거 한 줄이 아래의 try~raise까지 네줄과 같음
#     post = get_object_or_404(Post,pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404

#     return render(request,'instagram/post_detail.html',{'post':post,})


# post_detail=DetailView.as_view(model=Post,queryset=Post.objects.filter(is_public=True))

class PostDetailView(DetailView):
    model = Post
    def get_queryset(self):
        qs = super().get_queryset()
        
        if not self.request.user.is_authenticated:#로그인이 되어있지 않다면
            qs = qs.filter(is_public = True)#공개된 것만 봐라
        return qs

post_detail = PostDetailView.as_view()

def archives_year(request,year):
    return HttpResponse(f"{year} archives")