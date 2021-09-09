# Dom-Base XSS attack
In the search bar i see a `select` box that selects the `tagID` index and when nothing is selected the tagID will be blank this is a perfect place to insert payloads.

![image](https://user-images.githubusercontent.com/63194321/132681760-8801a214-2ea3-405f-8a3e-298c3b7327ff.png)

I would insert in the payload `<option><script>alert(document.cookie)</script></option>`.

![image](https://user-images.githubusercontent.com/63194321/132683773-e0ae4b0d-0bc6-4d3f-be0b-f457d2792000.png)

After the victim clicks on the URL, the server will execute the script and temporarily save it in the DOM of the web page.

![image](https://user-images.githubusercontent.com/63194321/132684175-7d888150-09e2-4237-b45f-1eaea29171d9.png)

The browser then renders the results page and executes the attacker's script

![image](https://user-images.githubusercontent.com/63194321/132684271-2c9e0555-8718-401f-902e-61fa38896af5.png)


