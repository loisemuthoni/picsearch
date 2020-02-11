from django.shortcuts import render,redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Image,Likes
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CommentForm


# class ImageListView(LoginRequiredMixin,ListView):
#     '''
#     class based view to display uploaded images
#     '''
#     model = Image
#     template_name = 'main/index.html'
#     context_object_name = 'images'
#     ordering = ['-pk']
@login_required
def Index_View(request):
    '''
    function based view to display index page
    '''
    form = CommentForm()
    all_likes = Likes.objects.all()
    users = User.objects.all()
    images = Image.objects.all().order_by('-pk')
    return render(request,'main/index.html',{'images':images,"form":form,"likes":all_likes,"users":users})

@login_required
def CommentOnImage(request,pk):
    '''
    View for commenting on a specfic image
    '''
    current_user = request.user
    current_image = Image.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.image = current_image
            comment.save()
            return redirect(Index_View)
    else:       
        return redirect(Index_View)

class ImageDetailView(LoginRequiredMixin,DetailView):
    '''
    Class based view for viewing specific image with its details
    '''
    model = Image

# class PersonalProfileView(LoginRequiredMixin,DetailView):
#     pass


@login_required
def OtherProfile(request,pk):
    '''
    Function to display user profile
    '''
    user = User.objects.get(pk=pk)
    users = User.objects.all()
    current_user = request.user
    images = Image.objects.filter(profile=user)
    context = {
        "user":user,
        "images":images,
        "users":users,
        "current_user":current_user
    }
    return render(request,"main/profileview.html",context)


@login_required
def ImageSearch(request):
    '''
    Function to search for images by name
    '''
    if 'image' in request.GET and request.GET['image']:
        searched_image = request.GET.get('image')
        searched_images = Image.search_by_name(searched_image)
        message = f"{searched_image}"
        return render(request,'main/search.html',{"message":message,"images":searched_images,})
    else:
        message = "blank"
        return render(request,'main/search.html',{"messsage":message})


class ImageCreateView(LoginRequiredMixin,CreateView):
    '''
    Class based view for adding new image
    '''
    model = Image
    fields = ['image','image_name','image_caption']

    def form_valid(self,form):
        '''
        form overide to set user who uploaded image
        '''
        form.instance.profile = self.request.user
        return super().form_valid(form)


class ImageUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    '''
    Class based view for updating new image
    '''
    model = Image
    fields = ['image','image_name','image_caption']

    def form_valid(self,form):
        '''
        form overide to set user who uploaded image
        '''
        form.instance.profile = self.request.user
        return super().form_valid(form)

    def test_func(self):
        '''
        Function run by userpassestestmixin to check if user passes test to be able to update image
        '''
        image = self.get_object()
        if self.request.user == image.profile:
            return True
        return False


class ImageDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):

    '''
    class based view to delete image object
    '''
    model = Image
    success_url = '/'

    def test_func(self):
        '''
        Function run by userpassestestmixin to check if user passes test to be able to delete image
        '''
        image = self.get_object()
        if self.request.user == image.profile:
            return True
        return False

@login_required
def Like(request,pk):
    '''
    Implements the like functionality in the app
    '''
    current_user = request.user
    likes = Likes.objects.filter(user=current_user).first()
    if likes == None:
        image = Image.objects.get(pk=pk)
        current_user = request.user
        user_likes = Likes(user=current_user,image=image)
        user_likes.save()
        return redirect(Index_View)
    else:
        likes.delete()
        return redirect(Index_View)

