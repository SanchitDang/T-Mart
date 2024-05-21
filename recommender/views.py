import json

from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from products.models import product
from .utils import add_view_history

from .recommendations import search_products


class ProductView(View):
    def get(self, request, product_id):
        user_id = request.GET.get('user_id')
        if not user_id:
            return JsonResponse({'error': 'user_id parameter is required'}, status=400)

        try:
            user_id = int(user_id)
        except ValueError:
            return JsonResponse({'error': 'user_id must be an integer'}, status=400)

        product = get_object_or_404(product, id=product_id)

        # Add or update view history
        add_view_history(user_id, product_id)

        # Return product details (for example)
        product_data = {
            'id': product.id,
            'name': product.name,
            'description': product.desc,
            'discount': product.discount,
            'image1': product.image1.url,
            'image2': product.image2.url,
            'image3': product.image3.url,
            'image4': product.image4.url,
            'occassion': product.occassion.name,
            'sleeve': product.sleeve.name,
            'neck': product.neck.name,
            'ideal': product.ideal.name,
            'brand': product.brand.name,
            'color': product.color.name
        }
        return JsonResponse(product_data)


@csrf_exempt
def update_view_history(request):
    if request.method == "POST":
        data=json.loads(request.body.decode("utf-8"))
        user_id = data.get('user_id')
        product_id = data.get('product_id')

        print("user_id   >>>>>",data)
        if not user_id or not product_id:
            return JsonResponse({'error': 'user_id and product_id are required'}, status=400)

        try:
            user_id = int(user_id)
            product_id = int(product_id)
        except ValueError:
            return JsonResponse({'error': 'user_id and product_id must be integers'}, status=400)

        add_view_history(user_id, product_id)
        return JsonResponse({'message': 'View history updated successfully'})

    return JsonResponse({'error': 'Invalid request method'}, status=405)


def search(request):
    if request.method == 'GET' and 'q' in request.GET:
        search_query = request.GET['q']
        search_results = search_products(search_query)
        print("search_resultswssssssssssssssssssssssssssssssssssssss")
        print(search_results)
        return render(request, 'search-list.html', {'search_results': search_results})
    else:
        return render(request, 'search-list.html', {'search_results': []})
    