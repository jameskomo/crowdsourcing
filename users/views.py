from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm,FreelancerDataForm
from django.contrib.auth.models import User



@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        else:
            messages.error(request, _('Please correct the error below.'))

    else:
        try:
            p_form = ProfileUpdateForm(instance=request.user.profile)
            
        except User.DoesNotExist:
            print ("Sorry, this user has no profile")

    context = {
        'p_form': p_form
    }

    return render(request, 'profile.html', context)


# Freelancer Data Form
def freelancer_data(request):
    if request.method == 'POST':
        freelancer_form = FreelancerDataForm(request.POST)
        if freelancer_form.is_valid():
            freelancer_form.save()
            bio = form.cleaned_data.get('bio')
            skills = form.cleaned_data.get('skills')
            availability = form.cleaned_data.get('availability')
            completed = form.cleaned_data.get('completed')
            documents = form.cleaned_data.get('documents')
            messages.success(request, f'Your bio data has been created! You are now able to update your freelancer information and apply jobs')
            return redirect('login')
    else:
        freelancer_form = FreelancerDataForm()
    return render(request, 'freelancer_data.html', {'freelancer_form': freelancer_form})

# Freelancer Data End