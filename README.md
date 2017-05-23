# Log Anaylsis Project

### To Run Log Report:

1. Assuming you have VirtualBox and Vagrant installed, clone [this whole repo](https://github.com/udacity/fullstack-nanodegree-vm).
2. To run the VM, cd to the directory where you cloned this repo and cd once more to /vagrant and type:
    ```
    vagrant up
    ```
3. Now that the VM is up and running you can type 
    ```
    vagrant ssh
    ```
    Which will connect you to the VM
4. Fire up PSQL by typing 
    ```
    psql news
    ```
    Once in the database create the Views refenced below to have the reports pull properly.
5. With the Views created, place the logdb.py file into the vagrant folder (or you can create you own folder for the program) and run
    ```
    python logdb.py
    ```
    This should show the output of the report in your command line.  A file named by the day's date is also created for record keeping.


Views created:

1 - Art Paths to connect the articles table to the log table:
```SQL
CREATE VIEW art_path AS
    SELECT title, '/article/' || slug AS path 
    FROM articles;
```

2 - author_path created to associate the authors with their article slugs, which can be used in the full path joining the log table:
```SQL
CREATE VIEW author_path AS
    SELECT authors.name, '/article/' || articles.slug AS path
    FROM authors
    JOIN articles 
    ON authors.id = articles.author;
```
