#marcos bisneto & jessica hellem

from bs4 import BeautifulSoup
import requests
import re

class Buscador:


	def __init__(self, palavraBusca):
		self.palavraBusca = palavraBusca
		self.blackLink = []
		
	def buscarPage(self, url):
		if url not in self.blackLink:
			links = []

			try:
				res = requests.get(url) 
			
			except Exception as e:
				print("Conexão em falha - Verificar a internet ou Link "+url)
				
				res = None
			if res != None:		
				html_page = BeautifulSoup(res.text,'html.parser')
				pattern = re.compile(r'href="(.*?)"')
				for i in res.text.split(): 
					if 'http' in i or 'https' in i:	
						links += pattern.findall(i) 
				numLink = len(links)		
				print("Foram encontrados "+str(len(links))+" Links em "+url+":")
				
				for i in links:
					print("\n>",i)
				print(links)

				self.blackLink.append(url)
				
				palavra = html_page.text.find(self.palavraBusca)
				
				palavras = html_page.text[palavra-10:palavra+len(self.palavraBusca)+10]

				if len(palavras)>0 :
					print("\n >>> A busca encontrou a palavra: "+palavras)
				else:
					print(" >> Nada foi encontrado aqui: ")
				return links
			return []
					

	def profundidadeBuscar(self, urls,depth):
				lk = []
				if depth > 0:
					for i in urls:
						lk = self.buscarPage(i)
					self.profundidadeBuscar(lk, depth-1)	
				else:
					print("Busca Finalizada!")

palavra = input(" >>> Digite a palavra que você procura: ")

link = input(" >>> Informe um link: ")

depth = int(input(" >>> Qual a profundidade?: "))

buscador = Buscador( palavra)
buscador.profundidadeBuscar([link],depth)