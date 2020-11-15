#importation de modules 

import requests 
#import pandas as pd

import bs4
from bs4 import BeautifulSoup
import requests

#application 



#crawling through all the pages associate to the chosen technologies
def get_pages(token, key_words, nb_pages):
    pages = []
    if type(key_words) != list or type(nb_pages) != int:
        raise Exception("please provide the right type of arguments")
    
    else:
        for word in key_words:
            for index in range(1,nb_pages+1):
                page = token + word + "&page=" + str(index)
                pages.append(page)
    return pages


def even_indexed_items(liste_items):
    
    if type(liste_items) != list:
        
        raise Exception("parameter is not a list")
    else :
        
        indexes = list(range(len(liste_items)))
        output_list = [liste_items[index] for index in indexes if index %2 == 0]
        
        return output_list


def opportunities_extractor(URL):
    page = requests.get(URL)
    page
    
    #check if the extractor connected to the site
    if str(page) != "<Response [200]>":
        raise Exception("page not reachable")
    
    else:
        #parsing of the web page
        soup = BeautifulSoup(page.text, "html.parser")
    
    #jobs extraction
        jobs = []
        links = []
        for div in soup.find_all(name="div", attrs={"id":"titre-mission"}) :
            for a in div.find_all(name="a", attrs={"class":"rtitre"} , href = True):
                links.append("https://www.freelance-info.fr"+a["href"])
                job = a.get_text().split()
                jobs.append(' '.join(job))
            
        jobs = even_indexed_items(jobs)
        links = even_indexed_items(links)
    
    #locations extraction
        locations = []
        for span in soup.find_all(name="span", attrs={"class":"textvert9"}) :
            location = span.get_text()
            locations.append(location)
        
        locations = even_indexed_items(locations)
    
    #dates extraction
        dates = []
        for span in soup.find_all(name="span", attrs={"class":"textgrisfonce9"}) :
            date = span.get_text()
            dates.append(date)
        
        dates = even_indexed_items(dates)
    
    #duration and daily rates extraction
        durations = []
        for span in soup.find_all(name="span") :
            duration = span.get_text()
            durations.append(duration)
        
        durations = even_indexed_items(durations)
        durations = even_indexed_items(durations[5:])
    
        duration = list(map(lambda item : item.split("|")[1] , even_indexed_items(durations)))
        TJM = list(map(lambda item : item.split("|")[2] , even_indexed_items(durations)))
    
    
    
    outputs = [jobs , locations , dates , duration , TJM , links]

    length_list_extracted = min([length_list for length_list in list(map(lambda x : len(x) , outputs)) ])
    #print(length_list_extracted)
    
    align_extraction = []
    for k  in range(length_list_extracted):

    	align_extraction.append([jobs[k] , locations[k] , dates[k] , duration[k] , TJM[k] , links[k]])
     


    
    results = {}
    #results = [jobs , location , dates , duration , TJM , links]
    results = {"jobs" : jobs , "location" : locations , "dates" : dates , "duration" : duration , "TJM" : TJM}


    return(align_extraction )



# execution de l'api

# if __name__ == '__main__':

# 	 token = "https://www.freelance-info.fr/missions?keywords="

# 	# #invokation of all the pages
#     key_words = ["python" , ""]
# 	 URLs = get_pages(token , key_words =  , nb_pages = 1)
# 	# URLs

# 	 opportunities = []
# 	 for url in URLs:
# 	     opportunities.append(opportunities_extractor(url))
	
# 	 opportunities = sum(opportunities , [])    
# 	# #opportunities = pd.concat(opportunities)
# 	 print(opportunities)
 