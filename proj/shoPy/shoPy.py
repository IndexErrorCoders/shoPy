#!/usr/bin/python3
#-*- coding: utf-8 -*-
# http://code.runnable.com/UiPhLHanceFYAAAP/how-to-perform-ajax-in-flask-for-python
# https://flask-socketio.readthedocs.org/en/latest/
# http://nullege.com/codes/search/flask.ext.socketio.SocketIO

import test
from test import mon_mag 
from test import mon_client
from test import mon_panier
from test import mon_ecom

from flask import Flask, jsonify, render_template, request, url_for, redirect, flash



from datetime import date, time, datetime,timedelta
import datetime 

import ast

maintenant = datetime.datetime.now()
d = maintenant


app = Flask(__name__)


@app.route('/ACHETER')
def ACHETER():

	clikedname = request.args.get('clikedname', 0, type=str)


	pythoncapture=str()

	pythoncapture = clikedname
	mon_ecom.justcliked = pythoncapture


	mon_ecom.justcliked = mon_ecom.justcliked
	
	print("\n mon_ecom.justcliked = pythoncapture  : ",pythoncapture)
	
	
	
	
	
	
	
	if pythoncapture == 'patate1buy':
		mon_panier.prendre_Patate()
	elif pythoncapture == 'viande1buy':
		mon_panier.prendre_Viande()
	elif pythoncapture == 'poisson1buy':
		mon_panier.prendre_Poisson()
	elif pythoncapture == 'muguet1buy':
		mon_panier.prendre_Muguet()	
	else:
		pass
	
	
	if pythoncapture == 'patate5buy':
		mon_panier.prendre_Patate5()
	elif pythoncapture == 'viande5buy':
		mon_panier.prendre_Viande5()
	elif pythoncapture == 'poisson5buy':
		mon_panier.prendre_Poisson5()
	elif pythoncapture == 'muguet5buy':
		mon_panier.prendre_Muguet5()	
	else:
		pass


	if pythoncapture == 'patate1drop':
		mon_panier.reposer_Patate()
	elif pythoncapture == 'viande1drop':
		mon_panier.reposer_Viande()
	elif pythoncapture == 'poisson1drop':
		mon_panier.reposer_Poisson()
	elif pythoncapture == 'muguet1drop':
		mon_panier.reposer_Muguet()	
	else:
		pass


	if pythoncapture == 'patateCANCEL':
		mon_panier.annuler_Patate()
	elif pythoncapture == 'viandeCANCEL':
		mon_panier.annuler_Viande()
	elif pythoncapture == 'poissonCANCEL':
		mon_panier.annuler_Poisson()
	elif pythoncapture == 'muguetCANCEL':
		mon_panier.annuler_Muguet()	
	else:
		pass


	
	mon_panier.calcul_pan_pA()
	
	mag_Qmuguet = mon_mag.muguet

	mag_Qpatate = mon_mag.patate
	mag_Qviande = mon_mag.viande
	mag_Qpoisson = mon_mag.poisson	
	
	pan_Qpatate = mon_panier.patate
	pan_Qviande = mon_panier.viande
	pan_Qpoisson = mon_panier.poisson
	pan_Qmuguet = mon_panier.muguet
	
	pan_pApatate = mon_panier.pan_pA["patate"]
	pan_pAviande = mon_panier.pan_pA["viande"]
	pan_pApoisson = mon_panier.pan_pA["poisson"]
	pan_pAmuguet = mon_panier.pan_pA["muguet"]
	
	
	
	

	pan_PRIX = mon_panier.pan_PRIX
	mag_liste = mon_mag.mag_liste

	

	data={}
	data['pan_PRIX'] = pan_PRIX
	data['pan_Qpatate'] = pan_Qpatate
	data['pan_Qviande'] = pan_Qviande
	data['pan_Qpoisson'] = pan_Qpoisson
	data['pan_Qmuguet'] = pan_Qmuguet

	data['pan_pApatate'] = pan_pApatate
	data['pan_pAviande'] = pan_pAviande
	data['pan_pApoisson'] = pan_pApoisson
	data['pan_pAmuguet'] = pan_pAmuguet


	data['mag_Qpatate'] = mag_Qpatate
	data['mag_Qviande'] = mag_Qviande
	data['mag_Qpoisson'] = mag_Qpoisson
	data['mag_Qmuguet'] = mag_Qmuguet

	data['mag_liste'] = mag_liste

	correspond = dict()

	G = 'mag_Q'

	D = 'pan_Q'

	data['MagPan'] = correspond




	for truc in mag_liste:

		current_dict = dict()
		
		current_dict[str(G+truc)]=str(D+truc)

		correspond.update(current_dict)


	data['MagPan'].update(correspond)




	return jsonify(data)



@app.route('/MAJ_budget_max')
def MAJ_budget_max():

	new_budget_max = request.args.get('new_budget_max', 0, type=str)


	

	print("\n new_budget_max =   : ",new_budget_max)

	

	data = {}
	data["new_budget_max"] = new_budget_max

	mon_client.budget_max = new_budget_max

	return jsonify(data)

	


@app.route('/AllerPayer', methods=['GET', 'POST'])
def AllerPayer():
	
	if request.method == 'POST':
		CBnumber = request.form["CBnumber"]
		cryptogramme = request.form["cryptogramme"]
		
		
		print("\n\n\n ")
		print("\n CBnumber   : ", CBnumber)
		print("\n cryptogramme   : ", cryptogramme)
		print("\n\n\n ")
		
		CBnumber = int(CBnumber)
		cryptogramme = int(cryptogramme)
		
		if  CBnumber == 12000 + cryptogramme:
			print("\n CBnumber et cryptogramme concordants ;-) ")
			print("\n\n\n ")
			mon_client.braquerMag()
			print("\n mon_client.braquerMag() ")
			return redirect(url_for('index'))
			
		else:
			print("\n CBnumber et cryptogramme NON concordants  !!!")
			flash(u' QUELQUECHOSE NE VAS PAS','error')
			print("\n\n\n ")
			error = 6
			return redirect(url_for('RedPage',error=error))
		
		
		
		
		

	else:
		pan_PRIX = mon_panier.pan_PRIX
		return render_template('AllerPayer.html',mon_mag =mon_mag,mon_client=mon_client,mon_panier=mon_panier,mon_ecom=mon_ecom)
	
		
	


@app.route('/')
def index():
    return render_template('index.html', mon_mag =mon_mag,mon_client=mon_client,mon_panier=mon_panier,mon_ecom=mon_ecom)

	

@app.route('/RedPage')	
def RedPage():
	return render_template('RedPage.html', mon_mag =mon_mag,mon_client=mon_client,mon_panier=mon_panier,mon_ecom=mon_ecom)



if __name__ == "__main__":
	app.secret_key = 'super secret key'
	

	
	app.config['SECRET_KEY'] = 'super secret key'
	

	app.debug = True
	app.run()

