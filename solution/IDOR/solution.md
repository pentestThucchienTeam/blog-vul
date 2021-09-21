# Insecure direct object reference


## 1. Detect    


At the `/preview` page. We can see the pending post. When admin approves, the post's status changes to `active` and it is removed in the request list  

![image](https://user-images.githubusercontent.com/22276823/133434553-a5037591-8a14-4c76-a00a-d0d3f94c6789.png)


Let attend to column ID. It's a list of sequence number. We can check by changin


The blog returns not found. Because this post status is `active`. So we can't show it in the `preview` page  


## 2. Exploit  

We know the post ID is sequence number. We can list all the posts have status `active` and our requested post. If the ID not show in that list, it has 2 case. 

1. The post is disabled or deleted  

2. The post is belong to another people and it's pending  

After checking we found some ID `15, 17, 21,..`. Let check  

The post ID `15`  

![image](https://user-images.githubusercontent.com/22276823/133437304-a3f0b872-3b9b-45d8-a1b7-c33775c7749c.png)


The post ID `17` 

![image](https://user-images.githubusercontent.com/22276823/133437458-062d27bd-de58-482c-9005-768f1bb1037a.png)


You can check by logging out current account (I'm logging in `admin` account) and log in another account (`abc1` in my case) 


![image](https://user-images.githubusercontent.com/22276823/133438805-3fefc362-3bf1-4a0f-9e8c-cb196fcb22f0.png)
  
