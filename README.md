1. Edit my.cnf, adding the information of your database
2. Run 'docker build -t manage:1.0 . '
3. Run 'docker run -d -p 8000:8000 manage:1.0'
4. Go to http://127.0.0.1:8000/comments/query_comments/ in your local browser
