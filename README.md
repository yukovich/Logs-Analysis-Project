# Logs-Analysis-Project
Project under Udacity full stack nano degree

Navigate to your 'news' postresql database in the command line and run the following 3 SQL commands to create the views for the program to work:

	create view authortitlecount as select articles.author as author_id,maxes.title,maxes.count from (select articles.title,count(articles.title) from log,articles where log.path like '%'||articles.slug group by articles.title)as maxes,articles where maxes.title = articles.title;

	create view itsok as select count(itsok.date), itsok.date from (select status, date(time) from log where status = '200 OK') as itsok group by itsok.date;

	create view notok as select count(notok.date),notok.date from (select status,date(time) from log where status != '200 OK') as notok group by notok.date;

On your server command line, navigate to where you have saved source_code_submission.py and run it with "python source_code_submission.py".
