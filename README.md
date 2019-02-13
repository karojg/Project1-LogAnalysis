## Log Analysis - FullStack Web Developer NanoDegree

Project #1 of Udacity's FullStack WebDeveloper Nanodegree. 

## Objective

Objective of project is to apply SQL knowldege and improve skills. Project creates a reporting tool that answers the next questions:

**1. What are the most popular three articles of all time?** Which articles have been accessed the most? 

**2. Who are the most popular article authors of all time?** That is, when you sum up all of the articles each author has written, which authors get the most page views? 

**3. On which days did more than 1% of requests lead to errors?** The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

## Requirements

Minimum requirements correspond to:

- Python 2.7.12
- psycopg2 2.7.7
- PostgreSQL 9.5.14

This can also be achieved via a Virtual Machine and Vagrant.

## Instructions using VM and VirtualBox

- Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox.](https://www.virtualbox.org/wiki/Downloads)

- Clone the repository to your local machine

- Start the virtual machine: in project directory run `vagrant up` and then `vagrant ssh`

- Download and unzip the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). This file should be place into your vagrant directory.

- Load the database `psql -d news -f newsdata.sql;`

- Run Project `python newsdata.py`

## Results

![output](/Users/karojg/Documents/Education/Udacity_FullStack/Projects/Project1_LogAnalysis/FSND-Virtual-Machine/vagrant/newsdata/output.png)