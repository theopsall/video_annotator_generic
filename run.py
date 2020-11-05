from video_annotator_generic import app
from video_annotator_generic.utils import create_directories

if __name__ == "__main__":
    create_directories()
    app.run(host="0.0.0.0", port=9001)