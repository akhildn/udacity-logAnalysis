#Project Log Analysis

How to run:
-load the news database. `psql -d news -f newsdata.sql`
-create 2 views in the news database
	1. `create view error_stats as 
			select time::timestamp::date as date, count(*) as errors
			from log 
			where status like '4%' or status like '5%'
			group by (date);`
	2. 	`create view day_acitvity as 
			select time::timestamp::date as date, count(*) as total_activity
			from log 
			group by (date);`	
-to run type `python main.py` in shell
-open `localhost:8000` in your browser
-querying is slow, so please wait until the page is completely loaded.

			