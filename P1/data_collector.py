from bs4 import BeautifulSoup
import requests
import os


def folder_exists(path):
    return os.path.exists(path)


def data_collector():
    url = "https://opendata-ajuntament.barcelona.cat/data/en/dataset/est-mercat-immobiliari-lloguer-mitja-mensual"
    path = 'data/opendatabcn-rent/'
    if not folder_exists(path):
        os.makedirs(path)
        print("The new directory called " + path + " is created!")

    with requests.Session() as req:
        r = req.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        target = [f"{url}{item['href']}" for item in soup.select("a[href$='lloguer_preu_trim.csv']")] #here we have the location where all the datasets of our source are stored every time someone inserts any new data

        for x in target:
            y = x.split("//")
            url = 'https://' + y[-1]
            r = req.get(url)
            name = url.rsplit("/", 1)[-1]
            file = path + name
            if folder_exists(file):
                print(f"The file {file} already exists")
                continue
            with open(file, 'wb') as f:
                print(f"Downloading {url}")
                f.write(r.content) #we write all the content from the data source into our local computer

