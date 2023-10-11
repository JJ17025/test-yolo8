from ultralytics import YOLO

model = YOLO('yolov8n.yaml')  # เป็นการสร้างโมเดลใหม่ขึ้นมา
model = YOLO('yolov8n.pt')  # โหลด pretrained model มาเพื่อให้เราไม่ต้องเทรนใหม่ทั้งหมดตั้งแต่เริ่ม

path = 'data.yaml'
results = model.train(data=path, epochs=3)

# ทดสอบโมเดลโดยใช้ validation datasets ที่เตรียมไว้
results = model.val()

# เซฟโมเดลโดยให้โมเดลอยู่ใน ONNX format
success = model.export(format='onnx')
