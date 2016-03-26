import requests
import bs4
import sys
import os


os.system('clear')


status=open('status.txt','a')

def green():

	dt=sys.argv[1]
	url='http://greenlineservices.in/searchJourneys?source=1308&destination=1060&dateOfJourney='+str(dt)

	response=requests.get(url)
	html=response.text
	soup=bs4.BeautifulSoup(html,"lxml")
	#print soup.prettify()
	rows=soup.select('.search tbody tr')
	print ' '

	print '                        status of greenline bus service  '
	status.write( '                        status of greenline bus service  '+'\n')
	print '-------------------------------------------------------'
	status.write('-------------------------------------------------------'+'\n')

	for row in rows:
		td=row.select('td')
		print 'Departure time : '+td[1].getText()
		status.write('Departure time : '+td[1].getText()+'\n')
		print 'Arrival time : '+td[2].getText()
		status.write('Arrival time : '+td[2].getText()+'\n')
		print 'Number of seats available : '+td[3].select('span')[0].getText()
		status.write('Number of seats available : '+td[3].select('span')[0].getText()+'\n')
		
		print '---------------------------------------------------'
		status.write('---------------------------------------------------'+'\n\n')

def shm():

	dt=sys.argv[1]
	#url='http://greenlineservices.in/searchJourneys?source=1308&destination=1060&dateOfJourney='+str(dt)
	url='http://shyamolibusservice.com/searchJourneys?source=1308&destination=1060&dateOfJourney='+str(dt)

	response=requests.get(url)
	html=response.text
	soup=bs4.BeautifulSoup(html,"lxml")
	#print soup.prettify()
	rows=soup.select('.search tbody tr')
	print ' '

	print '                        status of shyamoli bus service  '
	status.write( '                        status of shyamoli bus service  '+'\n')
	print '-------------------------------------------------------'
	status.write('-------------------------------------------------------'+'\n')

	for row in rows:
		td=row.select('td')
		print 'Departure time : '+td[1].getText()
		status.write('Departure time : '+td[1].getText()+'\n')
		print 'Arrival time : '+td[2].getText()
		status.write('Arrival time : '+td[2].getText()+'\n')
		print 'Number of seats available : '+td[3].select('span')[0].getText()
		status.write('Number of seats available : '+td[3].select('span')[0].getText()+'\n')
		
		print '---------------------------------------------------'
		status.write('---------------------------------------------------'+'\n\n')


print 'querying greenline bus service'
green()		
print 'querying shyamoli bus service'
shm()	
status.close()









