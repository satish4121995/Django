from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.utils import timezone
# Create your views here.


def product_home_page(request):
	product = Product.objects.all()
	return render(request, 'products/home.html',{'products':product})
	
@login_required(login_url="account/signup")
def product_create(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon']:
			product = Product()
			product.title = request.POST['title']
			product.body = request.POST['body']
			if request.POST['url'].startswith('http') or request.POST['url'].startswith("https"):
				product.url = request.POST['url']
			else:
				product.url = "http://" + request.POST['url']
			product.icon= request.FILES['icon']
			product.image= request.FILES['image']
			product.pub_date = timezone.datetime.now()
			product.hunter = request.user
			product.save()
			return redirect('/product/' + str(product.id))  # /product/ and product/  are different
		else:
			return render(request, 'products/create.html', {'error':'please fill all field'})

	else:
		return render(request, 'products/create.html')

def product_display(request, product_id):
	product = get_object_or_404(Product,pk = product_id)
	return render(request, "products/detail.html", {'product':product})


@login_required(login_url="/account/signup")
def product_upvote(request, product_id):
	if request.method == 'POST':
		product = get_object_or_404(Product, pk=product_id)
		product.votes_total += 1
		product.save()
		return redirect('/product/' + str(product.id))
	# else:
		# return render(request, 'accounts/login.html')
