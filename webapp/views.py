from django.shortcuts import render
from .models import Technologies
import api

# Create your views here.
token = "https://www.freelance-info.fr/missions?keywords="

def home(request):
	return render(request , "home.html" , {})



def search(request):

	#query = request.GET.get('q')
	query = request.GET.values()
	results = []

	
    
	if query : 

		URLs = api.get_pages(token , list(query) , nb_pages = 3)
		for url in URLs :
			results.append(api.opportunities_extractor(url))

		results = sum(results , [])

	else:

		results = []

	return render(request , "search.html" , {"results" : results , "query" : query })
