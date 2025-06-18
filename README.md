# ✋🧠 Sign Language Detector using MediaPipe and OpenCV

This project uses **MediaPipe Hands** and **OpenCV** to detect fingers shown on **both hands** via webcam and map them to **static sign language meanings** based on combinations of left and right hand finger counts.

---

## 📌 Features

- 🤚 Detects both left and right hands using MediaPipe
- 📈 Counts number of fingers held up per hand
- 🧩 Combines left and right hand finger counts to support **6×6 = 36 unique sign mappings**
- 🔤 Maps total or specific finger patterns to meaningful sign labels
- 🎯 Real-time video processing with visual overlays (fingers, sign labels, and landmarks)
- 🧠 Easily extendable for gesture classification, dataset generation, or TTS integration

---

## 🔧 Setup Instructions

1. **Clone the repo or copy the code**
   ```bash
   git clone https://github.com/yourusername/sign-language-detector.git
   cd sign-language-detector
Install dependencies

bash
Copy
Edit
pip install opencv-python mediapipe
Run the script

bash
Copy
Edit
python sign_language_detector.py
🎓 Sign Mapping Logic
The detector combines left-hand finger count (0–5) with right-hand finger count (0–5) to support 36 possible combinations like so:

Left \ Right	0	1	2	3	4	5
0	S0	S1	S2	S3	S4	S5
1	S6	S7	S8	S9	S10	S11
2	S12	S13	S14	S15	S16	S17
3	S18	S19	S20	S21	S22	S23
4	S24	S25	S26	S27	S28	S29
5	S30	S31	S32	S33	S34	S35

Where S0 to S35 can be assigned to custom sign language meanings such as:

S0 = "Hello"

S1 = "I love you"

S2 = "No"

...

S35 = "Perfect"

🔄 You can easily customize the labels in the sign_labels dictionary or extend it to use a tuple-based mapping like sign_labels[(left, right)].

🧠 Example Signs (Default Mapping by Total Fingers Up)
Total Fingers	Label
0	Hello
1	I love you
2	No
3	Okay
4	Please
5	Yes
6	Great
7	Peace
8	Awesome
9	Thank You
10	Perfect

ℹ️ Total = Left + Right hand fingers

📌 How It Works
Uses mediapipe.solutions.hands to detect 21 landmarks per hand

Identifies which fingers are raised based on landmark position

Uses handedness (Right/Left) to correctly determine thumb state

Maps finger count to sign labels

Draws landmarks and displays real-time sign interpretation

🚀 Extensions and Ideas
📹 Save gestures as images for dataset creation

🧠 Add gesture recognition models using TensorFlow/Keras

🔊 Integrate with Text-to-Speech (pyttsx3 or gTTS)

🌐 Convert to a web app using Streamlit or Flask

🔤 Support dynamic signs (e.g., waving for "Hello")

📸 Demo

🧑‍💻 Author
Made with ❤️ by Your Name
Feel free to use, modify, and contribute!