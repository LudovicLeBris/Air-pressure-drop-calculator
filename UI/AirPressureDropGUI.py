# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AirPressureDropGUI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QToolBox, QWidget)

class Ui_form_airpressuredrop(object):
    def setupUi(self, form_airpressuredrop):
        if not form_airpressuredrop.objectName():
            form_airpressuredrop.setObjectName(u"form_airpressuredrop")
        form_airpressuredrop.resize(880, 686)
        form_airpressuredrop.setMinimumSize(QSize(880, 686))
        font = QFont()
        font.setPointSize(11)
        form_airpressuredrop.setFont(font)
        form_airpressuredrop.setLocale(QLocale(QLocale.English, QLocale.Europe))
        self.gridLayout_4 = QGridLayout(form_airpressuredrop)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gB_Air = QGroupBox(form_airpressuredrop)
        self.gB_Air.setObjectName(u"gB_Air")
        self.gB_Air.setMinimumSize(QSize(260, 160))
        self.gB_Air.setMaximumSize(QSize(400, 180))
        self.gridLayout = QGridLayout(self.gB_Air)
        self.gridLayout.setObjectName(u"gridLayout")
        self.la_altitude = QLabel(self.gB_Air)
        self.la_altitude.setObjectName(u"la_altitude")
        self.la_altitude.setMinimumSize(QSize(150, 0))
        self.la_altitude.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.la_altitude, 1, 0, 1, 1)

        self.chb_modif_air = QCheckBox(self.gB_Air)
        self.chb_modif_air.setObjectName(u"chb_modif_air")
        font1 = QFont()
        font1.setPointSize(9)
        self.chb_modif_air.setFont(font1)
        self.chb_modif_air.setLayoutDirection(Qt.RightToLeft)
        self.chb_modif_air.setIconSize(QSize(16, 16))
        self.chb_modif_air.setCheckable(True)

        self.gridLayout.addWidget(self.chb_modif_air, 2, 0, 1, 3)

        self.la_temperature = QLabel(self.gB_Air)
        self.la_temperature.setObjectName(u"la_temperature")
        self.la_temperature.setMinimumSize(QSize(150, 0))
        self.la_temperature.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.la_temperature, 0, 0, 1, 1)

        self.le_temperature = QLineEdit(self.gB_Air)
        self.le_temperature.setObjectName(u"le_temperature")
        self.le_temperature.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_temperature.sizePolicy().hasHeightForWidth())
        self.le_temperature.setSizePolicy(sizePolicy)
        self.le_temperature.setMinimumSize(QSize(80, 0))
        self.le_temperature.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.le_temperature, 0, 1, 1, 1)

        self.la_temperature_unit = QLabel(self.gB_Air)
        self.la_temperature_unit.setObjectName(u"la_temperature_unit")

        self.gridLayout.addWidget(self.la_temperature_unit, 0, 2, 1, 1)

        self.le_altitude = QLineEdit(self.gB_Air)
        self.le_altitude.setObjectName(u"le_altitude")
        self.le_altitude.setEnabled(False)
        self.le_altitude.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.le_altitude, 1, 1, 1, 1)

        self.la_altitude_unit = QLabel(self.gB_Air)
        self.la_altitude_unit.setObjectName(u"la_altitude_unit")

        self.gridLayout.addWidget(self.la_altitude_unit, 1, 2, 1, 1)


        self.gridLayout_4.addWidget(self.gB_Air, 1, 0, 1, 1)

        self.gB_var_APD = QGroupBox(form_airpressuredrop)
        self.gB_var_APD.setObjectName(u"gB_var_APD")
        self.gB_var_APD.setMinimumSize(QSize(270, 180))
        self.gB_var_APD.setMaximumSize(QSize(400, 220))
        self.gridLayout_3 = QGridLayout(self.gB_var_APD)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.la_total_add_APD = QLabel(self.gB_var_APD)
        self.la_total_add_APD.setObjectName(u"la_total_add_APD")
        self.la_total_add_APD.setMaximumSize(QSize(16777215, 26))
        self.la_total_add_APD.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.la_total_add_APD, 2, 0, 1, 3)

        self.le_total_add_APD = QLineEdit(self.gB_var_APD)
        self.le_total_add_APD.setObjectName(u"le_total_add_APD")
        self.le_total_add_APD.setEnabled(False)
        self.le_total_add_APD.setFrame(False)
        self.le_total_add_APD.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_total_add_APD, 3, 0, 1, 2)

        self.la_total_add_APD_unit = QLabel(self.gB_var_APD)
        self.la_total_add_APD_unit.setObjectName(u"la_total_add_APD_unit")

        self.gridLayout_3.addWidget(self.la_total_add_APD_unit, 3, 2, 1, 1)

        self.la_add_APD_unit = QLabel(self.gB_var_APD)
        self.la_add_APD_unit.setObjectName(u"la_add_APD_unit")

        self.gridLayout_3.addWidget(self.la_add_APD_unit, 1, 2, 1, 1)

        self.le_add_APD = QLineEdit(self.gB_var_APD)
        self.le_add_APD.setObjectName(u"le_add_APD")
        self.le_add_APD.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_add_APD, 1, 1, 1, 1)

        self.la_add_APD = QLabel(self.gB_var_APD)
        self.la_add_APD.setObjectName(u"la_add_APD")
        self.la_add_APD.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.la_add_APD, 1, 0, 1, 1)

        self.la_sections_APD_unit = QLabel(self.gB_var_APD)
        self.la_sections_APD_unit.setObjectName(u"la_sections_APD_unit")

        self.gridLayout_3.addWidget(self.la_sections_APD_unit, 0, 2, 1, 1)

        self.le_sections_APD = QLineEdit(self.gB_var_APD)
        self.le_sections_APD.setObjectName(u"le_sections_APD")
        self.le_sections_APD.setEnabled(False)
        self.le_sections_APD.setFrame(False)
        self.le_sections_APD.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_sections_APD, 0, 1, 1, 1)

        self.la_sections_APD = QLabel(self.gB_var_APD)
        self.la_sections_APD.setObjectName(u"la_sections_APD")
        self.la_sections_APD.setMinimumSize(QSize(180, 0))
        self.la_sections_APD.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.la_sections_APD, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.gB_var_APD, 2, 0, 1, 1)

        self.gB_Results = QGroupBox(form_airpressuredrop)
        self.gB_Results.setObjectName(u"gB_Results")
        self.gB_Results.setMinimumSize(QSize(260, 0))
        self.gB_Results.setMaximumSize(QSize(400, 16777215))
        self.gridLayout_2 = QGridLayout(self.gB_Results)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.la_total_singAPD = QLabel(self.gB_Results)
        self.la_total_singAPD.setObjectName(u"la_total_singAPD")
        self.la_total_singAPD.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.la_total_singAPD, 2, 0, 1, 3)

        self.le_total_APD = QLineEdit(self.gB_Results)
        self.le_total_APD.setObjectName(u"le_total_APD")
        self.le_total_APD.setEnabled(False)
        self.le_total_APD.setMinimumSize(QSize(0, 30))
        self.le_total_APD.setMaximumSize(QSize(180, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(245, 245, 245, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.NoRole, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.NoRole, brush3)
        brush4 = QBrush(QColor(120, 120, 120, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.NoRole, brush5)
        self.le_total_APD.setPalette(palette)
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.le_total_APD.setFont(font2)
        self.le_total_APD.setFrame(False)
        self.le_total_APD.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.le_total_APD, 5, 1, 1, 1)

        self.le_total_singAPD = QLineEdit(self.gB_Results)
        self.le_total_singAPD.setObjectName(u"le_total_singAPD")
        self.le_total_singAPD.setEnabled(False)
        self.le_total_singAPD.setMaximumSize(QSize(180, 16777215))
        self.le_total_singAPD.setFrame(False)
        self.le_total_singAPD.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.le_total_singAPD, 3, 1, 1, 1)

        self.la_total_APD_unit = QLabel(self.gB_Results)
        self.la_total_APD_unit.setObjectName(u"la_total_APD_unit")
        self.la_total_APD_unit.setMinimumSize(QSize(0, 30))
        self.la_total_APD_unit.setFont(font2)

        self.gridLayout_2.addWidget(self.la_total_APD_unit, 5, 2, 1, 1)

        self.la_total_APD = QLabel(self.gB_Results)
        self.la_total_APD.setObjectName(u"la_total_APD")
        self.la_total_APD.setFont(font2)
        self.la_total_APD.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.la_total_APD, 4, 0, 1, 3)

        self.le_total_linAPD = QLineEdit(self.gB_Results)
        self.le_total_linAPD.setObjectName(u"le_total_linAPD")
        self.le_total_linAPD.setEnabled(False)
        self.le_total_linAPD.setMaximumSize(QSize(180, 16777215))
        self.le_total_linAPD.setCursor(QCursor(Qt.WaitCursor))
        self.le_total_linAPD.setFrame(False)
        self.le_total_linAPD.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.le_total_linAPD, 1, 1, 1, 1)

        self.la_total_linAPD_unit = QLabel(self.gB_Results)
        self.la_total_linAPD_unit.setObjectName(u"la_total_linAPD_unit")

        self.gridLayout_2.addWidget(self.la_total_linAPD_unit, 1, 2, 1, 1)

        self.la_total_linAPD = QLabel(self.gB_Results)
        self.la_total_linAPD.setObjectName(u"la_total_linAPD")
        self.la_total_linAPD.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.la_total_linAPD, 0, 0, 1, 3)

        self.la_total_singAPD_unit = QLabel(self.gB_Results)
        self.la_total_singAPD_unit.setObjectName(u"la_total_singAPD_unit")

        self.gridLayout_2.addWidget(self.la_total_singAPD_unit, 3, 2, 1, 1)


        self.gridLayout_4.addWidget(self.gB_Results, 3, 0, 1, 1)

        self.gB_Ducts = QGroupBox(form_airpressuredrop)
        self.gB_Ducts.setObjectName(u"gB_Ducts")
        self.gB_Ducts.setMinimumSize(QSize(500, 0))
        self.gridLayout_5 = QGridLayout(self.gB_Ducts)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tB_sections = QToolBox(self.gB_Ducts)
        self.tB_sections.setObjectName(u"tB_sections")
        self.tB_sections.setMinimumSize(QSize(480, 0))
        self.T1 = QWidget()
        self.T1.setObjectName(u"T1")
        self.T1.setGeometry(QRect(0, 0, 480, 503))
        self.tB_sections.addItem(self.T1, u"Section #1")

        self.gridLayout_5.addWidget(self.tB_sections, 3, 0, 1, 2)

        self.btn_remove_section = QPushButton(self.gB_Ducts)
        self.btn_remove_section.setObjectName(u"btn_remove_section")
        self.btn_remove_section.setAcceptDrops(False)
        self.btn_remove_section.setAutoFillBackground(False)

        self.gridLayout_5.addWidget(self.btn_remove_section, 1, 0, 1, 1)

        self.btn_add_section = QPushButton(self.gB_Ducts)
        self.btn_add_section.setObjectName(u"btn_add_section")

        self.gridLayout_5.addWidget(self.btn_add_section, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.gB_Ducts, 1, 1, 3, 2)

        self.Title_app = QLabel(form_airpressuredrop)
        self.Title_app.setObjectName(u"Title_app")
        self.Title_app.setMinimumSize(QSize(200, 37))
        self.Title_app.setMaximumSize(QSize(16777215, 42))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.Title_app.setFont(font3)
        self.Title_app.setFrameShape(QFrame.NoFrame)
        self.Title_app.setFrameShadow(QFrame.Plain)
        self.Title_app.setLineWidth(1)
        self.Title_app.setMidLineWidth(0)
        self.Title_app.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.Title_app, 0, 0, 1, 3)


        self.retranslateUi(form_airpressuredrop)

        self.tB_sections.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(form_airpressuredrop)
    # setupUi

    def retranslateUi(self, form_airpressuredrop):
        form_airpressuredrop.setWindowTitle(QCoreApplication.translate("form_airpressuredrop", u"APD Calculator", None))
        self.gB_Air.setTitle(QCoreApplication.translate("form_airpressuredrop", u"Air characteristics", None))
        self.la_altitude.setText(QCoreApplication.translate("form_airpressuredrop", u"Altitude", None))
        self.chb_modif_air.setText(QCoreApplication.translate("form_airpressuredrop", u"Change defaults datas", None))
        self.la_temperature.setText(QCoreApplication.translate("form_airpressuredrop", u"Temperature", None))
        self.la_temperature_unit.setText(QCoreApplication.translate("form_airpressuredrop", u"\u00b0C", None))
        self.la_altitude_unit.setText(QCoreApplication.translate("form_airpressuredrop", u"m", None))
        self.gB_var_APD.setTitle(QCoreApplication.translate("form_airpressuredrop", u"Additionnals APD", None))
        self.la_total_add_APD.setText(QCoreApplication.translate("form_airpressuredrop", u"Total additionnals air pressure drops", None))
        self.la_total_add_APD_unit.setText(QCoreApplication.translate("form_airpressuredrop", u"Pa", None))
        self.la_add_APD_unit.setText(QCoreApplication.translate("form_airpressuredrop", u"Pa", None))
        self.la_add_APD.setText(QCoreApplication.translate("form_airpressuredrop", u"Additionnal APD", None))
        self.la_sections_APD_unit.setText(QCoreApplication.translate("form_airpressuredrop", u"Pa", None))
        self.la_sections_APD.setText(QCoreApplication.translate("form_airpressuredrop", u"Section's additionals APD", None))
        self.gB_Results.setTitle(QCoreApplication.translate("form_airpressuredrop", u"Results", None))
        self.la_total_singAPD.setText(QCoreApplication.translate("form_airpressuredrop", u"Total singular air pressure drop", None))
        self.la_total_APD_unit.setText(QCoreApplication.translate("form_airpressuredrop", u"Pa", None))
        self.la_total_APD.setText(QCoreApplication.translate("form_airpressuredrop", u"Total air pressure drop", None))
        self.la_total_linAPD_unit.setText(QCoreApplication.translate("form_airpressuredrop", u"Pa", None))
        self.la_total_linAPD.setText(QCoreApplication.translate("form_airpressuredrop", u"Total linear air pressure drop", None))
        self.la_total_singAPD_unit.setText(QCoreApplication.translate("form_airpressuredrop", u"Pa", None))
        self.gB_Ducts.setTitle(QCoreApplication.translate("form_airpressuredrop", u"Air ducts", None))
        self.tB_sections.setItemText(self.tB_sections.indexOf(self.T1), QCoreApplication.translate("form_airpressuredrop", u"Section #1", None))
        self.btn_remove_section.setText(QCoreApplication.translate("form_airpressuredrop", u"Remove current section", None))
        self.btn_add_section.setText(QCoreApplication.translate("form_airpressuredrop", u"Add a duct section", None))
        self.Title_app.setText(QCoreApplication.translate("form_airpressuredrop", u"AIR PRESSURE DROP CALCULATOR", None))
    # retranslateUi

