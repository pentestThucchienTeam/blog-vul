# Reflected XSS

Observe the search page, the website allows users to search for articles through the title, the system will pass the search parameter through the GET method on the URL. If no results are found, the site will return the following:

![image](https://user-images.githubusercontent.com/63194321/133408527-b759068d-1b96-4176-b997-df7569f95754.png)

Notice that the site responds completely to what the user has just typed. So we will enter a piece of code to see if the code runs. If the code runs, the site is already vulnerable to XSS.

![image](https://user-images.githubusercontent.com/63194321/133415780-267ba1d5-78e2-42fd-818a-456f92c5ae2f.png)

The code we entered is already running, so this site has been XSS.

### Exploit

**B1.** Now we enter a malicious payload `<script>alert(document.cookie)</script>` and the application will respond to the payload and execute it.

![image](https://user-images.githubusercontent.com/63194321/133412106-bd901eb4-f0d4-4206-97ca-0cf22557910e.png)

**B2.** Now we will copy and send this URL to others.

![image](https://user-images.githubusercontent.com/63194321/133416274-1317cd76-557c-4037-8876-0d2224adecad.png)

If the user accesses the link, the code will be executed
