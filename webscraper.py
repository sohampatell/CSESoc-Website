import requests
html_text = requests.get('https://au.indeed.com/jobs?q=data+analyst&l=Sydney+NSW&from=searchOnHP&vjk=e0fe0e86eeb37e0d&advn=5238022611890227').text
print(html_text)