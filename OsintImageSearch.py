import os
import time
import requests
import webbrowser
from tkinter import Tk, filedialog

testingmode = True
apitoken = 'VpiDMt6F0LdWTeaoJLeC31u+t+HEMfed2j2r9z0tOMT5e03xBUfmWGpQ0U2ciMEHnNjbU/sHTss=' 

def searchbyface(imagefile):
    site = 'https://facecheck.id'
    headers = {'accept': 'application/json', 'Authorization': apitoken}
    files = {'images': open(imagefile, 'rb'), 'id_search': None}

    response = requests.post(site + '/api/upload_pic', headers=headers, files=files).json()

    if response['error']:
        return f"{response['error']} ({response['code']})", None, None

    id_search = response['id_search']
    print(response['message'] + ' id_search=' + id_search)

    jsondata = {
        'id_search': id_search,
        'with_progress': True,
        'status_only': False,
        'demo': testingmode
    }

    while True:
        response = requests.post(site + '/api/search', headers=headers, json=jsondata).json()
        if response['error']:
            return f"{response['error']} ({response['code']})", None, None
        if response['output']:
            return None, response['output']['items'], id_search
        print(f'{response["message"]} progress: {response["progress"]}%')
        time.sleep(1)

Tk().withdraw()
imagefile = filedialog.askopenfilename(title="[+] - Select Image", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])

if not imagefile:
    print("[+] - No File Selected")
    exit()

error, urlsimages, search_id = searchbyface(imagefile)

if urlsimages:
    resulttxt = "results.txt"
    with open(resulttxt, "w", encoding="utf-8") as f:
        for idx, im in enumerate(urlsimages, 1):
            score = im.get('score')
            url = im.get('url')
            f.write(f"[+] - [{idx}] - Url: {url}\n")

    print(f"\n[+] - Results Were Saved In '{resulttxt}'")

    searchurl = f"https://facecheck.id/#{search_id}"
    print(f"[+] - Opening In Browser: {searchurl}")
    webbrowser.open(searchurl)
else:
    print("[-] - Error:", error)
