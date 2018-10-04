create view error_stats as 
			select time::timestamp::date as date, count(*) as errors
			from log 
			where status like '4%' or status like '5%'
			group by (date);
			
create view day_acitvity as 
			select time::timestamp::date as date, count(*) as total_activity
			from log 
			group by (date);