from ultralytics import YOLO

model = YOLO("yolo26n.pt")  # carrega um modelo de deteção YOLO26n pré-treinado
results = model("https://ultralytics.com/images/bus.jpg", save=True)  # faz a previsão e guarda a imagem anotada