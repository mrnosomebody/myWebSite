from django.shortcuts import render
from services.instagram_api import InstagramAPI


def resume(request):
    # a = InstagramAPI()
    context = {
        # 'instagram_media_urls': a.get_instagram_media()
    }
    return render(request, 'resume/resume.html')
