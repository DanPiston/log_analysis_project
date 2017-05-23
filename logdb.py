#!/usr/bin/env python3

# Database log project for Udacity
import psycopg2
from datetime import date
DBNAME = 'news'

db = psycopg2.connect(database=DBNAME)


def get_top_three():
    """Returns top 3 artiles by visits"""
    c = db.cursor()
    query = """
           select art_paths.title, count(log.path) as count
           from art_paths join log
           on art_paths.path = log.path
           group by art_paths.title
           order by count desc
           limit 3;
           """
    c.execute(query)
    top_list = c.fetchall()
    c.close()
    results = 'The Top 3 Articles:\n'
    for entry in top_list:
        results += '{} --- {} views\n'.format(entry[0], entry[1])
    return results


def get_author_info():
    """Returns list of Authors by popularity"""
    c = db.cursor()
    query = """
            select author_path.name, count(author_path.path) as count
            from author_path join log
            on author_path.path = log.path
            group by author_path.name
            order by count desc;
            """
    c.execute(query)
    author_info = c.fetchall()
    c.close()
    author_list = '\nThe Most Popular Authors:\n'
    for author in author_info:
        author_list += '{} -- {} views\n'.format(author[0], author[1])
    return author_list


def get_bad_days():
    """Return days when bad request > 1%"""
    c = db.cursor()
    query = """
            select date_trunc('day', time) as day,
            round((count(case when status != '200 OK'
            then 1 else null end) * 100)::numeric /count(*), 1) as percent
            from log
            group by day
            order by day desc;
            """
    c.execute(query)
    requests_log = c.fetchall()
    c.close()
    bad_days = '\nDays When Errors >= 1%:\n'
    for day in requests_log:
        correct_date = date.strftime(day[0], "%b %d, %Y")
        if day[1] >= 1:
            bad_days += '{} -- {}% errors\n'.format(correct_date, day[1])
    return bad_days


def write_report():
    """Writes report"""
    time = date.today()
    report_file = open('{}.txt'.format(time), 'w')
    report_file.write(get_top_three() + get_author_info() + get_bad_days())
    report_file.close()
    print(get_top_three() + get_author_info() + get_bad_days())


write_report()
