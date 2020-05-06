import json
import mirrors
from PyQt5.QtWidgets import QMainWindow, QApplication, QProgressBar, QPushButton, QSpacerItem
from PyQt5 import QtCore, QtWidgets, QtGui
import design
import sys
import os
import loadvideo
import re
from urllib import request
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
anime_list = []


class VideoLoader(QtCore.QObject):
    # This is thread for loading videos
    running = False
    newState = QtCore.pyqtSignal(dict)
    def run(self):
        while True:
            # When process put progress in queue we update info
            download = queue.get()
            if download:
                # sending signal
                self.newState.emit(download)
            QtCore.QThread.sleep(5)


# Main window class
class MainWindow(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.downloadButton.clicked.connect(self._download)
        self.thread = QtCore.QThread(parent=self)
        self.DownLoadThread = VideoLoader()
        self.DownLoadThread.moveToThread(self.thread)
        self.DownLoadThread.newState.connect(self._downloads_progress)
        self.thread.started.connect(self.DownLoadThread.run)
        self.listAnimeButton.clicked.connect(self._list_anime_view)
        self.searchListButton.clicked.connect(self._find_anime)
        self.pbars = []  # progress bars on downloads screen
        self.search_res = [] # result buttons on list screen
        self.spacer_res = None
        self.downloadAbout = None
        self.thread.start()


    def _find_anime(self):
        text = self.SearchEdit.text()
        text = re.sub(r"^\s+|\n|\r|\s+$", "", text)  # Removes not significant symbols
        if(len(text) > 2):
            # Clear scroll area
            for i in range(len(self.search_res)):
                self.scrollAreaWidget.removeWidget(self.search_res[i])
            self.scrollAreaWidget.removeItem(self.spacer_res)
            self.spacer_res = None
            self.search_res = []
            search_results = list(filter(lambda x: text.lower() in x["name"].lower(), anime_list))
            # Display results
            for res in search_results:
                btn = QPushButton(res["name"])
                btn.setStyleSheet("""
                    background-color:#848484;
                    height:30px;
                    color:black;
                    text-align:left;
                    padding-left:10px;
                """)
                btn.setMaximumHeight(30)
                btn.clicked.connect(lambda: self._about_screen(res["text"],
                                                               res["image"],
                                                               res["link"],
                                                               res["name"],
                                                               res["author"],
                                                               res["date"]))
                self.scrollAreaWidget.addWidget(btn)
                self.search_res.append(btn)
            # Space in the end of the
            self.spacer_res = QtWidgets.QSpacerItem(10, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            self.scrollAreaWidget.addItem(self.spacer_res)

    def _about_screen(self, text, image, link, name,author, date):
        self.stackedWidget.setCurrentIndex(3)
        data = request.urlopen(image).read()
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(data)
        self.imageabout.setPixmap(pixmap)
        result_text = "Автор: {}\nДата: {}\n{}".format(author, date,text)
        self.about_text.setText(result_text)
        # Create button download
        if self.downloadAbout:
            self.verticalLayout_9.removeWidget(self.downloadAbout)
            self.downloadAbout.destroy()
        self.downloadAbout = QtWidgets.QPushButton(self.verticalWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadAbout.sizePolicy().hasHeightForWidth())
        self.downloadAbout.setSizePolicy(sizePolicy)
        self.downloadAbout.setStyleSheet("background-color:#5F5F5F;\n"
                                         "\n"
                                         "border-width: 2px;\n"
                                         "border-radius: 10px;\n"
                                         "color:white;\n"
                                         "width:65px;\n"
                                         "height:30px;\n"
                                         "padding: 4px;\n"
                                         "")
        self.downloadAbout.setObjectName("downloadAbout")
        self.downloadAbout.setText("Download")
        self.verticalLayout_9.addWidget(self.downloadAbout, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.downloadAbout.clicked.connect(lambda: self._download(link_page=link))

    def _list_anime_view(self):
        self.stackedWidget.setCurrentIndex(1)

    def _downloads_progress(self, item):
        done = item.get("done")
        number = item.get("item")
        self.pbars[number].setValue(done)

    def _download(self, link_page=None):
        global queue
        # Loading videos using working mirror
        # If was used other way to present link
        print('here')
        self.stackedWidget.setCurrentIndex(0)
        if link_page:
            base_link = re.search(r"https:\/\/?.*org", link_page).group(0)
        else:
            base_link = re.search(r"https:\/\/?.*org", self.linkEdit.text()).group(0)
            link_page = self.linkEdit.text()
        video_links = loadvideo.load(link_page, base_link)
        pool = Pool(3)
        self.pbars = []
        for item in video_links:
            pbar = QProgressBar(self)
            self.scrollareadownloads.addWidget(pbar)
            self.pbars.append(pbar)
        pool.map_async(loadvideo.download_video,[(link,i, queue) for i,link in enumerate(video_links)])
        pool.close()

def load_settings():
    with open(os.path.join(exec_folder, "settings.json"), 'r') as file:
        settings = json.load(file)
    return settings


def main():
    global anime_list
    print(exec_folder)
    settings = load_settings()
    find_mirror = settings.get("find_mirror")
    start_mirrors = settings.get("start_mirrors")
    end_mirrors = settings.get("end_mirrors")
    if find_mirror and start_mirrors and end_mirrors:
        mirror = mirrors.look_for_mirror(start_mirrors, end_mirrors)
    if os.path.isfile(os.path.join(exec_folder, "anime_base.json")):
        with open(os.path.join(exec_folder, "anime_base.json")) as file:
            anime_list = json.load(file)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
