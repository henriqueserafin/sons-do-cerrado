import cv2
#importando media pipe
import mediapipe as mp


mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

with mp_face_mesh.FaceMesh(min_detection_confidence=0.5,min_tracking_confidence=0.5) as facemesh:
#capturar camera
   cap=cv2.VideoCapture(1)

while cap.isOpened():
     sucesso,frame = cap.read()
     if not sucesso:
        print('Ignorando o frame vazio da camêra')
        continue
     frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
     #processar o frame (openCv - MediaPipe)
     saida_facemesh=facemesh.process(frame)
     #transformando rgb para bgr
     frame=cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2BGR)

     for face_landmarks in saida_facemesh.multi_face_landmarks:
         pass
     mp_drawing.draw_landmarks(frame,face_landmarks,mp_face_mesh.FACEMESH_CONTOURS)
     cv2.imshow('Camera',frame)
     if cv2.waitKey(10) & 0xFF == ord('c'):
        break
cap.release()
cv2.destroyAllWindows()
