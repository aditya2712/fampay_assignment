# fampay_assignment

### Techstack
- Django
- DRF (Django-rest-framework)
- Celery (Used for periodic tasks)
- Database: Sqlite3

### About the project
- There are 2 models 
  1. Video : Used to store the vidoe data.
  2. Tag : Used to store keyword information about the videos.
- To fetch the videos related to a particular keyword, the admin can create an instance of Tag model using the *Admin Panel*.
- The added tag will be used next time when the videos are being fetched from youtube.
- Fetched videos from youtube will be added in the database, and a unique Id is given to the video, so that there are no duplicate entires.
- There is a *paginated browsable API* to get the vidoes from database based on a particular keyword.

### API Endpoints
- `GET /youtube/videos/?page=1&tag=football`: Returns the videos stored in the database related to the keyword "football".

Sample Response:
```

{
    "count": 50,
    "next": "http://localhost:8000/youtube/videos/?page=2&tag=football",
    "previous": null,
    "results": [
        {
            "id": 52,
            "title": "Dallas Cowboys vs. San Fransisco 49ers | 2022 Divisional Round Game Highlights",
            "published_date": "2023-01-23T02:58:23Z",
            "description": "Check out our other channels: NFL Mundo https://www.youtube.com/mundonfl NFL Brasil ...",
            "video_id": "CwaKooHmJOM",
            "thumbnail_url": "https://i.ytimg.com/vi/CwaKooHmJOM/default.jpg",
            "channel_title": "NFL",
            "tag": 2
        },
        {
            "id": 54,
            "title": "LIVE SHOW: The Latest On Auburn Football Recruiting &amp; The 2023 Recruiting Class | Auburn Live",
            "published_date": "2023-01-23T02:07:19Z",
            "description": "Jeffrey Lee, Cole Pinkston and \"Jhead\" discuss the latest news on the recruiting trail regarding Auburn Football & give their ...",
            "video_id": "9168vAkaWLc",
            "thumbnail_url": "https://i.ytimg.com/vi/9168vAkaWLc/default.jpg",
            "channel_title": "Auburn Tigers on Auburn Live",
            "tag": 2
        }
    ]
}
```

### Added features:
- Admin Panel: For the admin user, there is an Admin Panel, using which they can effectively perform any operation such as View/Update/Delete/Create Tags and Videos


## Instructions to run the project:
1. Clone the repository.
2. Create a new venv: `py -m venv venv`
3. Activate venv: `.\venv\Scripts\activate`
4. Install all the requiremetns using the given requirements.txt file : `pip install -r requirements.txt`
5. Create .env file using the .env.example file
6. Run migrations: `py manage.py migrate`
7. Create superuser: `py manage.py createsuperuser`
8. Run the server: `py manage.py runserver`
9. Server will be accessible on `http://localhost:8000/`. Admin panel will be available on `http://localhost:8000/admin` login with the superuser creds.
10. To run the celery worker, open new terminal and run the following command: `celery -A fampay_assignment worker -l info`
11. The project also requires celery beat for periodic tasks, so open a new terminal and run: `celery -A fampay_assignment beat -l info`
12. Now, youtube vidoes will be fetched every 10 seconds periodically.

Project Screenshots:
Admin Panel: 
![image](https://user-images.githubusercontent.com/61308121/213984983-8c3eb1f8-ee4c-437d-9faa-6c2e9dbc05f0.png)
Browsable list of videos:
![image](https://user-images.githubusercontent.com/61308121/213985065-8bfc05a6-3208-404b-aa9b-737d414ccb34.png)
Browsable API to get paginated videos list:
![image](https://user-images.githubusercontent.com/61308121/213985129-0e7bd29d-0d85-4435-ad35-d2b22e57d635.png)

