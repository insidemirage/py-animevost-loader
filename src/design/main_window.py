# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(679, 438)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color:#444343;\n"
"border:none;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setStyleSheet("background-color:#F9F9F9;\n"
"height:40px;")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.downloadsButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.downloadsButton.setStyleSheet("image: url(:/downloadsBtn/download.png);\n"
"width:30px;\n"
"height:30px;")
        self.downloadsButton.setText("")
        self.downloadsButton.setObjectName("downloadsButton")
        self.horizontalLayout_4.addWidget(self.downloadsButton)
        self.listAnimeButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.listAnimeButton.setStyleSheet("image: url(:/listBtn/list.png);\n"
"width:30px;\n"
"height:30px;")
        self.listAnimeButton.setText("")
        self.listAnimeButton.setObjectName("listAnimeButton")
        self.horizontalLayout_4.addWidget(self.listAnimeButton)
        self.SettingsAnimeButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.SettingsAnimeButton.setStyleSheet("image: url(:/settingsBtn/edit-tools.png);\n"
"width:30px;\n"
"height:30px;")
        self.SettingsAnimeButton.setText("")
        self.SettingsAnimeButton.setObjectName("SettingsAnimeButton")
        self.horizontalLayout_4.addWidget(self.SettingsAnimeButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.linkEdit = QtWidgets.QLineEdit(self.horizontalWidget)
        self.linkEdit.setStyleSheet("background-color:#E7E7E7;\n"
"border-radius:10px;\n"
"height:30px;\n"
"width:294px;\n"
"padding-left:10px;")
        self.linkEdit.setObjectName("linkEdit")
        self.horizontalLayout.addWidget(self.linkEdit)
        self.downloadButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.downloadButton.setStyleSheet("background-color:#5F5F5F;\n"
"\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"color:white;\n"
"width:65px;\n"
"height:30px;\n"
"padding: 4px;")
        self.downloadButton.setObjectName("downloadButton")
        self.horizontalLayout.addWidget(self.downloadButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.horizontalWidget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.DownloadsPage = QtWidgets.QWidget()
        self.DownloadsPage.setObjectName("DownloadsPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.DownloadsPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cancelLoadButton = QtWidgets.QPushButton(self.DownloadsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelLoadButton.sizePolicy().hasHeightForWidth())
        self.cancelLoadButton.setSizePolicy(sizePolicy)
        self.cancelLoadButton.setStyleSheet("background-color:#5F5F5F;\n"
"\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"color:white;\n"
"width:65px;\n"
"height:30px;\n"
"\n"
"padding: 4px;")
        self.cancelLoadButton.setObjectName("cancelLoadButton")
        self.verticalLayout_2.addWidget(self.cancelLoadButton, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.scrollArea = QtWidgets.QScrollArea(self.DownloadsPage)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 661, 302))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollareadownloads = QtWidgets.QVBoxLayout()
        self.scrollareadownloads.setObjectName("scrollareadownloads")
        self.verticalLayout_5.addLayout(self.scrollareadownloads)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.DownloadsPage)
        self.ListPage = QtWidgets.QWidget()
        self.ListPage.setObjectName("ListPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ListPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.SearchEdit = QtWidgets.QLineEdit(self.ListPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchEdit.sizePolicy().hasHeightForWidth())
        self.SearchEdit.setSizePolicy(sizePolicy)
        self.SearchEdit.setStyleSheet("background-color:#E7E7E7;\n"
"border-radius:10px;\n"
"height:30px;\n"
"width:300px;\n"
"padding-left:10px;")
        self.SearchEdit.setObjectName("SearchEdit")
        self.horizontalLayout_5.addWidget(self.SearchEdit)
        self.searchListButton = QtWidgets.QPushButton(self.ListPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchListButton.sizePolicy().hasHeightForWidth())
        self.searchListButton.setSizePolicy(sizePolicy)
        self.searchListButton.setStyleSheet("background-color:#5F5F5F;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"color:white;\n"
"width:65px;\n"
"height:30px;\n"
"padding: 4px;")
        self.searchListButton.setObjectName("searchListButton")
        self.horizontalLayout_5.addWidget(self.searchListButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.ListScrollArea = QtWidgets.QScrollArea(self.ListPage)
        self.ListScrollArea.setWidgetResizable(True)
        self.ListScrollArea.setObjectName("ListScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 661, 316))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollAreaWidget = QtWidgets.QVBoxLayout()
        self.scrollAreaWidget.setObjectName("scrollAreaWidget")
        self.verticalLayout_7.addLayout(self.scrollAreaWidget)
        self.ListScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.ListScrollArea)
        self.stackedWidget.addWidget(self.ListPage)
        self.SettingsPage = QtWidgets.QWidget()
        self.SettingsPage.setObjectName("SettingsPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.SettingsPage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.SettingsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.changeQualityButton = QtWidgets.QPushButton(self.SettingsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.changeQualityButton.sizePolicy().hasHeightForWidth())
        self.changeQualityButton.setSizePolicy(sizePolicy)
        self.changeQualityButton.setStyleSheet("background-color:#5F5F5F;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"color:white;\n"
"width:65px;\n"
"height:20px;\n"
"padding: 4px;")
        self.changeQualityButton.setObjectName("changeQualityButton")
        self.horizontalLayout_9.addWidget(self.changeQualityButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label = QtWidgets.QLabel(self.SettingsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.searchmirrorschbx = QtWidgets.QCheckBox(self.SettingsPage)
        self.searchmirrorschbx.setText("")
        self.searchmirrorschbx.setObjectName("searchmirrorschbx")
        self.horizontalLayout_8.addWidget(self.searchmirrorschbx)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.SettingsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.endSearchingMirror = QtWidgets.QLineEdit(self.SettingsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endSearchingMirror.sizePolicy().hasHeightForWidth())
        self.endSearchingMirror.setSizePolicy(sizePolicy)
        self.endSearchingMirror.setStyleSheet("background-color:#E7E7E7;\n"
"border-radius:10px;\n"
"width:100px;\n"
"height:20px;\n"
"\n"
"text-align:center;")
        self.endSearchingMirror.setAlignment(QtCore.Qt.AlignCenter)
        self.endSearchingMirror.setObjectName("endSearchingMirror")
        self.horizontalLayout_7.addWidget(self.endSearchingMirror)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.SettingsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.startSearchingMirror = QtWidgets.QLineEdit(self.SettingsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startSearchingMirror.sizePolicy().hasHeightForWidth())
        self.startSearchingMirror.setSizePolicy(sizePolicy)
        self.startSearchingMirror.setStyleSheet("background-color:#E7E7E7;\n"
"border-radius:10px;\n"
"width:100px;\n"
"height:20px;\n"
"")
        self.startSearchingMirror.setAlignment(QtCore.Qt.AlignCenter)
        self.startSearchingMirror.setObjectName("startSearchingMirror")
        self.horizontalLayout_6.addWidget(self.startSearchingMirror)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.ButtonSaveSettings = QtWidgets.QPushButton(self.SettingsPage)
        self.ButtonSaveSettings.setStyleSheet("background-color:#5F5F5F;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"color:white;\n"
"width:65px;\n"
"height:20px;\n"
"padding: 4px;")
        self.ButtonSaveSettings.setObjectName("ButtonSaveSettings")
        self.verticalLayout_4.addWidget(self.ButtonSaveSettings)
        self.stackedWidget.addWidget(self.SettingsPage)
        self.AboutPage = QtWidgets.QWidget()
        self.AboutPage.setObjectName("AboutPage")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.AboutPage)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalWidget_5 = QtWidgets.QWidget(self.AboutPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_5.sizePolicy().hasHeightForWidth())
        self.verticalWidget_5.setSizePolicy(sizePolicy)
        self.verticalWidget_5.setMinimumSize(QtCore.QSize(200, 0))
        self.verticalWidget_5.setStyleSheet("")
        self.verticalWidget_5.setObjectName("verticalWidget_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalWidget_5)
        self.verticalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.imageabout = QtWidgets.QLabel(self.verticalWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageabout.sizePolicy().hasHeightForWidth())
        self.imageabout.setSizePolicy(sizePolicy)
        self.imageabout.setMinimumSize(QtCore.QSize(200, 300))
        self.imageabout.setStyleSheet("")
        self.imageabout.setText("")
        self.imageabout.setScaledContents(True)
        self.imageabout.setObjectName("imageabout")
        self.verticalLayout_9.addWidget(self.imageabout)
        self.horizontalLayout_10.addWidget(self.verticalWidget_5)
        self.about_text = QtWidgets.QLabel(self.AboutPage)
        self.about_text.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_text.sizePolicy().hasHeightForWidth())
        self.about_text.setSizePolicy(sizePolicy)
        self.about_text.setStyleSheet("color:white;")
        self.about_text.setText("")
        self.about_text.setWordWrap(True)
        self.about_text.setObjectName("about_text")
        self.horizontalLayout_10.addWidget(self.about_text)
        self.stackedWidget.addWidget(self.AboutPage)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Animevost Load App"))
        self.linkEdit.setPlaceholderText(_translate("MainWindow", "Введите сюда ссылку на страницу animevost..."))
        self.downloadButton.setText(_translate("MainWindow", "Скачать"))
        self.cancelLoadButton.setText(_translate("MainWindow", "Отмена"))
        self.SearchEdit.setPlaceholderText(_translate("MainWindow", "Введите название..."))
        self.searchListButton.setText(_translate("MainWindow", "Search"))
        self.label_4.setText(_translate("MainWindow", "Loading quality:"))
        self.changeQualityButton.setText(_translate("MainWindow", "480"))
        self.label.setText(_translate("MainWindow", "Mirror searching:"))
        self.label_3.setText(_translate("MainWindow", "Mirror searching end:"))
        self.endSearchingMirror.setText(_translate("MainWindow", "90"))
        self.label_2.setText(_translate("MainWindow", "Mirror searching start:"))
        self.startSearchingMirror.setText(_translate("MainWindow", "40"))
        self.ButtonSaveSettings.setText(_translate("MainWindow", "Save"))
        self.imageabout.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))

