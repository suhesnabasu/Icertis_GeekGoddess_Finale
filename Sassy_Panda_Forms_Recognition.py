# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 16:19:25 2020

@author: Sassy Panda
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import re
import matplotlib.pyplot as plt

def main():
    r = requests.get('https://www.sec.gov/forms')
    soup = bs(r.text,features="lxml")
    download_link = soup.select('td[class="display-title-content views-field views-field-field-display-title"]')
    data = []
    #male_flag = False
    #female_flag = False
    count = 5;
    for each_link in download_link:
        #print(each_link.a['href'])
        print(each_link.a.get_text())
        pdf_link = "https://www.sec.gov" + each_link.a['href']
        #print(findWholeWord('he')(str(requests.get(pdf_link).content)))
        
        if findWholeWord('he')(str(requests.get(pdf_link).content)) is not None:
            #male_flag = True
            #data['Gender'].append('Male')
            #data['Names'].append(each_link.a.get_text())
            data.append([each_link.a.get_text(), 'Male'])
        elif findWholeWord('she')(str(requests.get(pdf_link).content)) is not None:
            #female_flag = True
            #data['Gender'].append('Female')
            #data['Names'].append(each_link.a.get_text())
            data.append([each_link.a.get_text(), 'Female'])
        elif findWholeWord('he')(str(requests.get(pdf_link).content)) is not None and findWholeWord(' she ')(str(requests.get(pdf_link).content)) is not None:
            #data['Gender'].append('Both')
            #data['Names'].append(each_link.a.get_text())
            data.append([each_link.a.get_text(), 'Both'])
        elif findWholeWord('he/she')(str(requests.get(pdf_link).content)) is not None:
            #data['Gender'].append('Both')
            #data['Names'].append(each_link.a.get_text())
            data.append([each_link.a.get_text(), 'Both'])
            
        count = count - 1
        if count == 0:
            break
        
        
        print("[Done]")

    print(data)
    #print(data.keys())
    #print(data.values())
    #keys = list(data.keys())
    #values = list(data.values())
    df = pd.DataFrame(data, columns=['Names', 'Gender'])
    print(df)

    #plt.plot(keys, values)
    count_values = df['Gender'].value_counts()
    print(count_values)
    print(type(count_values))
    df.Gender.value_counts().plot(kind='bar')
    #plt.bar(df['Gender'].value_counts())
    '''new = pd.DataFrame.from_dict(data, orient='index')
    print(new.describe)'''
    plt.show()
      
    #print(data)
    
def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search    
    
# Driver Code 
if __name__ == '__main__': 
    
    # Calling main() function 
    main() 