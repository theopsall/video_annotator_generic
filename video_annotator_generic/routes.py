import os
from flask import render_template, request, redirect, session
from video_annotator_generic import app
from video_annotator_generic import utils
from video_annotator_generic.config import CLASSES



@app.route('/')
@app.route('/home')
def home():
    """
    Home page

    Returns:
        [type]: [description]
    """

    return render_template("index.html", title='Home VAT')


@app.route('/annotate', methods=['GET', 'POST'])
def annotate():

    if "username" in session:
        if (len(utils.get_videos()) > len(utils.annotated(session['username']))):
            diff = utils.get_difference(session['username'])
            video = utils.get_random_video(diff)
            session['video'] = video

            return render_template('annotation.html',
                                   title="Video Annotator Tool",
                                   username=session['username'],
                                   classes=CLASSES,
                                   filename='Videos' + os.sep + session['video'])
        else:
            return render_template('profile.html',
                        title="Annotator's Profile",
                        username=session["username"],
                        num_videos=utils.num_videos(),
                        already_annotated=utils.num_annotated(session["username"]))

    else:
        return render_template("index.html", title='Home VAT')


@app.route('/finish', methods=['GET', 'POST'])
def finish():
    if request.method == 'POST':
        # save annotations
        annotations = (request.form['labels'])
        message = 'Congrats you have successfully Annotated {0}'.format(session["username"])

        utils.add_annotation(session['username'], session['video'], annotations)
        utils.add_video(session['username'], session['video'])

        annotations = []
        session.pop('video', None)


        return render_template('profile.html',
                                title="Annotator's Profile",
                                username=session["username"],
                                num_videos=utils.num_videos(),
                                already_annotated=utils.num_annotated(session["username"]),
                                message = message)
    else:
        message = 'Video {0} failed to be annotated'.format()
        return render_template('profile.html',
                                title="Annotator's Profile",
                                username=session["username"],
                                num_videos=utils.num_videos(),
                                already_annotated=utils.num_annotated(session["username"]),
                                message = message)



@app.route('/profile', methods=['POST', 'GET'])
def profile():
    if 'username' in session:
        return render_template('profile.html',
                                title="Annotator's Profile",
                                username=session["username"],
                                num_videos=utils.num_videos(),
                                already_annotated=utils.num_annotated(session["username"]))
       
    return render_template("index.html", title='Home VAT')


@app.route('/login', methods=['GET', 'POST'])
def login():

    error = None
    if request.method == "POST":
        email = request.form['email']
        if email in utils.get_users():
            session["username"] = email
            print(session)
            return render_template('profile.html',
                                   title="Annotator's Profile",
                                   username=email,
                                   num_videos=utils.num_videos(),
                                   already_annotated=utils.num_annotated(email))
        else:
            error = "User with email {} does not exist. Please check your email or Sign Up".format(email)
            return render_template("login.html", title="Sign in to VAT", error=error)

    return render_template("login.html", title="Sign in to VAT", error=error)


@app.route("/register", methods=["POST", "GET"])
def register():
    error = None
    if request.method == "POST":
        email = request.form['email']
        if email in utils.get_users():
            error = "User with email {} already exists. Please check your email or Login in".format(email)
            return render_template("register.html", title="Sign in to VAT", error=error)
        else:
            session["username"] = email
            utils.add_user(email)
            utils.make_annotation_file(email)
            return render_template('profile.html',
                                   title="Annotator's Profile",
                                   username=email,
                                   num_videos=utils.num_videos(),
                                   already_annotated=utils.num_annotated(email))

    return render_template("register.html", title="Sign Up to VAT", error=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('video',None)
    return render_template("index.html", title="HOME VAT")


@app.errorhandler(404)
def not_found(e):
    """
    Handling non existing routes
    Args:
        e: error of not finding the route

    Returns:

    """

    return render_template("404.html")
