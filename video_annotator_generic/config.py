import os

PATH = os.getcwd()
VIDEOS = os.path.join(PATH, 'video_annotator_generic', 'static', 'Videos')
ANNOTATED = os.path.join(PATH, 'video_annotator_generic', 'static', 'Annotated')
USERS = os.path.join(PATH, 'video_annotator_generic', '.users', 'users.txt')
DATABASE = os.path.join(PATH, 'annotations_database.txt')

CLASSES = {
    "Static": "A static camera is locked down on a tripod or pedestal and remains still. It is commonly used in dialogues.",
    "Vertical_movement": "Vertical movement of the camera lens while the camera remains locked on a tripod. It is like tilting your head up/down",
    "Tilt": "Moving the entire camera up or down without moving its lens. Tilting up is like moving up your entire body from a sitting position.",
    "Panoramic": "Lateral movement of the camera lens while the camera remains locked down on its tripod or pedestal. It is like moving your head from one side to another.",
    "Panoramic_lateral": "The camera follows the action moving parallel to characters (crabbing)",
    "Panoramic_360": "A semicircular movement of the camera.",
    "Travelling_in": "Moving the camera towards the subject without changing the focal length. The camera moves in a steady and smooth manner and it is usually mounted on a cart named dolly.",
    "Travelling_out": "Moving the camera away from the subject without changing the focal length. The camera moves in a steady and smooth manner and it is usually mounted on a cart named dolly.",
    "Zoom_in": "Zoom in requires adjusting the focal length of the lens to make the subject appear closer in the frame. It gives the illusion of moving the camera further.",
    "Zoom_out": "Zoom in requires adjusting the focal length of the lens to make the subject appear further away in the frame. It gives the illusion of moving the camera closer.",
    "Vertigo": "The camera moves backward or forward (travelling) while simultaneously the focal length changes in the opposite direction",
    "Aerial": "The camera is flown above action",
    "Handled": "The camera moves throughout the filming set while the camera operator physically holds it. These camera shots are shaky and create a hectic feeling.",
    "Car_front_windshield": "Front windshield shot",
    "Car_side_mirror": "Side mirror shot",
    "N/A": "The available labels do not describe the shot adequately."
}

if __name__ == "__main__":
    for i in CLASSES:
        print(i)