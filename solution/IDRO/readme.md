# Insercure Direct Object Reference

## Detect

__Preview__ function allow you preview your request posts which are pending. Observe the URL, you can be realized that path of posts is its id.

  
![image](https://user-images.githubusercontent.com/22276823/132520737-fd6e1ff4-fa08-4b16-a805-cf84641aabcf.png)  
  
My post has id = 16 and the url = `prview/16`

![image](https://user-images.githubusercontent.com/22276823/132520877-54336061-6882-4613-bbf0-89babaa8cb76.png)  

Try changing the id by other id which isn't in your list of requestposts. For example: 15  
  
![image](https://user-images.githubusercontent.com/22276823/132521004-f2747701-52a0-4366-bfe0-314b04c7c40b.png)  

The result, it displayed a post of a other user with `id = 15`.

IDOR vulnerability allow you can see and modify arbitrary post of other users from active to pending.



