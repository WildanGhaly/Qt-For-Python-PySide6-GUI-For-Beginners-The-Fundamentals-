# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(720, 405)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(720, 405))
        Form.setMaximumSize(QSize(720, 405))
        self.quote_label = QLabel(Form)
        self.quote_label.setObjectName(u"quote_label")
        self.quote_label.setGeometry(QRect(0, 0, 720, 405))
        self.quote_label.setMinimumSize(QSize(720, 405))
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(20)
        self.quote_label.setFont(font)
        self.quote_label.setStyleSheet(u"background-image: url(:/newPrefix/images/quotes.jpg)")
        self.quote_label.setTextFormat(Qt.MarkdownText)
        self.quote_label.setPixmap(QPixmap(u":/newPrefix/images/quotes.jpg"))
        self.quote_label.setScaledContents(True)
        self.quote_label.setAlignment(Qt.AlignCenter)
        self.quote_label.setMargin(-1)
        self.quotes_output = QLabel(Form)
        self.quotes_output.setObjectName(u"quotes_output")
        self.quotes_output.setGeometry(QRect(110, 249, 501, 81))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.quotes_output.sizePolicy().hasHeightForWidth())
        self.quotes_output.setSizePolicy(sizePolicy1)
        self.quotes_output.setMaximumSize(QSize(16777215, 16777215))
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.quote_label.setText("")
        self.quotes_output.setText(QCoreApplication.translate("Form", u"Quotes Here", None))
    # retranslateUi

