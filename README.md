# video_annotator_generic
Annotate video shots of a video

![APM](https://img.shields.io/apm/l/vim-mode)
[![Generic badge](https://img.shields.io/badge/python->=3-green.svg)](https://shields.io/)

About
----
At the annotations_database.txt we are keeping the annotations in the form of 
user, video, label 
 ## Web App Usage:

 You have to register/login with your email, in order to start the annotation process.
 The app will randomly peek a video that you have not already annotate to begin with.


## Installation
```bash
git clone https://github.com/theopsall/video_annotator_generic.git
cd video_annotator_generic
pip install -r requirements.txt
```

## Running:
```bash
python3 run.py
```

Tree Structure
---
```
├───.users
├───static
│   ├───Annotated
│   └───Videos
```
Under the ./users direcroty you can find the users.txt file which contains the emails of the registered users on the Web app, in order to wrok the login and register mechanism.

Under the static folder you can find the Annotated directory which contains a {email}.txt file for each user with the annotated videos.

Under the static folder you can find the Video directory which contains the dataset.
