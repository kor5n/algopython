#создай тут фоторедактор Easy Editor!
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QFileDialog, QLabel, QListWidget, QHBoxLayout, QVBoxLayout, QApplication, QWidget
from PIL import Image, ImageFilter
workdir = ""
app = QApplictaion([])
window = QWidget()
folder = QPushButton("Папка")
choose_el = QListWidget()
lb_image = QLabel("image")
black_white = QPushButton("Ч/Б")
left = QPushButton("Лево")
right = QPushButton("Право")
mirror = QPushButton("Зеркало")
sharpness = QPushButton("Резкость")
main_lay = QHBoxLayout()
fold_lay = QVBoxLayout()
image_lay = QVBoxLayout()
buttons = QHBoxLayout()

fold_lay.addWidget(folder, alignment=AlginLeft)
fold_lay.addWidget(choose_el, alignment=AlginLeft)

image_lay.addWidget(lb_image)

buttons.addWidget(left)
buttons.addWidget(right)
buttons.addWidget(mirror)
buttons.addWidget(sharpness)
buttons.addWidget(black_white)
class ImageProcessor():
    def __init__(self):
        self.image = None
        self.directory = None
        self.filename = None
        self.save_directory = "Modified/"
    def loadImage(self, filename, directory):
        self.filename = filename
        self.directory = directory
        file_path = os.path.join(workdir, filename)
        self.image = Image.open(filename)
        def showImage(self, path):
            lb_image.hide
            pixmapimage = QPixmap(path)
            w, h = lb_image.width(), lb_image.height()
            pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRation)
            lb_image.setPixmap(pixmapimage)
            lb_image.show()
    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(workdir, self.save_directory, self.filename)
        self.showImage()
    def saveImage(self):
        path = os.path.join(workdir, self.save_directory)
        if not(os.pathexists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
def showChoosenImage():
    if spisok.currentRow() >= 0:
        filename = spisok.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workdir.directory, workimage.filename)  
        workimage.showImage(image_path)
def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(extension):
               result.append(filename)
    return(result)

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.ExistingDirectory()
def showFilenameList():
    extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    chooseWorkdir()
    files = filter(os.listdir(workdir), extensions)
    spisok.clear()
    for filename in files:
        spisok.addItem(filename)
folder.clicked.connect(chooseWorkdir)
workimage = ImageProcessor()
spisok.currentRowChanged.connect(showChoosenImage)
black_white.clicked.connect(do_bw)
folder.clicked.connect(saveImage)
lb_image.addLayout(buttons)
main_lay.addLayout(fold_lay)
main_lay.addLayout(lb_image)
window.setLayout(main_lay)
window.show()
app.exec_()