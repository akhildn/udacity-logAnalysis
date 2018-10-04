#!/usr/bin/env python3
import psycopg2

DBNAME = "news"


def popular_articles():
    """Return top 3 articles from the 'news-database' with most views first"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # fixed as per review displays only top 3
    c.execute("SELECT a.id, a.title, COUNT(l.path) AS views "
              "FROM log l, articles a "
              "WHERE l.path = '/article/'||a.slug "
              "GROUP BY (a.id) "
              "ORDER BY views DESC limit 3")
    slugs = c.fetchall()
    db.close()
    return slugs


def popular_authors():
    """Return top authors from the 'news-database' with most views first"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT au.name, COUNT(l.path) AS views "
              "FROM log l, articles a, authors au "
              "WHERE l.path = '/article/'||a.slug "
              "AND a.author = au.id "
              "GROUP BY (au.name) "
              "ORDER BY views DESC;")
    authors = c.fetchall()
    db.commit()
    db.close()
    return authors


def get_error_rates():
    """Returns days which had more than 1.5% errors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # fixed as per review, displays only the ones which are greater than 1.5
    # (stated in project built it chapter)
    c.execute("SELECT date, rate "
              "FROM "
              "(SELECT e.date, "
              "((e.errors*100)::DECIMAL/d.total_activity)::DECIMAL as rate "
              "FROM error_stats e, day_acitvity d "
              "WHERE d.date = e.date "
              "ORDER BY rate DESC) "
              "AS r "
              "WHERE r.rate >1.5")
    errors = c.fetchall()
    db.commit()
    db.close()
    return errors
