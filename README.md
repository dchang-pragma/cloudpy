# cloudpy
create config.ini in the same directory as app.py
test ignore


mysql notes

We put two placeholders (%)  inside the UPDATE statement, one for book title and the other for book id. We passed both  UPDATE statement ( query ) and  (title,id) tuple to the  execute() method. The connector will interpret the query to the following:


UPDATE books
SET title = 'The Giant on the Hill *** TEST ***'
WHERE id = 37

It is important to understand that we should always use placeholders ( %s) inside any SQL statements that contain input from users. This helps us prevent SQL injection.

Let’s test our new module to see if it works.

First, we select the book with id 37:



SELECT * FROM books
WHERE id = 37;

Python MySQL Update Example Before Changes

Second, we run the module.

Third, we select the book entry by executing the  SELECT statement above again to see if it is really changed.

Python MySQL Update After Changes

It works as expected.

In this tutorial, you have learned how how to update data by using MySQL Connector/Python API.