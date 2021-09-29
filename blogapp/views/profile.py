from blogapp.views.profile_form import ProfileForm
from blogapp.models.Userprofile import Userprofile as profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render


class profileView(LoginRequiredMixin, TemplateView):
    login_url = "/login"
    redirect_field_name = "next"
    template_name = "blogapp/profile.html"

    def get(self, request):
        id = request.user.id
        objectProfile = get_object_or_404(profile, user_id=id)
        if objectProfile.avatar != None:
            imageName = objectProfile.avatar.name.split('/')[-1]
        else:
            imageName = None
        return render(request, self.template_name, {"objectProfile": objectProfile, "imageName": imageName})
    def post(self, request):
        id = request.user.id
        if request.FILES:
            profile_update = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if profile_update.is_valid():
                profile_update.save()
        else:
            profile_update = ProfileForm(request.POST, instance=request.user.profile)
            if profile_update.is_valid():
                profile_update.save()

        objectProfile = get_object_or_404(profile, user_id=id)
        imageName = objectProfile.avatar.name.split('/')[-1]

        return render(request, self.template_name, {"objectProfile": objectProfile, "imageName": imageName})
