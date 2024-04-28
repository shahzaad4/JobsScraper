import csv

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import datetime

jobs = []

def get_data():
    first_page = urlopen(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=")
    doc = BeautifulSoup(first_page, "html.parser")
    posts = doc.find_all('li', class_='clearfix job-bx wht-shd-bx')


    for post in posts:
        job_title = post.find("h2").get_text().strip()
        company = post.find("h3", {"class": "joblist-comp-name"}).get_text().strip()
        location = post.find("ul", {"class": "top-jd-dtl clearfix"}).find("span").get_text().strip()
        job_desc = post.find("ul", {"class": "list-job-dtl clearfix"}).find_all("li")[0].text.replace(
            "Job Description:", "").strip()
        key_skills = post.find("ul", {"class": "list-job-dtl clearfix"}).find("span", {
            "class": "srp-skills"}).get_text().strip()
        time_posted=post.find("span",{"class":"sim-posted"}).get_text().strip()
        job_det_url=post.find("a").get('href')

        jobs.append([[job_title],[company],[location],[job_desc],[key_skills],[job_det_url]])

def save_data(jobs):
    date=datetime.date.today()
    with open(f"{date}.csv","w",newline="") as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(['Job Details','Company Name','Location','Job Description','Skills','More Info'])
        for job in jobs:
            writer.writerow(job)
get_data()
save_data(jobs)
