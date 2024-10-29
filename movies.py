import requests
import yaml
import json

def obtener_url(page):
   
    try:
   
        with open('auth.yaml', 'r') as file:
   
            config = yaml.safe_load(file)
   
        ACCESS_TOKEN = config['moviedb']['access_token']
        url = f'https://api.themoviedb.org/3/trending/movie/week?page={page}&language=es-CO'
   
        headers = {
            'Content-type': 'application/json',
            'Authorization': 'Bearer ' + ACCESS_TOKEN
        }
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        datos = resp.json()
        
        with open('peliculas.json', 'w') as json_file:
          
            json.dump(datos, json_file)
        
        return datos
   
    except requests.exceptions.RequestException as e:
       
        print(f"Error: {e}")
       
        return None
