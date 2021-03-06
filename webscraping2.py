# -*- coding: utf-8 -*-
"""webscraping2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c41_eBeEwE_w1XN1MH6h25Z12kOqC6y7
"""

import requests

url = 'https://www.python.org/jobs/'
req = requests.get(url)

req

req.text

req.text[:200]

from bs4 import BeautifulSoup

soup = BeautifulSoup(req.text, 'lxml')

jobs = soup.find('ol', {'class':'list-recent-jobs'})

jobs

type(jobs.findAll())

jobs.findAll('li')

for job in jobs.findAll('li'):
    d = dict()
    d['company name'] = job.find('span' ,{'class':'listing-company-name'}).text
    d['job type'] = job.find('span' , {'class':'listing-job-type'}).text
    d['company location'] = job.find('span', {'class':'listing-location'}).text
    d['time posted'] = job.find('span', {'class':'listing-posted'}).text
    d['company category'] = job.find('span', {'class':'listing-company-category'}).text
    print(d)

l_head = []
for j in jobs.findAll('h2'):
    l_head.append(j.find('a').text)
l_head

l_company_loc = []
for j in jobs.findAll('h2'):
    l_company_loc.append(j.find('span', {'class':'listing-location'}).text)
l_company_loc

l_comp_cat = []
for j in jobs.findAll('span', {'class':'listing-company-category'}):
    l_comp_cat.append(j.find('a').text)
l_comp_cat

l_company_name=[]
for j in jobs.findAll('span' ,{'class':'listing-company-name'}):
  l_company_name.append(j.find('a').text)
l_company_name

l_job_type =[]
for j in jobs.findAll('span',{'class':'listing-job-type'}):
  l_job_type.append(j.find('a').text)
l_job_type

l_time_posted =[]
for j in jobs.findAll('span', {'class':'listing-posted'}):
  l_time_posted.append(j.find('time').text)
l_time_posted

import pandas as pd
df=pd.DataFrame()
df['company name']=l_company_name
df['job type']=l_job_type
df['company location']=l_company_loc
df['time posted']=l_time_posted
df['company categray']=l_comp_cat
df



