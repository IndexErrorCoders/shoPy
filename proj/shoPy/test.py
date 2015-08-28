#!/usr/bin/python3
#-*- coding: utf-8 -*-

class Mag:    

    
	def __init__(self,mag_liste= ['patate','viande','poisson','muguet'],
	patate=17,viande=8,poisson=12,muguet=7,
	mag_pU={"patate":3,"viande":80,"poisson":55,"muguet":720}): 

		self.mag_liste= mag_liste 

		self.patate = patate        

		self.viande = viande 

		self.poisson = poisson         

		self.muguet = muguet

		self.mag_pU= mag_pU
		


	def livrer_Patate(self):

		self.patate -= 1

	def livrer_Viande(self):

		self.viande -= 1

	def livrer_Poisson(self):

		self.poisson -= 1

	def livrer_Muguet(self):

		self.muguet -= 1
	
	
	def livrer_Patate5(self):

		self.patate -= 5

	def livrer_Viande5(self):

		self.viande -= 5

	def livrer_Poisson5(self):

		self.poisson -= 5

	def livrer_Muguet5(self):

		self.muguet -= 5
	
	
	


	def livrer_5(self,camelot):
		for x in Mag.mag_liste :
			naz=naz

	def rempoter_Patate(self,patate):

		self.patate += 1

	def rempoter_Viande(self,viande):


		self.Viande_Qtt += 1

	def rempoter_Muguet(self,muguet):

		self.muguet += 1
	
	
	
		


pan_liste= ['patate','viande','poisson','muguet']

pan_cout={"patate":0,"viande":0,"poisson":0,"muguet":0}

mon_mag = Mag()

class Panier: 

	def __init__(self,patate=0,viande=0,poisson=0,muguet=0,pan_pA={"patate":0,"viande":0,"poisson":0,"muguet":0}, pan_PRIX=0): 
		
		self.patate = patate        

		self.viande = viande 

		self.poisson = poisson         

		self.muguet = muguet

		self.pan_pA = pan_pA
		
		self.pan_PRIX = pan_PRIX


	def calcul_pan_pA(self):

		self.pan_pA["patate"] = (mon_mag.mag_pU["patate"])*(self.patate)

		self.pan_pA["viande"] = (mon_mag.mag_pU["viande"])*(self.viande)

		self.pan_pA["poisson"] = (mon_mag.mag_pU["poisson"])*(self.poisson)

		self.pan_pA["muguet"] = (mon_mag.mag_pU["muguet"])*(self.muguet)
		
		self.pan_PRIX = self.pan_pA["patate"] + self.pan_pA["viande"] + self.pan_pA["poisson"] + self.pan_pA["muguet"]
		
		
		

	def calcul_pan_PRIX(self):
	
		self.pan_PRIX = self.pan_pA["patate"] + self.pan_pA["viande"] + self.pan_pA["poisson"] + self.pan_pA["muguet"]




	def prendre_Patate(self):

		self.patate += 1

	def prendre_Viande(self):

		self.viande += 1

	def prendre_Poisson(self):

		self.poisson += 1	


	def prendre_Muguet(self):

		self.muguet += 1
	
	
	def prendre_Patate5(self):

		self.patate += 5

	def prendre_Viande5(self):

		self.viande += 5

	def prendre_Poisson5(self):

		self.poisson += 5	


	def prendre_Muguet5(self):

		self.muguet += 5





	def reposer_Patate(self):

		self.patate -= 1

	def reposer_Viande(self):

		self.viande -= 1
	
	def reposer_Poisson(self):
	
		self.poisson -= 1		

	def reposer_Muguet(self):

		self.muguet -= 1



	def annuler_Patate(self):

		self.patate = 0

	def annuler_Viande(self):

		self.viande = 0
	
	def annuler_Poisson(self):
	
		self.poisson = 0		

	def annuler_Muguet(self):

		self.muguet = 0





mon_panier = Panier()
		
class Client: 

	def __init__(self, pseudo="", password="",adresse="",CB=0,codeCB=0,budget_max=200,facture=0):
		
		self.pseudo = pseudo
		self.password = password
		self.adresse = adresse
		self.CB = CB
		self.codeCB = codeCB
		self.budget_max = budget_max
		self.facture = facture

	def braquerMag(self):
		
		mon_mag.patate -= mon_panier.patate
		mon_panier.patate = 0

		mon_mag.viande -= mon_panier.viande
		mon_panier.viande = 0

		mon_mag.poisson -= mon_panier.poisson
		mon_panier.poisson = 0

		mon_mag.muguet -= mon_panier.muguet
		mon_panier.muguet = 0

	
		
		

mon_client = Client()
	


class Ecommerce():
    """docstring for ecommerce"""
    def __init__(self, liste_article= ['Patate','Viande','Muguet'], justcliked = 'vierge'):

        self.liste_article = liste_article
        self.justcliked = justcliked


mon_ecom = Ecommerce()


