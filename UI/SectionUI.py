# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SectionUI.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QTableView, QWidget)

class Ui_Form_duct_section(object):
    def setupUi(self, Form_duct_section):
        if not Form_duct_section.objectName():
            Form_duct_section.setObjectName(u"Form_duct_section")
        Form_duct_section.resize(480, 500)
        Form_duct_section.setMinimumSize(QSize(480, 500))
        font = QFont()
        font.setPointSize(11)
        Form_duct_section.setFont(font)
        Form_duct_section.setLocale(QLocale(QLocale.English, QLocale.Europe))
        self.gridLayout = QGridLayout(Form_duct_section)
        self.gridLayout.setObjectName(u"gridLayout")
        self.la_section_length = QLabel(Form_duct_section)
        self.la_section_length.setObjectName(u"la_section_length")
        self.la_section_length.setMinimumSize(QSize(138, 0))
        self.la_section_length.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.la_section_length.setIndent(4)

        self.gridLayout.addWidget(self.la_section_length, 6, 0, 1, 1)

        self.rbtn_circularduct = QRadioButton(Form_duct_section)
        self.grbtn_gaine = QButtonGroup(Form_duct_section)
        self.grbtn_gaine.setObjectName(u"grbtn_gaine")
        self.grbtn_gaine.addButton(self.rbtn_circularduct)
        self.rbtn_circularduct.setObjectName(u"rbtn_circularduct")
        self.rbtn_circularduct.setChecked(True)

        self.gridLayout.addWidget(self.rbtn_circularduct, 0, 0, 1, 2)

        self.la_flow_speed = QLabel(Form_duct_section)
        self.la_flow_speed.setObjectName(u"la_flow_speed")
        self.la_flow_speed.setMinimumSize(QSize(138, 0))
        self.la_flow_speed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.la_flow_speed.setIndent(4)

        self.gridLayout.addWidget(self.la_flow_speed, 7, 0, 1, 1)

        self.la_linAPD = QLabel(Form_duct_section)
        self.la_linAPD.setObjectName(u"la_linAPD")
        self.la_linAPD.setMinimumSize(QSize(138, 0))
        self.la_linAPD.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.la_linAPD.setIndent(4)

        self.gridLayout.addWidget(self.la_linAPD, 8, 0, 1, 1)

        self.le_section_length = QLineEdit(Form_duct_section)
        self.le_section_length.setObjectName(u"le_section_length")
        self.le_section_length.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.le_section_length, 6, 1, 1, 4)

        self.le_duct_height = QLineEdit(Form_duct_section)
        self.le_duct_height.setObjectName(u"le_duct_height")
        self.le_duct_height.setMinimumSize(QSize(138, 0))
        self.le_duct_height.setMaxLength(32767)
        self.le_duct_height.setFrame(True)
        self.le_duct_height.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.le_duct_height, 3, 0, 1, 1)

        self.btn_add_sing = QPushButton(Form_duct_section)
        self.btn_add_sing.setObjectName(u"btn_add_sing")
        self.btn_add_sing.setMinimumSize(QSize(0, 134))
        self.btn_add_sing.setAutoDefault(False)

        self.gridLayout.addWidget(self.btn_add_sing, 9, 5, 1, 1)

        self.la_flow_rate_unit = QLabel(Form_duct_section)
        self.la_flow_rate_unit.setObjectName(u"la_flow_rate_unit")

        self.gridLayout.addWidget(self.la_flow_rate_unit, 5, 5, 1, 1)

        self.la_duct_width_unit = QLabel(Form_duct_section)
        self.la_duct_width_unit.setObjectName(u"la_duct_width_unit")

        self.gridLayout.addWidget(self.la_duct_width_unit, 3, 5, 1, 1)

        self.le_duct_width = QLineEdit(Form_duct_section)
        self.le_duct_width.setObjectName(u"le_duct_width")
        self.le_duct_width.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.le_duct_width, 3, 3, 1, 2)

        self.la_flow_rate = QLabel(Form_duct_section)
        self.la_flow_rate.setObjectName(u"la_flow_rate")
        self.la_flow_rate.setMinimumSize(QSize(138, 0))
        self.la_flow_rate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.la_flow_rate.setIndent(4)

        self.gridLayout.addWidget(self.la_flow_rate, 5, 0, 1, 1)

        self.la_singAPD = QLabel(Form_duct_section)
        self.la_singAPD.setObjectName(u"la_singAPD")
        self.la_singAPD.setMinimumSize(QSize(138, 0))
        self.la_singAPD.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.la_singAPD.setIndent(4)

        self.gridLayout.addWidget(self.la_singAPD, 10, 0, 1, 1)

        self.la_section_length_unit = QLabel(Form_duct_section)
        self.la_section_length_unit.setObjectName(u"la_section_length_unit")

        self.gridLayout.addWidget(self.la_section_length_unit, 6, 5, 1, 1)

        self.le_flow_speed = QLineEdit(Form_duct_section)
        self.le_flow_speed.setObjectName(u"le_flow_speed")
        self.le_flow_speed.setEnabled(False)
        self.le_flow_speed.setFrame(False)
        self.le_flow_speed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.le_flow_speed, 7, 1, 1, 4)

        self.la_diameter_unit = QLabel(Form_duct_section)
        self.la_diameter_unit.setObjectName(u"la_diameter_unit")

        self.gridLayout.addWidget(self.la_diameter_unit, 2, 5, 1, 1)

        self.la_linAPD_unit = QLabel(Form_duct_section)
        self.la_linAPD_unit.setObjectName(u"la_linAPD_unit")

        self.gridLayout.addWidget(self.la_linAPD_unit, 8, 5, 1, 1)

        self.rbtn_rectanguladuct = QRadioButton(Form_duct_section)
        self.grbtn_gaine.addButton(self.rbtn_rectanguladuct)
        self.rbtn_rectanguladuct.setObjectName(u"rbtn_rectanguladuct")
        self.rbtn_rectanguladuct.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.rbtn_rectanguladuct, 0, 2, 1, 3)

        self.la_add_APD = QLabel(Form_duct_section)
        self.la_add_APD.setObjectName(u"la_add_APD")
        self.la_add_APD.setMinimumSize(QSize(138, 0))
        self.la_add_APD.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.la_add_APD, 11, 0, 1, 1)

        self.le_duct_section = QLineEdit(Form_duct_section)
        self.le_duct_section.setObjectName(u"le_duct_section")
        self.le_duct_section.setEnabled(False)
        self.le_duct_section.setFrame(False)
        self.le_duct_section.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.le_duct_section, 4, 1, 1, 4)

        self.la_singAPD_unit = QLabel(Form_duct_section)
        self.la_singAPD_unit.setObjectName(u"la_singAPD_unit")

        self.gridLayout.addWidget(self.la_singAPD_unit, 10, 5, 1, 1)

        self.le_flow_rate = QLineEdit(Form_duct_section)
        self.le_flow_rate.setObjectName(u"le_flow_rate")
        self.le_flow_rate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.le_flow_rate, 5, 1, 1, 4)

        self.la_duct_sheath = QLabel(Form_duct_section)
        self.la_duct_sheath.setObjectName(u"la_duct_sheath")
        self.la_duct_sheath.setMinimumSize(QSize(138, 0))
        self.la_duct_sheath.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.la_duct_sheath.setIndent(4)

        self.gridLayout.addWidget(self.la_duct_sheath, 4, 0, 1, 1)

        self.la_duct_section_unit = QLabel(Form_duct_section)
        self.la_duct_section_unit.setObjectName(u"la_duct_section_unit")

        self.gridLayout.addWidget(self.la_duct_section_unit, 4, 5, 1, 1)

        self.tV_sing = QTableView(Form_duct_section)
        self.tV_sing.setObjectName(u"tV_sing")
        self.tV_sing.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.tV_sing, 9, 0, 1, 5)

        self.le_singAPD = QLineEdit(Form_duct_section)
        self.le_singAPD.setObjectName(u"le_singAPD")
        self.le_singAPD.setEnabled(False)
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        self.le_singAPD.setPalette(palette)
        self.le_singAPD.setFrame(False)
        self.le_singAPD.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.le_singAPD, 10, 1, 1, 4)

        self.le_linAPD = QLineEdit(Form_duct_section)
        self.le_linAPD.setObjectName(u"le_linAPD")
        self.le_linAPD.setEnabled(False)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        self.le_linAPD.setPalette(palette1)
        self.le_linAPD.setFrame(False)
        self.le_linAPD.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.le_linAPD, 8, 1, 1, 4)

        self.cbb_material = QComboBox(Form_duct_section)
        self.cbb_material.setObjectName(u"cbb_material")
        self.cbb_material.setLayoutDirection(Qt.LeftToRight)
        self.cbb_material.setEditable(False)
        self.cbb_material.setModelColumn(0)

        self.gridLayout.addWidget(self.cbb_material, 1, 0, 1, 6)

        self.la_duct_height_unit = QLabel(Form_duct_section)
        self.la_duct_height_unit.setObjectName(u"la_duct_height_unit")

        self.gridLayout.addWidget(self.la_duct_height_unit, 3, 1, 1, 1)

        self.la_flow_speed_unit = QLabel(Form_duct_section)
        self.la_flow_speed_unit.setObjectName(u"la_flow_speed_unit")

        self.gridLayout.addWidget(self.la_flow_speed_unit, 7, 5, 1, 1)

        self.le_add_APD = QLineEdit(Form_duct_section)
        self.le_add_APD.setObjectName(u"le_add_APD")
        self.le_add_APD.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.le_add_APD, 11, 1, 1, 4)

        self.la_unite_PdCdiv = QLabel(Form_duct_section)
        self.la_unite_PdCdiv.setObjectName(u"la_unite_PdCdiv")

        self.gridLayout.addWidget(self.la_unite_PdCdiv, 11, 5, 1, 1)

        self.la_diameter = QLabel(Form_duct_section)
        self.la_diameter.setObjectName(u"la_diameter")
        self.la_diameter.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.la_diameter.setIndent(4)

        self.gridLayout.addWidget(self.la_diameter, 2, 0, 1, 1)

        self.cbb_diameter = QComboBox(Form_duct_section)
        self.cbb_diameter.setObjectName(u"cbb_diameter")
        self.cbb_diameter.setEnabled(True)

        self.gridLayout.addWidget(self.cbb_diameter, 2, 1, 1, 4)

        QWidget.setTabOrder(self.rbtn_circularduct, self.rbtn_rectanguladuct)
        QWidget.setTabOrder(self.rbtn_rectanguladuct, self.cbb_material)
        QWidget.setTabOrder(self.cbb_material, self.cbb_diameter)
        QWidget.setTabOrder(self.cbb_diameter, self.le_duct_height)
        QWidget.setTabOrder(self.le_duct_height, self.le_duct_width)
        QWidget.setTabOrder(self.le_duct_width, self.le_duct_section)
        QWidget.setTabOrder(self.le_duct_section, self.le_flow_rate)
        QWidget.setTabOrder(self.le_flow_rate, self.le_section_length)
        QWidget.setTabOrder(self.le_section_length, self.le_flow_speed)
        QWidget.setTabOrder(self.le_flow_speed, self.le_linAPD)
        QWidget.setTabOrder(self.le_linAPD, self.btn_add_sing)
        QWidget.setTabOrder(self.btn_add_sing, self.tV_sing)
        QWidget.setTabOrder(self.tV_sing, self.le_singAPD)

        self.retranslateUi(Form_duct_section)

        QMetaObject.connectSlotsByName(Form_duct_section)
    # setupUi

    def retranslateUi(self, Form_duct_section):
        Form_duct_section.setWindowTitle(QCoreApplication.translate("Form_duct_section", u"Duct section", None))
        self.la_section_length.setText(QCoreApplication.translate("Form_duct_section", u"Section length", None))
        self.rbtn_circularduct.setText(QCoreApplication.translate("Form_duct_section", u"Circular duct", None))
        self.la_flow_speed.setText(QCoreApplication.translate("Form_duct_section", u"Flow speed", None))
        self.la_linAPD.setText(QCoreApplication.translate("Form_duct_section", u"Linear APD", None))
        self.le_section_length.setPlaceholderText(QCoreApplication.translate("Form_duct_section", u"Enter section length", None))
        self.le_duct_height.setPlaceholderText(QCoreApplication.translate("Form_duct_section", u"Enter duct height", None))
        self.btn_add_sing.setText(QCoreApplication.translate("Form_duct_section", u"Add\n"
" singularity", None))
        self.la_flow_rate_unit.setText(QCoreApplication.translate("Form_duct_section", u"m\u00b3/h", None))
        self.la_duct_width_unit.setText(QCoreApplication.translate("Form_duct_section", u"mm", None))
        self.le_duct_width.setPlaceholderText(QCoreApplication.translate("Form_duct_section", u"Enter duct width", None))
        self.la_flow_rate.setText(QCoreApplication.translate("Form_duct_section", u"Flow rate", None))
        self.la_singAPD.setText(QCoreApplication.translate("Form_duct_section", u"Singular APD", None))
        self.la_section_length_unit.setText(QCoreApplication.translate("Form_duct_section", u"m", None))
        self.le_flow_speed.setPlaceholderText("")
        self.la_diameter_unit.setText(QCoreApplication.translate("Form_duct_section", u"mm", None))
        self.la_linAPD_unit.setText(QCoreApplication.translate("Form_duct_section", u"Pa", None))
        self.rbtn_rectanguladuct.setText(QCoreApplication.translate("Form_duct_section", u"Rectangular duct", None))
        self.la_add_APD.setText(QCoreApplication.translate("Form_duct_section", u"Additionnal APD", None))
        self.la_singAPD_unit.setText(QCoreApplication.translate("Form_duct_section", u"Pa", None))
        self.le_flow_rate.setPlaceholderText(QCoreApplication.translate("Form_duct_section", u"Enter flow rate", None))
        self.la_duct_sheath.setText(QCoreApplication.translate("Form_duct_section", u"Duct section", None))
        self.la_duct_section_unit.setText(QCoreApplication.translate("Form_duct_section", u"m\u00b2", None))
        self.le_singAPD.setPlaceholderText("")
        self.le_linAPD.setPlaceholderText("")
        self.cbb_material.setCurrentText("")
        self.cbb_material.setPlaceholderText(QCoreApplication.translate("Form_duct_section", u"Choose duct material", None))
        self.la_duct_height_unit.setText(QCoreApplication.translate("Form_duct_section", u"mm", None))
        self.la_flow_speed_unit.setText(QCoreApplication.translate("Form_duct_section", u"m/s", None))
        self.la_unite_PdCdiv.setText(QCoreApplication.translate("Form_duct_section", u"Pa", None))
        self.la_diameter.setText(QCoreApplication.translate("Form_duct_section", u"Diameter", None))
        self.cbb_diameter.setPlaceholderText(QCoreApplication.translate("Form_duct_section", u"choose duct diameter", None))
    # retranslateUi

