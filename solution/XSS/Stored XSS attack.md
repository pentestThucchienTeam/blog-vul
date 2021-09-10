# Stored XSS attack
When commenting on a post with the special `<hr> Hello` caption, we discovered that it's possible to embed HTML tags in a post's comments.

![image](https://user-images.githubusercontent.com/63194321/132675357-de9e730a-6ad0-4345-a3a2-99007fe3d9ca.png)

Therefore, I will inject a malicious payload here `<script>alert(document.cookie)</script>`.Payload has been done.

![image](https://user-images.githubusercontent.com/63194321/132675854-59905c6c-ed80-4b34-9463-de807318b066.png)

The payload is already stored in the databases, so any user accessing the page containing this payload will be attacked.

