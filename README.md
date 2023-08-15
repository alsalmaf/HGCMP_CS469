# HGCMP(Hand Gesture Controlled Music PLayer)
Welcome to the Hand Gesture Recognition for Music Player Control GitHub repository!  

The project's primary goal is to develop a real-time hand gesture recognition system tailored for music player control, offering users an intuitive and interactive means to manage music playback. This system will enable users to effortlessly play/pause tracks, adjust volume levels, and navigate through SoundCloud playlists using hand gestures. By integrating seamlessly with SoundCloud and allowing users to provide their SoundCloud playlist link, the project ensures a continuous stream of music from their preferred source. By eliminating the need for physical buttons or traditional inputs, the project aims to enhance user engagement and redefine the way individuals interact with music players, providing a novel and convenient experience.  
  
<sub><sup>*this project is Windows OS specific.</sup></sub>

## What Is Hand Gesture Recognition?
Hand Gesture Recognition is an exciting field of computer vision that enables machines to understand and interpret human hand movements. In this project, this technology has been harnessed to create an intuitive way to interact with your music player. By recognizing specific hand gestures, you can effortlessly control your music without touching a single button.


## Features and Functionality:

The product will offer the following features and functionality for controlling the music player using hand gestures:

### Play/Pause Track:
Users can make a "shaka" sign with their hand to play or pause the currently playing track. The "shaka" gesture is formed by joining the thumb and index finger to create a circle, while the remaining fingers are extended. . When the user makes this gesture, it will serve as the trigger to toggle between play and pause states.

### Volume Control:
Users can adjust the volume level using hand gestures with zero to five fingers. Each finger represents a specific volume level, ranging from 0 to 100%. For example:

- Zero fingers (closed fist) will mute the volume.
- Two fingers will set the volume to 40%
- Five fingers (open hand) will set the volume to 100%.

<img src="https://github.com/alsalmaf/HGCMP_CS469/blob/main/instructionSetDiagram.png" width="400">

### Playlist Navigation:
Users can use a thumbs gesture to navigate through the playlist. A thumbs-down gesture to the right will move to the next track, while a thumbs-up gesture to the left will go back to the previous track.

# How to Use

1. **Clone the Repository:** Start by cloning this repository to your local machine.
```
    git clone https://github.com/alsalmaf/HGCMP.git
    cd HGCMP
```

3. **Set Up Dependencies:** Install the required dependencies using the provided instructions.
       
   *The current latest version mediapipe 0.9.0.1 (a machine learning framework neccary for this project) currently provides wheels for Windows for Python 3.7-3.10 so you may need to downgrade your Python version.
```
    setup.bat
```

5. **Run the Program:** Execute the program, and your webcam will become your music control center.
```
    python run.py
```
