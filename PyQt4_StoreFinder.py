# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQt4_StoreFinder.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(821, 322)
        self.itemList = QtGui.QListWidget(Dialog)
        self.itemList.setGeometry(QtCore.QRect(10, 10, 231, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.itemList.setFont(font)
        self.itemList.setObjectName(_fromUtf8("itemList"))
        self.splitter = QtGui.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(10, 260, 801, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.line = QtGui.QFrame(self.splitter)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.store_image = QtGui.QLabel(Dialog)
        self.store_image.setGeometry(QtCore.QRect(250, 10, 231, 251))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.store_image.sizePolicy().hasHeightForWidth())
        self.store_image.setSizePolicy(sizePolicy)
        self.store_image.setText(_fromUtf8(""))
        self.store_image.setScaledContents(True)
        self.store_image.setObjectName(_fromUtf8("store_image"))
        self.name_label = QtGui.QLabel(Dialog)
        self.name_label.setGeometry(QtCore.QRect(490, 10, 291, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("맑은 고딕"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(490, 30, 321, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.category_label = QtGui.QLabel(Dialog)
        self.category_label.setGeometry(QtCore.QRect(490, 45, 311, 16))
        self.category_label.setText(_fromUtf8(""))
        self.category_label.setObjectName(_fromUtf8("category_label"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(490, 70, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.introduction_label = QtGui.QLabel(Dialog)
        self.introduction_label.setGeometry(QtCore.QRect(540, 70, 261, 161))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.introduction_label.setFont(font)
        self.introduction_label.setText(_fromUtf8(""))
        self.introduction_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.introduction_label.setWordWrap(True)
        self.introduction_label.setObjectName(_fromUtf8("introduction_label"))
        self.address_label = QtGui.QLabel(Dialog)
        self.address_label.setGeometry(QtCore.QRect(490, 230, 311, 31))
        self.address_label.setText(_fromUtf8(""))
        self.address_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.address_label.setWordWrap(True)
        self.address_label.setObjectName(_fromUtf8("address_label"))
        self.korean_button = QtGui.QPushButton(Dialog)
        self.korean_button.setGeometry(QtCore.QRect(90, 280, 75, 31))
        self.korean_button.setObjectName(_fromUtf8("korean_button"))
        self.cafe_button = QtGui.QPushButton(Dialog)
        self.cafe_button.setGeometry(QtCore.QRect(170, 280, 75, 31))
        self.cafe_button.setObjectName(_fromUtf8("cafe_button"))
        self.pub_button = QtGui.QPushButton(Dialog)
        self.pub_button.setGeometry(QtCore.QRect(250, 280, 75, 31))
        self.pub_button.setObjectName(_fromUtf8("pub_button"))
        self.etc_button = QtGui.QPushButton(Dialog)
        self.etc_button.setGeometry(QtCore.QRect(330, 280, 75, 31))
        self.etc_button.setObjectName(_fromUtf8("etc_button"))
        self.random_button = QtGui.QPushButton(Dialog)
        self.random_button.setGeometry(QtCore.QRect(740, 280, 75, 31))
        self.random_button.setObjectName(_fromUtf8("random_button"))
        self.total_button = QtGui.QPushButton(Dialog)
        self.total_button.setGeometry(QtCore.QRect(10, 280, 75, 31))
        self.total_button.setObjectName(_fromUtf8("total_button"))
        self.splitter.raise_()
        self.itemList.raise_()
        self.store_image.raise_()
        self.name_label.raise_()
        self.line_2.raise_()
        self.category_label.raise_()
        self.label_3.raise_()
        self.introduction_label.raise_()
        self.address_label.raise_()
        self.korean_button.raise_()
        self.cafe_button.raise_()
        self.pub_button.raise_()
        self.etc_button.raise_()
        self.random_button.raise_()
        self.total_button.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "중대 맛집 탐색기", None))
        self.name_label.setText(_translate("Dialog", "리스트에서 맛집을 선택해주세요!", None))
        self.label_3.setText(_translate("Dialog", "소개 :", None))
        self.korean_button.setText(_translate("Dialog", "한식", None))
        self.cafe_button.setText(_translate("Dialog", "카페", None))
        self.pub_button.setText(_translate("Dialog", "술집", None))
        self.etc_button.setText(_translate("Dialog", "기타 음식", None))
        self.random_button.setText(_translate("Dialog", "랜덤 선택", None))
        self.total_button.setText(_translate("Dialog", "전체", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

