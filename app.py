import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')

# 6 
# Pour le CA par produit
données["ca"] = données["prix"] * données["qte"]

# moyenne 
moy_ca_produit = données.groupby("produit")["ca"].mean()
print('Moyenne du CA par produit :')
print(moy_ca_produit)

# mediane
med_ca_produit = données.groupby("produit")["ca"].median()
print('Médiane du CA par produit :')
print(med_ca_produit)

# Pour le volume des ventes par produit
# moyenne
moy_ca_produit = données.groupby("produit")["qte"].mean()
print('Moyenne du volume par produit :')
print(moy_ca_produit)

# mediane
med_ca_produit = données.groupby("produit")["qte"].median()
print('Médiane du volume par produit :')
print(med_ca_produit)

# Pour le volume des ventes par produit
# l'écart-type
ecarttype_ca_produit = données.groupby("produit")["qte"].std()
print('Écart-type du volume par produit :')
print(ecarttype_ca_produit)

# la variance
variance_ca_produit = données.groupby("produit")["qte"].var()
print('Variance du volume par produit :')
print(variance_ca_produit)

# 7
ventes_par_produit = {}
for produit, quantite in zip(données["produit"], données["qte"]):
	ventes_par_produit[produit] = ventes_par_produit.get(produit, 0) + quantite
#print(ventes_par_produit)

# produit le + vendu
if ventes_par_produit:
	quantite_max = max(ventes_par_produit.values())
	produits_plus_vendus = [
		produit for produit, quantite in ventes_par_produit.items()
		if quantite == quantite_max
	]
	print('Produit le plus vendu :', str(produits_plus_vendus[0]), '-', quantite_max, 'unités')
# ou .join si plusieurs produits ont la même quantité maximale

# produit le - vendu
if ventes_par_produit:
	quantite_min = min(ventes_par_produit.values())
	produits_moins_vendus = [
		produit for produit, quantite in ventes_par_produit.items()
		if quantite == quantite_min
	]
	print('Produit le moins vendu :', str(produits_moins_vendus[0]), '-', quantite_min, 'unités')

# 8
# graphe ventes par produit
figure = px.pie(données, values='qte', names='produit', title='quantité vendue par produit')

figure.write_html('ventes-par-produit.html')

print('ventes-par-produit.html généré avec succès !')

# graphe CA par produit
figure = px.pie(données, values='ca', names='produit', title='CA par produit')

figure.write_html('ca-par-produit.html')

print('ca-par-produit.html généré avec succès !')