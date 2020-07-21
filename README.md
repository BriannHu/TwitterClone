# Django Twitter App

 This is a basic Twitter web app that combines Django to handle the backend along with React for the frontend.
 
 Basic Twitter features are implemented including:
 * Posting/viewing tweets
 * Liking/unliking/retweeting tweets
 * User registration/login/logout system
 * Following/unfollowing users

Todo list:
* Improved UI
* Exclusive authentication (specific to McGill)
* DMs feature
* Trending feature

## Running this Project

To run this project, you will need Python 3.5+ installed on your computer. Download instructions can be found on the [official Python site](https://www.python.org/downloads/). It's recommended to also create a virtual environment to avoid installing Python dependencies globally. Create it with:
```
pip install virtualenv
```
Clone or download this repository and open it in your editor of choice. In a terminal, run the following command in the base directory of the project:
```
virtualenv env
```
This will create a new folder env in your base directory, which you can then activate with:
```
source env/bin/activate
```
Install the project dependencies with:
```
pip install -r requirements.txt
```
Now you can run the project locally:
```
python manage.py runserver
```

## Acknowledgements

This is a project inspired by a similar one from CFE (Coding for Entrepreneurs).
* [Link to video tutorial](https://www.youtube.com/watch?v=f1R_bykXHGE)
* [Link to Github repo](https://github.com/codingforentrepreneurs/Tweetme-2)
