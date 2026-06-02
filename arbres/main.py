import pandas as pd


df_hds = pd.read_csv('data-raw/hds.csv', sep=';')
df_paris = pd.read_csv('data-raw/paris.csv', sep=';')

# print (df_hds.sample(2).T)
# print (df_paris.sample(2).T)

col_change = {
    'domanialite': 'domaine',
    'libellefrancais': 'nom_francais',
    'hauteurencm': 'hauteur',
    'circonferenceencm': 'circonference',
    'adresse': 'adresse',
    'arrondissement': 'arrondissement'
}

# 1. Renombrar las columnas
df_paris = df_paris.rename(columns=col_change)

# 2. Concatenar verticalmente
# axis=0 significa uno abajo del otro. sort=False mantiene el orden original de las columnas.
resultado = pd.concat([df_hds, df_paris], axis=0, ignore_index=True, sort=False)

# 3. Guardar el resultado
resultado.to_csv('data-raw/unified.csv', index=False)

print (resultado.sample(2).T)

df_hds.rename( columns={
    'NOM_FRANCAIS': 'nom',
    'COMMUNE': 'commune',
    'HAUTEUR': 'hauteur',
    'CIRCONFERENCE': 'circonference',
    'geo_point_2d': 'coord',
}, inplace=True)

df_paris.rename( columns={
    'LIBELLE FRANCAIS': 'nom',
    'HAUTEUR (m)': 'hauteur',
    'CIRCONFERENCE (cm)': 'circonference',
    'geo_point_2d': 'coord',
}, inplace=True)

df_paris['commune'] = 'Paris'

cols = ['nom', 'commune', 'hauteur', 'circonference', 'coord']

df= pd.concat([df_paris[cols], df_hds[cols]], ignore_index=True)

print (df.sample(2).T)

df.to_json('data/unified.json', orient='records', force_ascii=False)