# Server-side request forgery

## Detect  

The blog has 2 functions that allow user to create the new post at page `/requestpost`. One of them crawls the post content of the url that user submit on. Like this:  
  
![image](https://user-images.githubusercontent.com/22276823/132515793-b9c66c59-fab3-4219-9ed9-f1bd41a0de1f.png)  
  
Then we can see the content of post after submit
![image](https://user-images.githubusercontent.com/22276823/132802440-653c1b0e-31ea-47db-a448-540ba89a6ad7.png)  
  
  
Now, Submiting the blog's url. We saw the blog return the error but the post had been created. It means the url is crawled but the handle process returns error  
  
![image](https://user-images.githubusercontent.com/22276823/132802119-713b00a7-d979-4a54-9389-552fb8baa6ac.png)  
  
![image](https://user-images.githubusercontent.com/22276823/132802168-010b89c8-466b-4dd2-850c-c8ad1c3611f5.png)  
  
  
Although, The web admin notify the user just allow to submit the url in list. But they don't really validate the user's data. Because this is crawl function, the post is handled after crawled. So we can't see content of url. But this can conduce the blind SSRF, the attacker can find the dangerous requests using `GET` method
(like changepassword) to send request beacause it doesn't need to know the content of response. The another attack vector is port scanning.   


## Exploit  

__1. Send request with `localhost` and port `80`__  
   
![image](https://user-images.githubusercontent.com/22276823/133198124-ceb13408-8128-4e93-9905-5a2016755f0e.png)   
   
![image](https://user-images.githubusercontent.com/22276823/133197997-5a45148f-2a39-461f-87fe-ab8471feaedc.png)  


__2. Send request with `localhost` and port `22`__  

![image](https://user-images.githubusercontent.com/22276823/133198154-d65d5670-6132-4e18-a82e-3aa804eaf3c0.png)

![image](https://user-images.githubusercontent.com/22276823/133198179-d6b94f7e-2a56-4124-bc21-2a102b0d8fc5.png)  

looking at the error. If the server open port (`22` as above), The blog returns the banner of service. If port closed, it returns `connection refuse`  
