import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from moviepy.editor import *

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("vid2aud converter (v1.1)")

        FORMATS = ['.mp3', '.wav']

        self.selectFileBtn = QPushButton(self)
        self.selectFileBtn.resize(500, 50)
        self.selectFileBtn.setText("SELECT FILE")
        self.selectFileBtn.move(50, 10)
        self.selectFileBtn.clicked.connect(lambda:self.selectFile())

        self.fileLabel = QLabel(self)
        self.fileLabel.setText("Filename:")
        self.fileLabel.move(50, 70)

        self.formatLabel = QLabel(self)
        self.formatLabel.setText("Format:")
        self.formatLabel.move(370, 70)

        self.fileName = QLineEdit(self)
        self.fileName.resize(300, 30)
        self.fileName.move(50, 100)

        self.formats = QComboBox(self)
        self.formats.addItems(FORMATS)
        self.formats.resize(180, 30)
        self.formats.move(370, 100)

        self.convertBtn = QPushButton(self)
        self.convertBtn.setText("CONVERT")
        self.convertBtn.resize(500, 50)
        self.convertBtn.move(50, 140)
        self.convertBtn.clicked.connect(lambda:self.convert())

        self.clearBtn = QPushButton(self)
        self.clearBtn.setText("CLEAR")
        self.clearBtn.resize(500, 50)
        self.clearBtn.move(50, 190)
        self.clearBtn.clicked.connect(lambda:self.clear())

        self.status = QTextEdit(self)
        self.status.setReadOnly(True)
        self.status.resize(500, 120)
        self.status.move(50, 245)
        
        self.vidFile = ""

    def selectFile(self):
        vidFile = QFileDialog.getOpenFileName(self, 'Select Video', 'c:\\', "Video files (*.mp4 *.m4a)")
        self.vidFile = vidFile

        self.status.setText('Video selected: ' + vidFile[0])

    def convert(self):
        fileName = self.fileName.text()
        file_format = self.formats.currentText()
        save_directory = QFileDialog.getExistingDirectory(self, 'Select Destination')

        video = VideoFileClip(self.vidFile[0])
        audioClip = video.audio
        audioClip.write_audiofile(save_directory + '/' + fileName + file_format)

        video.close()
        audioClip.close()

        self.status.setText("Video converted to: " + save_directory + '/' + fileName + file_format)
        self.fileName.clear()
    
    def clear(self):
        self.fileName.clear()
        self.vidFile = ""
        self.status.clear()

def main():
    app = QApplication(sys.argv)
    ex = Window()
    ex.setFixedSize(600, 400)
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()