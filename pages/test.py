import cv2
import mediapipe as mp
from mediapipe.tasks import python
import threading 
import streamlit as st
import time

st.set_page_config(page_title="Sign language", page_icon="OK")

class GestureRecognizer:
    def __init__(self):
        self.num_hands = 2
        self.model_path = "abc.task"
        self.GestureRecognizer = mp.tasks.vision.GestureRecognizer
        self.GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
        self.VisionRunningMode = mp.tasks.vision.RunningMode

        self.lock = threading.Lock()
        self.current_gestures = []
        options = self.GestureRecognizerOptions(
            base_options=python.BaseOptions(model_asset_path=self.model_path),
            running_mode=self.VisionRunningMode.LIVE_STREAM,
            num_hands=self.num_hands,
            result_callback=self.__result_callback)
        self.recognizer = self.GestureRecognizer.create_from_options(options)

        self.timestamp = 0 
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=self.num_hands,
            min_detection_confidence=0.65,
            min_tracking_confidence=0.65)

    def main(self):
        st.title("Gesture Recognition with OpenCV And mediapipe")
        video_placeholder = st.empty()
        

        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
            np_array = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=np_array)
                    self.recognizer.recognize_async(mp_image, self.timestamp)
                    self.timestamp += 1  # should be monotonically increasing, because in LIVE_STREAM mode
                    self.put_gestures(frame)
                    # latest_gesture1=self.put_gestures(frame)
                    
                #  self.put_gestures(frame)
            # gesture_container.text(latest_gesture1)
            video_placeholder.image(frame, channels="BGR", use_column_width=True)
            
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                 break

        cap.release()

    # def put_gestures(self, frame):
    #     self.lock.acquire()
    #     gestures = self.current_gestures
    #     self.lock.release()
    #     y_pos = 50
    #     for hand_gesture_name in gestures:
    #         st.text(hand_gesture_name)
    #         y_pos += 50
    def put_gestures(self, frame):
        gesture_container = st.empty()
        self.lock.acquire()
        gestures = self.current_gestures
        self.lock.release()
        # num_displayed_gestures = min(5, len(gestures))

        # Display only the latest gesture
        if gestures:
            latest_gesture = gestures[-1]
            
            with gesture_container.container():
                st.text(latest_gesture)
                time.sleep(0.12)
            gesture_container.empty()
            # st.text(latest_gesture)

        # if gestures:
        #     latest_gesture = gestures[-1]
        #     gesture_container.text(latest_gesture)
       
    def __result_callback(self, result, output_image, timestamp_ms):
        self.lock.acquire()  # solves potential concurrency issues
        self.current_gestures = []
        if result is not None and any(result.gestures):
            st.write("Recognized gestures:")
            for single_hand_gesture_data in result.gestures:
                gesture_name = single_hand_gesture_data[0].category_name
                self.current_gestures.append(gesture_name)
        self.lock.release()

if __name__ == "__main__":
    rec = GestureRecognizer()
    rec.main()
