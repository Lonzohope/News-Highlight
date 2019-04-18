class Sources:
    def __init__(self,id,name,url):
        self.id=id
        self.name=name
        self.url=url

class Articles:
    def __init__(self,title,url,description,urlToImage):
        self.title=title
        self.url=url
        self.description=description
        self.urlToImage=urlToImage