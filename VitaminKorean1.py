# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 03:07:35 2020
@author: cardcaptr

"This is an edited version of the code at the following url: "
"https://www.geeksforgeeks.org/downloading-files-web-using-python/"
"The following will install the Vitamin Korean 1's mp3 files in the same directory as this .py file"
"""
#make sure these packages are installed
import requests 
from bs4 import BeautifulSoup

''''''

# specify the URL of the archive here 
archive_url = "http://www.darakwon.co.kr/mp3/FileDown_kor2.asp?p_id=6763&pf_type=5"

def get_mp3_links(): 
	
	# create response object 
	r = requests.get(archive_url) 
	
	# create beautiful-soup object 
	soup = BeautifulSoup(r.content,'html5lib') 
	
	# find all links on web-page 
	links = soup.findAll('a')
    
	# filter the link sending with .mp3
	mp3_links = ["http://www.darakwon.co.kr/mp3/"+ link['href'] for link in links if "mp3" in link['href']] 

	return mp3_links 


def download_mp3_series(mp3_links):
    n=1
    for link in mp3_links:
        '''iterate through all links in mp3_links 
		and download them one by one'''
        
		# obtain filename by splitting knowing in advance what the filename is
        # pretty brute force method, could be generalized
        n_s=str(n)
        file_name = "비타민한국어1_00"+n_s+".mp3"
        print ("Downloading file: %s" % file_name)
		
		# create response object 
        r = requests.get(link, stream = True) 
		
		# download started 
        with open(file_name, 'wb') as f: 
            for chunk in r.iter_content(chunk_size = 1024*1024): 
                if chunk: 
                    f.write(chunk) 
                    
        print ("%s downloaded!\n"%file_name)
        n=n+1
    print ("All mp3 downloaded!")
    return


if __name__ == "__main__": 

	# getting all video links 
	mp3_links = get_mp3_links() 

	# download all videos 
	download_mp3_series(mp3_links) 
	
