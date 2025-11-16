# ...existing code...
import sys
import cv2

def test_camera(index: int = 0) -> int:
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print(f"Камера {index} не открыта")
        return 1

    print(f"Камера {index} открыта. Нажмите 'q' чтобы выйти.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Не удалось получить кадр")
            break
        cv2.imshow("Camera Test - press q to quit", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    return 0

if __name__ == "__main__":
    cam_index = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    sys.exit(test_camera(cam_index))
# ...existing code...