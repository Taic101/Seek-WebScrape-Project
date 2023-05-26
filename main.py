from requests_html import HTML, HTMLSession
import csv
import os
session = HTMLSession()


region = 'All-Canterbury'
category = 'information-communication-technology'
page = '1'
keyword = ''

base_url= f"https://www.seek.co.nz/jobs-in-{category}/in-{region}?page={page}"


username = os.getlogin()
name_of_file = 'job_scrape.csv'
save_path = f'C:/Users/{username}/Desktop/'
complete_file_name = os.path.join(save_path, name_of_file)
csv_file = open(complete_file_name, 'w+')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Company', 'Type', 'Location', 'Salary', 'Field', 'Bulletpoints', 'Description'])


req = session.get(base_url)
req.html.render()


def grabJobData():
    
    job = req.html.find('._1wkzzau0.a1msqi7e')
    
    for jobs in job:
        job_title = jobs.find('._1wkzzau0._1wkzzauf._1rct8jy4._1rct8jy6._1rct8jy9.lnocuo2._1rct8jya._1rct8jyd._1wkzzau0._1wkzzauf.a1msqih', first=True).text
        job_company = jobs.find('._1wkzzau0._1wkzzauf._842p0a0', first=True).text
        
        try:
            job_type = jobs.find('._1wkzzau0.a1msqi5i.a1msqi0._6ly8y50', containing='time', first=True).text
        except Exception as e:
            job_type = 'Could not find job type, possibly fixed term'
            
        job_location = jobs.find('div._1wkzzau0.a1msqi6q > span._1wkzzau0.a1msqi4y.lnocuo0.lnocuo1.lnocuo21._1d0g9qk4.lnocuo7', first=True).text
        
        try:
            job_salary_info = jobs.find('._1wkzzau0.v28kuf0.v28kuf4.v28kuf2', first=True).text
        except Exception as e:
            job_salary_info = 'No information given, possibly negotiable'
        
        job_field = jobs.find('div._1wkzzau0.a1msqi6q.a1msqi4u.a1msqi4z > span._1wkzzau0.a1msqi4y.lnocuo0.lnocuo1.lnocuo21._1d0g9qk4.lnocuo7 > div._1wkzzau0.szurmz0.szurmzb > div._1wkzzau0.a1msqigi.a1msqi5a.a1msqig2.szurmz2j > div._1wkzzau0.a1msqir.a1msqif6.a1msqibu.a1msqi4y.a1msqifm > a._1wkzzau0._1wkzzauf._842p0a0', first=True).text
        
        try:
            job_bulletpoints = jobs.find('ul._1wkzzau0._1wkzzau3.szurmz0.szurmz4', first=True).text
        except Exception as e:
            job_bulletpoints = 'No Bulletpoints'
        
        job_description = jobs.find('span._1wkzzau0.a1msqi4y.lnocuo0.lnocuo1.lnocuo22._1d0g9qk4.lnocuo7', first=True).text

        print(job_title)
        print(job_company)
        print(job_type)
        print(job_location)
        print(job_salary_info)
        print(job_field)
        print(job_bulletpoints)
        print(job_description)
        print()
        
        csv_writer.writerow([job_title, job_company, job_type, job_location, job_salary_info, job_field, job_bulletpoints, job_description])
        
        
for n in range(1, 6):
    page = str(n)
    base_url= f"https://www.seek.co.nz/jobs-in-{category}/in-{region}?page={page}"
    req = session.get(base_url)
    req.html.render()
    print(page)
    grabJobData()
        
csv_file.close()

