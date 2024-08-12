from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from .models import Banner
import json



def home(request):
    id = request.GET['id']
    try:
        banner = Banner.objects.get(pk=id)
        return JsonResponse({
            'id': banner.id,
            'description': banner.description,
            'timer': banner.timer,
            'link': banner.link
        })
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Banner not found'}, status=404)

@csrf_exempt
@require_http_methods(["PUT"])
def update_banner(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            banner = Banner.objects.get(pk=1)
            banner.description = data.get('description', banner.description)
            banner.timer = data.get('timer', banner.timer)
            banner.link = data.get('link', banner.link)
            banner.save()
            print({
                'id': banner.id,
                'description': banner.description,
                'timer': banner.timer,
                'link': banner.link
            })
            return JsonResponse({
                'id': banner.id,
                'description': banner.description,
                'timer': banner.timer,
                'link': banner.link
            })
        
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Banner not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)




