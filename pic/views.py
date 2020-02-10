from django.shortcuts import render

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = InstaRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            fullName = form.cleaned_data['fullName']
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            messages.success(request, f'Account created for {username}')
            return redirect('home')
    else:
        form = InstaRegistrationForm()
    return render(request, 'users/register.html', {'form': form})