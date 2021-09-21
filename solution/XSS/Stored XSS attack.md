# Stored XSS attack
## 1. Detect 
In the Comment section of the article with each user's comment, the system will save it in the database and post it later.

![image](https://user-images.githubusercontent.com/63194321/133422051-2ad55ffd-13f1-4b3e-9be4-09023f044c35.png)

By not filtering the HTML tags in the user's form, the user is free to add these tags to the database.

![image](https://user-images.githubusercontent.com/63194321/133437848-51955829-bc3e-4aeb-aa99-c9420f9baf5d.png)

![image](https://user-images.githubusercontent.com/63194321/133425652-0e0a8289-2ad2-4387-be0a-479d0f0256a9.png)

Now we will write in a script, if this script works, the site has XSS.

![image](https://user-images.githubusercontent.com/63194321/133439235-0a0abd26-a71f-47c8-a57e-78ae6f7c560b.png)

![image](https://user-images.githubusercontent.com/63194321/133439321-76680f9b-2286-4f83-a225-eb0e09a1f757.png)

The `script` is already running so here is XSS

## 2. Exploit 

**B1.** Comment a malicious payload `<script>alert(document.cookie)</script>` on a certain post.

**B2.** After `submit` the article, the malicious payload was saved directly in the databases.

**B3.** Now anyone who enters a post with a malicious `comment` will be affected by this XSS.

![image](https://user-images.githubusercontent.com/63194321/132675854-59905c6c-ed80-4b34-9463-de807318b066.png)


