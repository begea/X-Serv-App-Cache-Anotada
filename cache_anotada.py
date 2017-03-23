#!/usr/bin/python3
import urllib.request
import webapp

class cacheanotada(webapp.webApp):
    cache = {} #Diccionario

    def parse(self, pet):
        lista = pet.split(" ")
        met = lista[0]
        rec = lista[1][1:]
        return (met, rec)

    def process(self, parsed):
        met, rec = parsed
        if met == "GET":
            print(rec)
            if rec.split("/")[0] == "Recarga":
                url1 = rec.split("/")[1]
                url2 = "http://" + url1
                Body = ("<meta http-equiv='Recarga' content=3;url=" + url2 + ">")
                return ("302 Redirection", Body)

                if rec in self.cache:
                    return ("200 OK", self.cache[rec])

                elif rec not in self.cache:
                    url2 = "http://" + rec
                    f = urllib.request.urlopen(url2)
                    body = f.read()
                    self.cache[rec] = body
                    busca = body.find("<body")
                    encuentra = body.find(">", busca)
                    HTML = ("<a href=" + url2 + ">Enlace</a>" +"<a href=" + rec + ">Recarga</a>")
                    Body = (body[:encuentra + 1] + HTML + body[encuentra + 1:])
                    return ("200 OK", Body)
            else:
                return ("403 No disponible", "Metodo no valido")
        else:
            return ("403 No disponible", "Metodo no valido")

if __name__ == "__main__":
    testWebApp = cacheanotada("localhost", 1256)
