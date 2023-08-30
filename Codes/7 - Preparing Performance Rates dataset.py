# -*- coding: utf-8 -*-

'''
In this code, we use the public available datasets and data obtained by
request to the Ministry of Education to create a  timeseries of students
performance rates (approval, failure and dropout rates) of
students for each year of school, municipality and dependence.
'''

import numpy as np
import pandas as pd
import os

# Setting working directory
os.chdir(r'C:\Users\Users\Documents\Artigos\FDN Outcomes')


''' From 1996 to 2005, we requested via Information Access Law (LAI) to access tables from
1995 to 2007 of performance rates to the Education Ministery. We received the tables from 1996 to
2005 and 2007. For 2006, the argue that they don't have the information, due to a change in the
methodology of the census '''


Perf_Rates_1996_2005 = pd.DataFrame()
for i in range(1996, 2005+1):
    # Reading file
    Perf_Rates_year= pd.read_excel(fr'Inputs\Censo Escolar\Performance Rates\Taxas_de_rendimento_1996-2005-2007\tx_rendimento_municipio_{i}.xls',
                                header = 7)
       
    # Renaming
    Perf_Rates_year.columns = np.append(['Ano','Região','UF', 'Código do UF',
                                   'Nome do Município','Código do Município','Localização','Rede'],Perf_Rates_year.columns[8:])
    
    # Selecting Localization = "Total" (Urban + Rural) and "Rede" is Private or Public or Total
    Perf_Rates_year = Perf_Rates_year[Perf_Rates_year['Localização'] == 'Total']	
    Perf_Rates_year = Perf_Rates_year[Perf_Rates_year['Rede'].isin(['Particular','Publico','Pública',
                                                                    'Privada','Total'])]	
    
    # Selecting columns
    if i in [2004, 2005]:
        Perf_Rates_year = Perf_Rates_year.iloc[:,[0,5,7,12,13,14,15,16,17,18,19,9,10,8,
                                     20, 29,30,31,32,33,34,35,36,26,27,25,
                                     37,46,47,48,49,50,51,52,53,43,44,42,54]]
    elif i in [2003]:
        Perf_Rates_year = Perf_Rates_year.iloc[:,[0,5,7,11,12,13,14,15,16,17,18,9,10,8,19,
                                     27,28,29,30,31,32,33,34,25,26,24,35,
                                     43,44,45,46,47,48,49,50,41,42,40,51]]
    elif i in [2000,2001,2002]:
        Perf_Rates_year = Perf_Rates_year.iloc[:,[0,4,7,11,12,13,14,15,16,17,18,9,10,8,19,
                                     27,28,29,30,31,32,33,34,25,26,24,35,
                                     43,44,45,46,47,48,49,50,41,42,40,51]]        
    elif i in [1996,1998]:
        Perf_Rates_year = Perf_Rates_year.iloc[:,[0,5,7,8,9,10,11,12,13,14,15,16,17,18,23,
                                     24,25,26,27,28,29,30,31,32,33,34,39,
                                     40,41,42,43,44,45,46,47,48,49,50,55]]    
    elif i in [1997,1999]:
        Perf_Rates_year = Perf_Rates_year.iloc[:,[0,4,7,11,12,13,14,15,16,17,18,9,10,8,19,
                                     27,28,29,30,31,32,33,34,25,26,24,35,
                                     43,44,45,46,47,48,49,50,41,42,40,51]]

    # Renaming
    Perf_Rates_year.columns = ['Year', 'Code', 'Dependence','Approv_Rate_1_Year',
                         'Approv_Rate_2_Year','Approv_Rate_3_Year','Approv_Rate_4_Year',
                         'Approv_Rate_5_Year','Approv_Rate_6_Year','Approv_Rate_7_Year',
                         'Approv_Rate_8_Year','Approv_Rate_1to4_Year','Approv_Rate_5to8_Year',
                         'Approv_Rate_1to8_Year','Approv_Rate_High_School',
                         'Fail_Rate_1_Year','Fail_Rate_2_Year','Fail_Rate_3_Year',
                         'Fail_Rate_4_Year','Fail_Rate_5_Year','Fail_Rate_6_Year',
                         'Fail_Rate_7_Year','Fail_Rate_8_Year','Fail_Rate_1to4_Year',
                         'Fail_Rate_5to8_Year','Fail_Rate_1to8_Year',
                         'Fail_Rate_High_School',
                         'Drop_Rate_1_Year','Drop_Rate_2_Year','Drop_Rate_3_Year',
                         'Drop_Rate_4_Year','Drop_Rate_5_Year','Drop_Rate_6_Year',
                         'Drop_Rate_7_Year','Drop_Rate_8_Year','Drop_Rate_1to4_Year',
                         'Drop_Rate_5to8_Year','Drop_Rate_1to8_Year',
                         'Drop_Rate_High_School']
    
    Perf_Rates_year['Year'] = Perf_Rates_year['Year'].astype(int)
    
    # Appending
    Perf_Rates_1996_2005 = pd.concat([Perf_Rates_1996_2005, Perf_Rates_year], axis = 'rows').reset_index(drop = True)


# Converting code to string
Perf_Rates_1996_2005['Code'] = Perf_Rates_1996_2005['Code'].astype(str).str.rstrip('.0')

# Replace 'Privada' with 'Particular' and 'Pública' with 'Publico'
Perf_Rates_1996_2005 = Perf_Rates_1996_2005.replace({'Privada':'Particular', 'Pública':'Publico'})









''' For 2006 on, we have the rates already calculated by the Education Ministery '''
# Source: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-rendimento-escolar
# Performance rates
Perf_Rates_2007_2022 = pd.DataFrame()
for i in range(2007, 2022+1):
    
    # Reading file
    if i in [2007,2008,2009,2010,2011]:
        Perf_Rates_year= pd.read_excel(fr'Inputs\Censo Escolar\Performance Rates\TX RENDIMENTO MUNICIPIOS {i}.xls',
                                    header = 7)
        # In 2007 and 2011, information is divided into 2 sheets
        if i in [2007,2011]:
            Perf_Rates_year_part2 = pd.read_excel(fr'Inputs\Censo Escolar\Performance Rates\TX RENDIMENTO MUNICIPIOS {i}.xls',
                                        header = 7, sheet_name = 1)
            Perf_Rates_year = pd.concat([Perf_Rates_year, Perf_Rates_year_part2], axis = 'rows')  
    else:
        Perf_Rates_year= pd.read_excel(fr'Inputs\Censo Escolar\Performance Rates\TX RENDIMENTO MUNICIPIOS {i}.xlsx',
                                    header = 7)
    
    if i == 2013:
        Perf_Rates_year= pd.read_excel(fr'Inputs\Censo Escolar\Performance Rates\TX RENDIMENTO MUNICIPIOS {i}.xlsx',
                                    header = 7, decimal = '.', na_values = '--')

    # Renaming
    Perf_Rates_year.columns = np.append(['Ano','Região','UF','Código do Município',
                                   'Nome do Município','Localização','Rede',
                                   'Aprovação no 1º Ano do Ensino Fundamental'],Perf_Rates_year.columns[8:])
    
    # Selecting Localization = "Total" (Urban + Rural) and "Rede" is Private or Public or Total
    Perf_Rates_year = Perf_Rates_year[Perf_Rates_year['Localização'] == 'Total']	
    Perf_Rates_year = Perf_Rates_year[Perf_Rates_year['Rede'].isin(['Particular','Publico','Pública',
                                                                    'Privada','Total'])]	
    
    # Selecting columns
    if i in range(2007, 2010+1):
        Perf_Rates_year = Perf_Rates_year.iloc[:,[0,3,6,8,9,10,11,12,13,14,15,18,16,17,24,26,27,
                                                  28,29,30,31,32,33,34,35,36,42,44,45,46,47,
                                                  48,49,50,51,52,53,54,60]]
    else:
        Perf_Rates_year = Perf_Rates_year.iloc[:,[0,3,6,11,12,13,14,15,16,17,18,8,9,7,
                                                  19,29,30,31,32,33,34,35,36,26,27,25,37,
                                                  47,48,49,50,51,52,53,54,44,45,43,55]]
    
    # Renaming
    Perf_Rates_year.columns = ['Year', 'Code', 'Dependence','Approv_Rate_1_Year',
                         'Approv_Rate_2_Year','Approv_Rate_3_Year','Approv_Rate_4_Year',
                         'Approv_Rate_5_Year','Approv_Rate_6_Year','Approv_Rate_7_Year',
                         'Approv_Rate_8_Year','Approv_Rate_1to4_Year','Approv_Rate_5to8_Year',
                         'Approv_Rate_1to8_Year','Approv_Rate_High_School',
                         'Fail_Rate_1_Year','Fail_Rate_2_Year','Fail_Rate_3_Year',
                         'Fail_Rate_4_Year','Fail_Rate_5_Year','Fail_Rate_6_Year',
                         'Fail_Rate_7_Year','Fail_Rate_8_Year','Fail_Rate_1to4_Year',
                         'Fail_Rate_5to8_Year','Fail_Rate_1to8_Year',
                         'Fail_Rate_High_School',
                         'Drop_Rate_1_Year','Drop_Rate_2_Year','Drop_Rate_3_Year',
                         'Drop_Rate_4_Year','Drop_Rate_5_Year','Drop_Rate_6_Year',
                         'Drop_Rate_7_Year','Drop_Rate_8_Year','Drop_Rate_1to4_Year',
                         'Drop_Rate_5to8_Year','Drop_Rate_1to8_Year',
                         'Drop_Rate_High_School']
    
    Perf_Rates_year['Year'] = Perf_Rates_year['Year'].astype(int)
    
    # Appending
    Perf_Rates_2007_2022 = pd.concat([Perf_Rates_2007_2022, Perf_Rates_year], axis = 'rows').reset_index(drop = True)


# Converting code to string
Perf_Rates_2007_2022['Code'] = Perf_Rates_2007_2022['Code'].astype(str).str.rstrip('.0')

# Replace 'Privada' with 'Particular' and 'Pública' with 'Publico'
Perf_Rates_2007_2022 = Perf_Rates_2007_2022.replace({'Privada':'Particular', 'Pública':'Publico'})



''' Concatting every year together'''
Performance_Rates_1995_2022 = pd.concat([Perf_Rates_1996_2005, Perf_Rates_2007_2022], axis = 'rows')


# Export the complete dataset as excel
Performance_Rates_1995_2022.to_excel('Outputs\Performance_Rates_by_Municip.xlsx', index = False)



# Selecting some important columns and exporting them 
Performance_Rates_1995_2022 = Performance_Rates_1995_2022[['Year', 'Code', 'Dependence',
                                #'Approv_Rate_1_Year', 'Approv_Rate_2_Year', 'Approv_Rate_3_Year',
                                #'Approv_Rate_4_Year', 'Approv_Rate_5_Year', 'Approv_Rate_6_Year',
                                #'Approv_Rate_7_Year', 'Approv_Rate_8_Year', 'Approv_Rate_9_Year',
                                #'Approv_Rate_10_Year', 'Approv_Rate_11_Year', 'Approv_Rate_12_Year',
                                'Approv_Rate_1to4_Year','Approv_Rate_5to8_Year',
                                'Approv_Rate_1to8_Year', 'Approv_Rate_High_School', 
                                #'Fail_Rate_1_Year','Fail_Rate_2_Year', 'Fail_Rate_3_Year', 
                                #'Fail_Rate_4_Year','Fail_Rate_5_Year', 'Fail_Rate_6_Year',
                                #'Fail_Rate_7_Year','Fail_Rate_8_Year', 'Fail_Rate_9_Year', 
                                #'Fail_Rate_10_Year','Fail_Rate_11_Year', 'Fail_Rate_12_Year',
                                'Fail_Rate_1to4_Year','Fail_Rate_5to8_Year',
                                'Fail_Rate_1to8_Year','Fail_Rate_High_School',
                                #'Drop_Rate_1_Year', 'Drop_Rate_2_Year','Drop_Rate_3_Year', 
                                #'Drop_Rate_4_Year', 'Drop_Rate_5_Year','Drop_Rate_6_Year', 
                                #'Drop_Rate_7_Year', 'Drop_Rate_8_Year','Drop_Rate_9_Year',
                                #'Drop_Rate_10_Year', 'Drop_Rate_11_Year','Drop_Rate_12_Year',
                                'Drop_Rate_1to4_Year','Drop_Rate_5to8_Year',
                                'Drop_Rate_1to8_Year', 'Drop_Rate_High_School']].reset_index(drop = True)


# Transform columns into numerical
Performance_Rates_1995_2022.iloc[:,3:] = Performance_Rates_1995_2022.iloc[:,3:].replace('--',np.nan).astype(float)


# Export as excel
Performance_Rates_1995_2022.to_excel('Outputs\Education_by_Municip.xlsx', index = False)







#### Examples of cities

# Manaus
Manaus = Performance_Rates_1995_2022[(Performance_Rates_1995_2022['Code'] == '1302603')&
                                (Performance_Rates_1995_2022['Dependence'] == 'Total')]
# São Paulo
Sao_Paulo = Performance_Rates_1995_2022[(Performance_Rates_1995_2022['Code'] == '3550308')&
                                (Performance_Rates_1995_2022['Dependence'] == 'Total')]


### Plotting some charts

# São Paulo Drop out rate

import matplotlib.pyplot as plt
# changing font size
plt.rcParams.update({'font.size': 20}) 

# Chart
fig, ax = plt.subplots(figsize=(15, 10))
ax.plot(Sao_Paulo[['Drop_Rate_1to8_Year']].set_index(Sao_Paulo['Year']), linewidth = 3, color = 'black')
ax.grid(axis='y', color='lightgrey', linestyle='dashed')
ax.tick_params(axis='x', rotation=90)
ax.tick_params(axis='y',  left='on')
ax.set_xticks(Sao_Paulo['Year'])
ax.legend(['Dropout Rate 1 to 8 Year, São Paulo'])
#plt.savefig(f'Outputs/Figures/Precipitation_by_month.png',facecolor='white', bbox_inches = 'tight', dpi = 1000)  
plt.show()


