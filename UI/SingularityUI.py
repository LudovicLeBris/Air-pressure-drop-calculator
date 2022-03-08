# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SingularityUI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_Singularities(object):
    def setupUi(self, Singularities):
        if not Singularities.objectName():
            Singularities.setObjectName(u"Singularities")
        Singularities.resize(420, 560)
        Singularities.setMinimumSize(QSize(420, 560))
        font = QFont()
        font.setPointSize(11)
        Singularities.setFont(font)
        Singularities.setLocale(QLocale(QLocale.English, QLocale.Europe))
        self.gridLayout_3 = QGridLayout(Singularities)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_title = QGridLayout()
        self.gridLayout_title.setObjectName(u"gridLayout_title")
        self.la_tilte = QLabel(Singularities)
        self.la_tilte.setObjectName(u"la_tilte")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.la_tilte.sizePolicy().hasHeightForWidth())
        self.la_tilte.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.la_tilte.setFont(font1)
        self.la_tilte.setAlignment(Qt.AlignCenter)

        self.gridLayout_title.addWidget(self.la_tilte, 0, 0, 1, 2)

        self.la_duct_shape = QLabel(Singularities)
        self.la_duct_shape.setObjectName(u"la_duct_shape")
        self.la_duct_shape.setMinimumSize(QSize(244, 0))
        self.la_duct_shape.setFont(font)
        self.la_duct_shape.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.la_duct_shape.setMargin(0)

        self.gridLayout_title.addWidget(self.la_duct_shape, 1, 0, 1, 1)

        self.le_duct_shape = QLineEdit(Singularities)
        self.le_duct_shape.setObjectName(u"le_duct_shape")
        self.le_duct_shape.setEnabled(False)
        self.le_duct_shape.setMinimumSize(QSize(100, 0))
        self.le_duct_shape.setMaximumSize(QSize(16777215, 16777215))
        self.le_duct_shape.setFrame(False)
        self.le_duct_shape.setReadOnly(True)

        self.gridLayout_title.addWidget(self.le_duct_shape, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_title, 0, 0, 1, 1)

        self.gridLayout_sing = QGridLayout()
        self.gridLayout_sing.setObjectName(u"gridLayout_sing")
        self.gridLayout_sing.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.la_sing06 = QLabel(Singularities)
        self.la_sing06.setObjectName(u"la_sing06")
        self.la_sing06.setFont(font)

        self.gridLayout_sing.addWidget(self.la_sing06, 5, 0, 1, 1)

        self.la_sing07 = QLabel(Singularities)
        self.la_sing07.setObjectName(u"la_sing07")
        self.la_sing07.setFont(font)

        self.gridLayout_sing.addWidget(self.la_sing07, 6, 0, 1, 1)

        self.sp_sing11 = QSpinBox(Singularities)
        self.sp_sing11.setObjectName(u"sp_sing11")
        self.sp_sing11.setMinimumSize(QSize(50, 0))
        self.sp_sing11.setMaximumSize(QSize(70, 16777215))
        self.sp_sing11.setFont(font)

        self.gridLayout_sing.addWidget(self.sp_sing11, 10, 1, 1, 1)

        self.sp_sing13 = QSpinBox(Singularities)
        self.sp_sing13.setObjectName(u"sp_sing13")
        self.sp_sing13.setMinimumSize(QSize(50, 0))
        self.sp_sing13.setMaximumSize(QSize(70, 16777215))
        self.sp_sing13.setFont(font)

        self.gridLayout_sing.addWidget(self.sp_sing13, 12, 1, 1, 1)

        self.sp_sing05 = QSpinBox(Singularities)
        self.sp_sing05.setObjectName(u"sp_sing05")
        self.sp_sing05.setMinimumSize(QSize(50, 0))
        self.sp_sing05.setMaximumSize(QSize(70, 16777215))
        self.sp_sing05.setFont(font)

        self.gridLayout_sing.addWidget(self.sp_sing05, 4, 1, 1, 1)

        self.la_sing08 = QLabel(Singularities)
        self.la_sing08.setObjectName(u"la_sing08")
        self.la_sing08.setFont(font)

        self.gridLayout_sing.addWidget(self.la_sing08, 7, 0, 1, 1)

        self.sp_sing06 = QSpinBox(Singularities)
        self.sp_sing06.setObjectName(u"sp_sing06")
        self.sp_sing06.setMinimumSize(QSize(50, 0))
        self.sp_sing06.setMaximumSize(QSize(70, 16777215))
        self.sp_sing06.setFont(font)

        self.gridLayout_sing.addWidget(self.sp_sing06, 5, 1, 1, 1)

        self.la_sing02 = QLabel(Singularities)
        self.la_sing02.setObjectName(u"la_sing02")
        self.la_sing02.setFont(font)

        self.gridLayout_sing.addWidget(self.la_sing02, 1, 0, 1, 1)

        self.la_sing10 = QLabel(Singularities)
        self.la_sing10.setObjectName(u"la_sing10")
        self.la_sing10.setFont(font)

        self.gridLayout_sing.addWidget(self.la_sing10, 9, 0, 1, 1)

        self.la_sing11 = QLabel(Singularities)
        self.la_sing11.setObjectName(u"la_sing11")
        self.la_sing11.setFont(font)

        self.gridLayout_sing.addWidget(self.la_sing11, 10, 0, 1, 1)

        self.sp_sing04 = QSpinBox(Singularities)
        self.sp_sing04.setObjectName(u"sp_sing04")
        self.sp_sing04.setMinimumSize(QSize(50, 0))
        self.sp_sing04.setMaximumSize(QSize(70, 16777215))
        self.sp_sing04.setFont(font)

        self.gridLayout_sing.addWidget(self.sp_sing04, 3, 1, 1, 1)

        self.la_sing05 = QLabel(Singularities)
        self.la_sing05.setObjectName(u"la_sing05")
        self.la_sing05.setFont(font)

        self.gridLayout_sing.addWidget(self.la_sing05, 4, 0, 1, 1)

        self.la_sing13 = QLabel(Singularities)
        self.la_sing13.setObjectName(u"la_sing13")
        self.la_sing13.setFont(font)

        self.gridLayout_sing.addWidget(self.la_sing13, 12, 0, 1, 1)

        self.la_sing03 = QLabel(Singularities)
        self.la_sing03.setObjectName(u"la_sing03")
        self.la_sing03.setFont(font)

        self.gridLayout_sing.addWidget(self.la_sing03, 2, 0, 1, 1)

        self.sp_sing08 = QSpinBox(Singularities)
        self.sp_sing08.setObjectName(u"sp_sing08")
        self.sp_sing08.setMinimumSize(QSize(50, 0))
        self.sp_sing08.setMaximumSize(QSize(70, 16777215))
        self.sp_sing08.setFont(font)

        self.gridLayout_sing.addWidget(self.sp_sing08, 7, 1, 1, 1)

        self.sp_sing10 = QSpinBox(Singularities)
        self.sp_sing10.setObjectName(u"sp_sing10")
        self.sp_sing10.setMinimumSize(QSize(50, 0))
        self.sp_sing10.setMaximumSize(QSize(70, 16777215))
        self.sp_sing10.setFont(font)

        self.gridLayout_sing.addWidget(self.sp_sing10, 9, 1, 1, 1)

        self.sp_sing14 = QSpinBox(Singularities)
        self.sp_sing14.setObjectName(u"sp_sing14")
        self.sp_sing14.setMinimumSize(QSize(50, 0))
        self.sp_sing14.setMaximumSize(QSize(70, 16777215))
        self.sp_sing14.setFont(font)

        self.gridLayout_sing.addWidget(self.sp_sing14, 13, 1, 1, 1)

        self.sp_sing01 = QSpinBox(Singularities)
        self.sp_sing01.setObjectName(u"sp_sing01")
        self.sp_sing01.setMinimumSize(QSize(50, 0))
        self.sp_sing01.setMaximumSize(QSize(70, 16777215))
        self.sp_sing01.setFont(font)

        self.gridLayout_sing.addWidget(self.sp_sing01, 0, 1, 1, 1)

        self.btn_valider = QPushButton(Singularities)
        self.btn_valider.setObjectName(u"btn_valider")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_valider.sizePolicy().hasHeightForWidth())
        self.btn_valider.setSizePolicy(sizePolicy1)
        self.btn_valider.setMaximumSize(QSize(16777215, 140))
        self.btn_valider.setFont(font)

        self.gridLayout_sing.addWidget(self.btn_valider, 14, 0, 1, 2)

        self.sp_sing12 = QSpinBox(Singularities)
        self.sp_sing12.setObjectName(u"sp_sing12")
        self.sp_sing12.setMinimumSize(QSize(50, 0))
        self.sp_sing12.setMaximumSize(QSize(70, 16777215))
        self.sp_sing12.setFont(font)

        self.gridLayout_sing.addWidget(self.sp_sing12, 11, 1, 1, 1)

        self.sp_sing09 = QSpinBox(Singularities)
        self.sp_sing09.setObjectName(u"sp_sing09")
        self.sp_sing09.setMinimumSize(QSize(50, 0))
        self.sp_sing09.setMaximumSize(QSize(70, 16777215))
        self.sp_sing09.setFont(font)

        self.gridLayout_sing.addWidget(self.sp_sing09, 8, 1, 1, 1)

        self.la_sing12 = QLabel(Singularities)
        self.la_sing12.setObjectName(u"la_sing12")
        self.la_sing12.setFont(font)

        self.gridLayout_sing.addWidget(self.la_sing12, 11, 0, 1, 1)

        self.la_sing04 = QLabel(Singularities)
        self.la_sing04.setObjectName(u"la_sing04")
        self.la_sing04.setFont(font)

        self.gridLayout_sing.addWidget(self.la_sing04, 3, 0, 1, 1)

        self.la_sing01 = QLabel(Singularities)
        self.la_sing01.setObjectName(u"la_sing01")
        self.la_sing01.setFont(font)

        self.gridLayout_sing.addWidget(self.la_sing01, 0, 0, 1, 1)

        self.la_sing09 = QLabel(Singularities)
        self.la_sing09.setObjectName(u"la_sing09")
        self.la_sing09.setFont(font)

        self.gridLayout_sing.addWidget(self.la_sing09, 8, 0, 1, 1)

        self.la_sing14 = QLabel(Singularities)
        self.la_sing14.setObjectName(u"la_sing14")
        self.la_sing14.setFont(font)

        self.gridLayout_sing.addWidget(self.la_sing14, 13, 0, 1, 1)

        self.sp_sing03 = QSpinBox(Singularities)
        self.sp_sing03.setObjectName(u"sp_sing03")
        self.sp_sing03.setMinimumSize(QSize(50, 0))
        self.sp_sing03.setMaximumSize(QSize(70, 16777215))
        self.sp_sing03.setFont(font)

        self.gridLayout_sing.addWidget(self.sp_sing03, 2, 1, 1, 1)

        self.sp_sing07 = QSpinBox(Singularities)
        self.sp_sing07.setObjectName(u"sp_sing07")
        self.sp_sing07.setMinimumSize(QSize(50, 0))
        self.sp_sing07.setMaximumSize(QSize(70, 16777215))
        self.sp_sing07.setFont(font)

        self.gridLayout_sing.addWidget(self.sp_sing07, 6, 1, 1, 1)

        self.sp_sing02 = QSpinBox(Singularities)
        self.sp_sing02.setObjectName(u"sp_sing02")
        self.sp_sing02.setMinimumSize(QSize(50, 0))
        self.sp_sing02.setMaximumSize(QSize(70, 16777215))
        self.sp_sing02.setFont(font)

        self.gridLayout_sing.addWidget(self.sp_sing02, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_sing, 1, 0, 1, 1)


        self.retranslateUi(Singularities)

        QMetaObject.connectSlotsByName(Singularities)
    # setupUi

    def retranslateUi(self, Singularities):
        Singularities.setWindowTitle(QCoreApplication.translate("Singularities", u"Singularities", None))
        self.la_tilte.setText(QCoreApplication.translate("Singularities", u"Singularities", None))
        self.la_duct_shape.setText(QCoreApplication.translate("Singularities", u"Duct shape", None))
        self.la_sing06.setText(QCoreApplication.translate("Singularities", u"Sing06", None))
        self.la_sing07.setText(QCoreApplication.translate("Singularities", u"Sing07", None))
        self.la_sing08.setText(QCoreApplication.translate("Singularities", u"Sing08", None))
        self.la_sing02.setText(QCoreApplication.translate("Singularities", u"Sing02", None))
        self.la_sing10.setText(QCoreApplication.translate("Singularities", u"Sing10", None))
        self.la_sing11.setText(QCoreApplication.translate("Singularities", u"Sing11", None))
        self.la_sing05.setText(QCoreApplication.translate("Singularities", u"Sing05", None))
        self.la_sing13.setText(QCoreApplication.translate("Singularities", u"Sing13", None))
        self.la_sing03.setText(QCoreApplication.translate("Singularities", u"Sing03", None))
        self.btn_valider.setText(QCoreApplication.translate("Singularities", u"Validate", None))
        self.la_sing12.setText(QCoreApplication.translate("Singularities", u"Sing12", None))
        self.la_sing04.setText(QCoreApplication.translate("Singularities", u"Sing04", None))
        self.la_sing01.setText(QCoreApplication.translate("Singularities", u"Sing01", None))
        self.la_sing09.setText(QCoreApplication.translate("Singularities", u"Sing09", None))
        self.la_sing14.setText(QCoreApplication.translate("Singularities", u"Sing14", None))
    # retranslateUi

