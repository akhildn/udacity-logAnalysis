#!/usr/bin/env python3
import psycopg2, bleach

DBNAME = "news"

def popular_articles():
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  #fixed as per review displays only top 3
  c.execute(" select a.id, a.title, count(l.path) as count from log l, articles a where l.path like '%'||a.slug group by (a.id) order by count desc limit 3")
  slugs = c.fetchall()
  db.close()
  return slugs

def popular_authors():
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select au.name, count(l.path) as count from log l, articles a, authors au where l.path like '%'||a.slug and a.author = au.id group by (au.name) order by count desc;")
  authors = c.fetchall()
  db.commit()
  db.close()
  return authors

def get_error_rates():
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  #fixed as per review, displays only the ones which are greater than 1.5 (stated in project built it chapter)
  c.execute("select date, rate from (select e.date, ((e.errors*100)::decimal/d.total_activity)::decimal as rate from error_stats e, day_acitvity d where d.date = e.date order by rate desc) as r where r.rate >1.5")
  errors = c.fetchall()
  db.commit()
  db.close()
  return errors


