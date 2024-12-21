# Django project to generate Resumes

## This app is quite useful when candidates don't have resumes and want quickly to built a one.

- In this app we just need to enter our basic details and submit it.

- After that instantly our resume in pdf form will be generated.

### Clone the repositary

```

git clone https://github.com/abhishek-sanwal/Social_Networking_rest_apis.git

```

### Run docker command which will run this app in a container

```
docker-compose up

```

Now app is hosted at local host 8000 port.

### Our home page ( http://127.0.0.1:8000/ ) will be like this

- ![Home page 1](/docs/images/Form_Resume_1.png)
- ![Home page 2](/docs//images//Form_Resume_2.png)
- ![Home page 3](/docs/images/Form_Resume_3.png)

After we click on submit button data will be stored in backend db.

## We can go to http://127.0.0.1:8000/list/ to list all resumes and download them

![Image to list resume](/docs/images/List_resumes.png)

After clicking on download option resume will be downloaded instatntly.

### Run this command to close container

```
docker-compose down
```

<br/>
