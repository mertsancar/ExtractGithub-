import httpx
from bs4 import BeautifulSoup

#https://github.com/search?p=2&q=frontend+developer&type=Users for second page

def get_Github_Users(keyword):
    
    res = httpx.get("https://github.com/search?q={0}&type=users".format(keyword))
    soup = BeautifulSoup(res, 'html.parser')
    search_result = soup.find("div", {"id": "user_search_results"})
    users_data = search_result.find_all("div", {"class": "d-flex hx_hit-user px-0 Box-row"})

    users = list()
    for user in users_data:
        
        try:
            username = user.find("a", {"class": "mr-1"}).text
        except Exception:
            username = ""
        
        try:
            userLink = "https://github.com" + user.find("a", {"class": "mr-1"})["href"]
        except Exception:
            userLink = ""
        
        try:
            description = user.find("p", {"class": "mb-1"}).text
        except Exception:
            description = ""
        
        
        try:
            country = user.find("div", {"class": "mr-3"}).text
        except Exception:
            country = ""
        
        
        users.append({"username":username,
                      "userLink":userLink,  
                "description": description,
                "country": country})

    return users