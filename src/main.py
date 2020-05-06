import json
import mirrors
from PyQt5.QtWidgets import QMainWindow, QApplication, QProgressBar
from PyQt5 import QtCore
import design
import sys
import os
import loadvideo
import re
from multiprocessing import Manager, Pool
'''


          _            _         _           _
         /\ \         /\ \     /_/\         / /\
         \ \ \        \_\ \    \_\ \       / /  \
         /\ \_\       /\__ \   /\_\/      / / /\ \__
        / /\/_/      / /_ \ \  \/_/      / / /\ \___\
       / / /        / / /\ \ \           \ \ \ \/___/
      / / /        / / /  \/_/            \ \ \
     / / /        / / /               _    \ \ \
 ___/ / /__      / / /               /_/\__/ / /
/\__\/_/___\    /_/ /                \ \/___/ /
\/_________/    \_\/                  \_____\/

        _   _                _               _                   _                 _
       /\_\/\_\ _           /\ \            / /\                /\ \              /\ \
      / / / / //\_\        /  \ \          / /  \              /  \ \            /  \ \
     /\ \/ \ \/ / /       / /\ \ \        / / /\ \            / /\ \_\          / /\ \ \
    /  \____\__/ /       / / /\ \_\      / / /\ \ \          / / /\/_/         / / /\ \_\
   / /\/________/       / / /_/ / /     / / /  \ \ \        / / / ______      / /_/_ \/_/
  / / /\/_// / /       / / /__\/ /     / / /___/ /\ \      / / / /\_____\    / /____/\
 / / /    / / /       / / /_____/     / / /_____/ /\ \    / / /  \/____ /   / /\____\/
/ / /    / / /       / / /\ \ \      / /_________/\ \ \  / / /_____/ / /   / / /______
\/_/    / / /       / / /  \ \ \    / / /_       __\ \_\/ / /______\/ /   / / /_______\
        \/_/        \/_/    \_\/    \_\___\     /____/_/\/___________/    \/__________/

           _                  _            _                 _               _       _           _              _
          / /\               /\ \         /\ \             /\ \             / /\    / /\        /\ \           / /\
         / /  \              \ \ \        \_\ \           /  \ \           / / /   / / /       /  \ \         / /  \
        / / /\ \             /\ \_\       /\__ \         / /\ \ \         / /_/   / / /       / /\ \ \       / / /\ \__
       / / /\ \ \           / /\/_/      / /_ \ \       / / /\ \ \       / /\ \__/ / /       / / /\ \_\     / / /\ \___\
      / / /\ \_\ \         / / /        / / /\ \ \     / / /  \ \_\     / /\ \___\/ /       / /_/_ \/_/     \ \ \ \/___/
     / / /\ \ \___\       / / /        / / /  \/_/    / / /    \/_/    / / /\/___/ /       / /____/\         \ \ \
    / / /  \ \ \__/      / / /        / / /          / / /            / / /   / / /       / /\____\/     _    \ \ \
   / / /____\_\ \    ___/ / /__      / / /          / / /________    / / /   / / /       / / /______    /_/\__/ / /
  / / /__________\  /\__\/_/___\    /_/ /          / / /_________\  / / /   / / /       / / /_______\   \ \/___/ /
  \/_____________/  \/_________/    \_\/           \/____________/  \/_/    \/_/        \/__________/    \_____\/
'''
exec_folder = os.path.dirname(__file__)
manager = Manager()
queue = manager.Queue()

#https://a49.agorov.org/tip/tv/2425-fruits-basket-2nd-season.html
class VideoLoader(QtCore.QObject):
    running = False
    newState = QtCore.pyqtSignal(dict)
    def run(self):
        while True:
            print("в потоке")
            download = queue.get()
            if download:
                print(download)
                # sending signal
                self.newState.emit(download)
            QtCore.QThread.sleep(1)


# Main window class
class MainWindow(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.downloadButton.clicked.connect(self._download)
        self.thread = QtCore.QThread()
        self.DownLoadThread = VideoLoader()
        self.DownLoadThread.moveToThread(self.thread)
        self.DownLoadThread.newState.connect(self._downloads_progress)
        self.thread.started.connect(self.DownLoadThread.run)
        self.pbars = []
        self.thread.start()



    def _downloads_progress(self, item):
        print("loads progress")
        done = item.get("done")
        number = item.get("item")
        self.pbars[number].setValue(done)

    def _download(self):
        global queue
        base_link = re.search(r"https:\/\/?.*org", self.linkEdit.text()).group(0)
        video_links = loadvideo.load(self.linkEdit.text(), base_link)
        pool = Pool(3)
        print('links here')
        print(video_links)
        self.pbars = []
        for item in video_links:
            pbar = QProgressBar(self)
            self.scrollareadownloads.addWidget(pbar)
            self.pbars.append(pbar)

        pool.map_async(loadvideo.download_video,[(link,i, queue) for i,link in enumerate(video_links)])
        pool.close()
        print("started pool")
        print("done with this shit")
def load_settings():
    with open(os.path.join(exec_folder, "settings.json"), 'r') as file:
        settings = json.load(file)
    return settings


def main():
    print(exec_folder)
    settings = load_settings()
    find_mirror = settings.get("find_mirror")
    start_mirrors = settings.get("start_mirrors")
    end_mirrors = settings.get("end_mirrors")
    if find_mirror and start_mirrors and end_mirrors:
        mirror = mirrors.look_for_mirror(start_mirrors, end_mirrors)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
