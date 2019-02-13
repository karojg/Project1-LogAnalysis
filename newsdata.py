#!/usr/bin/env python2

import psycopg2

DBNAME = "news"


def db_connection():
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    return cursor


def popular_articles(cursor):
    print "====================================================="
    print 'What are the most popular three articles of all time?'
    print "====================================================="
    cursor.execute("SELECT articles.title, COUNT(articles.title) as views\
    FROM articles, log WHERE concat('/article/', articles.slug) = log.path\
    GROUP BY articles.title\
    ORDER BY views desc limit 3;")
    articles = cursor.fetchall()
    for article in articles:
        print article[0], "-", article[1], "views"


def popular_authors(cursor):
    print ("\n")
    print "====================================================="
    print "Who are the most popular article authors of all time?"
    print "====================================================="
    cursor.execute("SELECT authors.name, COUNT(articles.author) as views\
    FROM log, articles\
    JOIN authors ON articles.author = authors.id\
    WHERE concat('/article/', articles.slug) = log.path\
    GROUP BY authors.name\
    ORDER BY views DESC;")
    authors = cursor.fetchall()
    for author in authors:
        print author[0], "-", author[1], "views"


def error_days(cursor):
    print("\n")
    print "====================================================="
    print "On which days did more than 1% of requests lead to errors?"
    print "====================================================="

    cursor.execute("SELECT new_time, round(percentage::numeric, 2)\
      FROM\
        (SELECT to_char(time, 'FMMonth DD YYYY') as new_time,\
        (SUM(case when status = '404 NOT FOUND' then 1 else 0 end)::float/\
        COUNT(status)::float)*100 as percentage\
        FROM log\
        GROUP BY new_time) as subquery\
      WHERE percentage > 1.0 order by percentage desc;")
    error_days = cursor.fetchall()
    for error_day in error_days:
        print error_day[0], "-", error_day[1], "%"


if __name__ == '__main__':
    cursor = db_connection()
    popular_articles(cursor)
    popular_authors(cursor)
    error_days(cursor)
    cursor.close()
