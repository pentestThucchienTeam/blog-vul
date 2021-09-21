# Dom-Base XSS attack

## 1. Detect 
In the Search page, if you don't select anything, the `tagID` field will be left blank on the URL.

![image](https://user-images.githubusercontent.com/63194321/133432102-740893fd-7755-41ce-8f49-feae26fc6060.png)

Now we enter anything as the value of tagID on the URL, it will also be written into the HTML of the web page.

![image](https://user-images.githubusercontent.com/63194321/133432522-2ea5dcac-73b1-4e92-8faf-bf51e135bc59.png)

![image](https://user-images.githubusercontent.com/63194321/133432578-9bc38616-fe4d-4dd4-8042-c29d80acd4ec.png)

This occurs because the value of the tagID parameter is written directly to the Document Object Model without going through the processor. So here it is easy to add malicious objects.

![image](https://user-images.githubusercontent.com/63194321/133430466-e1acaee1-8f2d-4d59-8373-d55c8e032333.png)

## 2. Exploid
**B1.** We will send the URL containing a malicious code to the victim.

![image](https://user-images.githubusercontent.com/63194321/133433722-81efea99-da71-4aa0-8642-edb046bbca63.png)

**B2.** After the victim clicks on the link, the browser will browse to `https://blog-vul.herokuapp.com` and start building the DOM of the page based on the static HTML. After building the DOM, the browser will execute the code contained in the DOM with the malicious payload.

![image](https://user-images.githubusercontent.com/63194321/132684271-2c9e0555-8718-401f-902e-61fa38896af5.png)


