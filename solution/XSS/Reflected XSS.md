# Reflected XSS

Go into the application's search bar to find anything for example `<br>JWT`. Then open the source code of the application and we will see that the application writes and executes what we put in.

![image](https://user-images.githubusercontent.com/63194321/132527139-3976e4f6-12a4-49eb-81e9-3cb8c737b1e4.png)

So if we enter a code like: `<script>alert(document.cookie)</script>`
The application will be hacked and return the user's cookie

![image](https://user-images.githubusercontent.com/63194321/132527583-e1754a6e-2b56-4a1e-a696-e99d4c367a93.png)
