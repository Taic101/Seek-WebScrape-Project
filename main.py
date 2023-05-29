from requests_html import HTML, HTMLSession
import csv
import os

session = HTMLSession()

##Get information from user
region = input("REGION\nRegions must be entered with a '-' symbol between each word (but not before or after) E.g: 'All-Canterbury'\nWork-From-Home is a valid region.\nIf you enter an erroneous input, such as 'idontknowwhattoput', an empty field will be used\nEnter a region: ")
print()
category = input("CATEGORY\nCategory must be entered with a '-' symbol between each word (but not before or after) E.g: 'information-communication-technology'\nEnter a category: ") or " "
print()
page = '1'
keyword = input("KEYWORD\nSame formatting as before E.g 'software-developer'\nPlease note, if a timeout error occurs simply run the script again.\nJust press enter if you do not want to enter a keyword.\nEnter a keyword: ") or " "
print()
pages_to_scrape = int(input("How many pages to scrape? E.g 15\nI reccomend around 20\nPages to scrape: ") or 20)
print()


##Create a base URL and use the user's input as fields
base_url= f"https://www.seek.co.nz/{keyword}-jobs-in-{category}/in-{region}?page={page}"

##Grab the user's windows username
username = os.getlogin()

##Name the file to be created and its path to be saved
name_of_file = 'job_scrape.csv'
save_path = f'C:/Users/{username}/Desktop/'
complete_file_name = os.path.join(save_path, name_of_file)

##Create the csv file
csv_file = open(complete_file_name, 'w+', encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Company', 'Type', 'Location', 'Salary', 'Field', 'Bulletpoints', 'Description'])

##The main function for scraping job data
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
        
##Iterate through the pages the user chose and scrape data from each      
for n in range(1, pages_to_scrape+1):
    page = str(n)
    base_url= f"https://www.seek.co.nz/jobs-in-{category}/in-{region}?page={page}"
    req = session.get(base_url)
    req.html.render()
    print(page)
    grabJobData()
        
csv_file.close()

