import urllib
def edit_route(endpoint)-> str:
    """
    acces to the url addin the end point to access the data 
    example:http://127.0.0.1:8000/{endpoint} this is the base adress, 
    {endpoint} is the route endpoint
    
    """
    request_users = urllib.request.urlopen(f"http://127.0.0.1:8000/{endpoint}")
    return request_users.read()