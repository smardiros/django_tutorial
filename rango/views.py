from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from rango.models import Category, Page

def index(request):
	context = RequestContext(request)


	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories': category_list}

	for category in category_list:
		category.url = category.name.replace(' ','_')

	return render(request,'rango/index.html',context_dict,context)
# Create your views here.

def category(request, category_name_url):
	context = RequestContext(request)

	category_name=category_name_url.replace('_',' ')

	context_dict = {'category_name': category_name}

	try:
		category = Category.objects.get(name=category_name)

		pages = Page.objects.filter(category=category)

		context_dict['pages'] = pages

		context_dict['category'] = category

	except Category.DoesNotExist:
		pass

	return render(request, 'rango/category.html', context_dict, context)