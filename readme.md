# Project Log Analysis

## Description
	
	Developed as a part of course work in udacity full stack web development nanodegree. Task given was to develop an internal reporting tool 
which will use the information from  the database which has over a million rows. 

Queries were writtern to find out:
	1. Top 3 articles with most views
	2. Most popular authors by number of views for all his articles
	3. On which days did more than 1% of requests lead to errors 

Tables in database:

1. articles: containts information about articles like who is the author for the atricle, title for the article, when was it published, and 
             content in the article 	

	
| Column |           Type           |                       Modifiers                      |
|-------+|-------------------------+|------------------------------------------------------|
| author | integer                  | not null                                             |
| title  | text                     | not null						   |
| slug   | text                     | not null						   |
| lead   | text                     |							   |
| body   | text                     |							   |
| time   | timestamp with time zone | default now()					   |
| id     | integer                  | not null default nextval('articles_id_seq'::regclass)|

`Indexes:
    "articles_pkey" PRIMARY KEY, btree (id)
    "articles_slug_key" UNIQUE CONSTRAINT, btree (slug)
Foreign-key constraints:
    "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)`
	
	
2. authors: contains thier name and thier bio

| Column |  Type   |                      Modifiers                      |
|-------+|--------+|-----------------------------------------------------|
 name   | text     | not null						 |
 bio    | text     |                                                     |  
 id     | integer  | not null default nextval('authors_id_seq'::regclass)|

`Indexes:
    "authors_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "articles" CONSTRAINT "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)`


3. log: contains info about all requests made to the articles 

| Column |           Type           |                    Modifiers                    |
|-------+--------------------------+|-------------------------------------------------|
| path   | text                     |                                                 |
| ip     | inet                     |                                                 |
| method | text                     |                                                 |
| status | text                     |                                                 |
| time   | timestamp with time zone | default now()                                   |
| id     | integer                  | not null default nextval('log_id_seq'::regclass)|

`Indexes:
    "log_pkey" PRIMARY KEY, btree (id)`


	

## Requirements

You can run this project using Vagrant if you do not have unix based environment already set up, 
if you do you just need the e requirements which are stated below.

	###What do you need to run this project:
		1. Python : v3
		2. PostgreSQL
		3. psycopg2 

	### How to set up Vagrant
		1. You can view about vagrant here : https://www.vagrantup.com/intro/index.html
		2. Download and install vagrant. (Download: https://www.vagrantup.com/downloads.html) 
		3. You would also need `Virtual Box` for the set up. (Download: https://www.virtualbox.org/wiki/Downloads)
		4. Set up the VM configuration. (You can find more info Vagrant docs). You can skip that part if you are using are files in my folder.
		5. Go to the folder which has Vagrant file, and run `vagrant up` in the shell
		6. Then type `vagrant ssh` 
	
	
## How to run:
- Download the news database (download: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
- Unzip the downloaded database file and copy newsdata.sql into your project folder where vagrant is set up
- Now type `psql -d news -f newsdata.sql` , this will set up the database for you.
- create 2 views in the news database, you can do this by running `create_views.sql`. This can be done by typing `psql -d news -f create_views.sql` 	
- to run type `python main.py` in shell
- open `localhost:8000` in your browser
- querying is slow, so please wait until the page is completely loaded.

			
