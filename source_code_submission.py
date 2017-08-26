import psycopg2

DBNAME = 'news'




def popular_articles():
	db = psycopg2.connect(database = DBNAME)
	c = db.cursor()
	c.execute("select articles.title,count(articles.title) from log,articles where log.path like '%'||articles.slug group by articles.title order by count(articles.title)desc limit 3")
	rows= c.fetchall()
	db.close()
	for value in rows:
		print '\t',(rows.index(value)+1), value[0], '--', value[1], "views"
		

	


def popular_authors():
	db = psycopg2.connect(database = DBNAME)
	c = db.cursor()
	c.execute("select authors.name, sum(authortitlecount.count) from authors, authortitlecount where authortitlecount.author_id = authors.id group by name order by sum desc")
	rows= c.fetchall()
	db.close()
	
	for value in rows:
		
		print '\t', (rows.index(value)+1),value[0], '--', value[1], 'views'

	#create view authortitlecount as select articles.author as author_id,maxes.title,maxes.count from (select articles.title,count(articles.title) from log,articles where log.path like '%'||articles.slug group by articles.title)as maxes,articles where maxes.title = articles.title;


def days_of_request_errors():
	db = psycopg2.connect(database = DBNAME)
	c = db.cursor()
	c.execute("select query.date, round(query.number,2) from (select itsok.date, (cast(notok.count as decimal(10,2)) /(cast(itsok.count as decimal(10,2))+cast(notok.count as decimal(10,2)))*100) as number from itsok, notok where itsok.date = Notok.date) as query where query.number > 1")
	rows= c.fetchall()
	db.close()

	for value in rows:
		
		print '\t', (rows.index(value)+1),value[0], '--', value[1],'%'
	


	#create view itsok as select count(itsok.date), itsok.date from (select status, date(time) from log where status = '200 OK') as itsok group by itsok.date;

	#create view notok as select count(notok.date),notok.date from (select status,date(time) from log where status != '200 OK') as notok group by notok.date;

print "What are the most popular 3 articles of all time?"
popular_articles()
print "Who are the most popular article authors of all time?"
popular_authors()
print "On which days did more than 1% of requests lead to errors?"
days_of_request_errors()

