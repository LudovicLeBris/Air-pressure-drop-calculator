import copy

from PySide6 import QtWidgets, QtCore
from UI.AirPressureDropGUI import Ui_form_airpressuredrop
from UI.SectionUI import Ui_Form_duct_section
from UI.SingularityUI import Ui_Singularities

from API import AirPressureDrop
from API import utils


def intvalidator(sentence: str) -> str:
    """
    Input validation with numbers only

    Args:
        sentence (str) : entry to be validated

    Returns:
        return blank string if argument is not valid, otherwise return the argument
    """
    validator = QtCore.QRegularExpression("^\d*$")
    match = validator.match(sentence)
    if not match.hasMatch():
        return ""
    return sentence


class MainWindow(QtWidgets.QWidget, Ui_form_airpressuredrop):
    """
    Main window display. This window summarizes the totals air pressure drops, display the air characteristics, and
    manage the ducts sections.

    Class attributes:
        SECTIONS : dict
            Class attribute storing the name, the duct section object and the window section object for each duct
            section created.

    Methods:
        setupcustomUI:
            Special configuration for some UI elements.
        setupConnections:
            Set the different signals of the UI elements.
        masks:
            Run the "intvalidator" function for the UI elements that require it.
        majtotalcalculation:
            Calculate the totals in all the UI elements when any change are detected.
        addSection:
            Allow adding duct section. Add window section in the toolbox widget and a duct section instance in the class
                attribute SECTIONS.
        remSection:
            Remove the active section from the toolbox widget and the class attribute SECTIONS.
        toggleAirOptions:
            Enable or disable the air characteristics fields.
        updateAirDatas:
            Update the air datas for the air drop calculations.
    """
    SECTIONS = {}

    def __init__(self):
        """
        Construct the main window elements and signals
        """
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setupcustomUI()
        self.setupConnections()
        self.show()

    def setupcustomUI(self):
        """
        Special configuration for some UI elements.

        Returns:
            None
        """
        self.tB_sections.removeItem(0)
        self.addSection()
        self.le_temperature.setText(str(AirPressureDrop.AIR.temperature))
        self.le_altitude.setText(str(AirPressureDrop.AIR.altitude))
        self.majtotalcalculation()

    def setupConnections(self):
        """
        Set the different signals of the UI elements.

        Returns:
            None
        """
        self.le_temperature.textChanged.connect(self.masks)
        self.le_altitude.textChanged.connect(self.masks)
        self.le_add_APD.textChanged.connect(self.masks)
        self.btn_add_section.clicked.connect(self.addSection)
        self.btn_remove_section.clicked.connect(self.remSection)
        self.chb_modif_air.toggled.connect(self.toggleAirOptions)
        self.le_temperature.editingFinished.connect(self.updateAirDatas)
        self.le_altitude.editingFinished.connect(self.updateAirDatas)
        self.le_add_APD.editingFinished.connect(self.majtotalcalculation)
        for v in self.SECTIONS.values():
            v["section window"].maj.connect(self.majtotalcalculation)

    def masks(self):
        """
        Run the "intvalidator" function for the UI elements that require it.

        Returns:
            None
        """
        self.le_temperature.setText(intvalidator(self.le_temperature.text()))
        self.le_altitude.setText(intvalidator(self.le_altitude.text()))
        self.le_add_APD.setText(intvalidator(self.le_add_APD.text()))

    def majtotalcalculation(self):
        """
        Calculate the totals in all the UI elements when any change are detected.

        Returns:
            None
        """
        sections_addapd = sum([v["section data"].optionals_pressure_drop for v in self.SECTIONS.values()])
        self.le_sections_APD.setText(str(sections_addapd))

        if self.le_add_APD.text() == "":
            add_apd = 0
        else:
            add_apd = int(self.le_add_APD.text())
        total_addapd = sections_addapd + add_apd
        self.le_total_add_APD.setText(str(total_addapd))

        total_lin_apd = round(sum([v["section data"].linear_pressure_drop for v in self.SECTIONS.values()]), 3)
        self.le_total_linAPD.setText(str(total_lin_apd))

        total_sing_apd = sum([v["section data"].singular_pressure_drop for v in self.SECTIONS.values()])
        self.le_total_singAPD.setText(str(total_sing_apd))

        total_apd = round(float(self.le_total_linAPD.text()) + float(self.le_total_singAPD.text()) + total_addapd, 3)
        self.le_total_APD.setText(str(total_apd))

    def addSection(self):
        """
        Allow adding duct section. Add window section in the toolbox widget and a duct section object in the class
        attribute SECTIONS.

        In details:
            - give a name for duct section identification
            - create a DuctSection instance from API module AirPressureDrop
            - create a SectionWindow instance for displaying the duct section datas in the toolbox widget

        Each element is stored in the class attribute SECTIONS with the following diagram:
            {number of index section: {
                "name": "name of the section, default : S + index number",
                "section data": "duct section instance",
                "section window": "duct section window instance"}}
        The number of index section is incremental

        Returns:
            None
        """
        if len(self.SECTIONS) == 0:
            new_index = 1
        else:
            last_index = list(self.SECTIONS.keys())[-1]
            new_index = last_index + 1
        self.SECTIONS[new_index] = {}
        self.SECTIONS[new_index]["name"] = f"S{new_index}"
        name = self.SECTIONS[new_index].get("name")
        self.SECTIONS[new_index]["section data"] = AirPressureDrop.DuctSection()
        section_data = self.SECTIONS[new_index].get("section data")
        self.SECTIONS[new_index]["section window"] = SectionWindow(section_data)
        section_window = self.SECTIONS[new_index].get("section window")
        section_window.setObjectName(name)
        self.tB_sections.addItem(section_window, f"Section #{new_index}")
        self.tB_sections.setCurrentIndex(new_index - 1)
        section_window.maj.connect(self.majtotalcalculation)
        self.majtotalcalculation()

    def remSection(self):
        """
        Remove the active section from the toolbox widget and the class attribute SECTIONS.

        Returns:
            None
        """
        section_window_index = self.tB_sections.currentIndex()
        section_index = int(self.tB_sections.currentWidget().objectName()[-1])
        self.tB_sections.removeItem(section_window_index)
        del self.SECTIONS[section_index]
        if section_window_index == 0:
            self.tB_sections.setCurrentIndex(0)
        else:
            self.tB_sections.setCurrentIndex(section_window_index - 1)
        self.majtotalcalculation()

    def toggleAirOptions(self):
        """
        Enable or disable the air characteristics fields.

        Returns:
            None
        """
        if self.chb_modif_air.isChecked():
            self.le_temperature.setEnabled(True)
            self.le_altitude.setEnabled(True)
        else:
            self.le_temperature.setEnabled(False)
            self.le_altitude.setEnabled(False)

    def updateAirDatas(self):
        """
        Update the air datas for all the air drop calculations.

        Returns:
            None
        """
        temperature = int(self.le_temperature.text())
        altitude = int(self.le_altitude.text())
        AirPressureDrop.AIR.update_air_datas(temperature, altitude)
        for k, v in self.SECTIONS.items():
            v["section data"].density = AirPressureDrop.AIR.density
            v["section data"].viscosity = AirPressureDrop.AIR.viscosity
            v["section window"].majcalculation()
        self.majtotalcalculation()


class SectionWindow(QtWidgets.QWidget, Ui_Form_duct_section):
    """
    Display a window for setting the air and duct characteristics of the duct section.

    Class attributes:
        maj: QtCore.Signal
            Transmit a classic signal for the main window object

    Instance attributes:
        section_data:
            Instance of the duct section
        singform : dict
            Window object for selection of the singularities
        data:
            singularities datas for construction of the data model class

    Methods:
        setupcustomUI:
            Special configuration for some UI elements.
        setupConnections:
            Set the different signals of the UI elements.
        masks:
            Run the "intvalidator" function for the UI elements that require it.
        majcalculation:
            Calculate all the characteristics of the duct section.
        shape:
            Allow the change the shape of the duct section. Toggle the correct dimension's fields.
        material:
            Allow to change the material of the duct section.
        diameter:
            Allow to change the diameter of the duct section, if shape is circular.
        height_width:
            Allow to change the height or the width of the duct section if shape is rectangular.
        flow_rate:
            Allow to change the flow rate of the air in the duct section.
        section_length:
            Allow to change the length of the duct section.
        additional_apd:
            Allow to add a valur for additional air pressure drop locally ins the duct section.
        addsingularities:
            Show the singularities window for adding singularities in the duct section.
    """
    maj = QtCore.Signal()

    def __init__(self, section_data):
        """
        Construct the duct section window and signals.

        Args:
            section_data: instance of the duct section
            singform : creation of an instance of the Singularities window
            data : singularities datas for construction of the data model class
            model : instance of singularities data model for the tableView widget
        """
        super(SectionWindow, self).__init__()
        self.section_data = section_data
        self.singform = Singularities(self.section_data)
        self.data = [[v[-1], v[0]] for v in self.section_data.singularities.values() if v[0] > 0]
        self.model = TableSingularitiesModel(self.data)
        self.setupUi(self)
        self.setupcustomUI()
        self.setupConnections()

    def setupcustomUI(self):
        """
        Special configuration for some UI elements.

        Returns:
            None
        """
        self.cbb_material.addItems([k for k in utils.ROUGHNESS.keys()])
        self.cbb_material.setCurrentText(str(self.section_data.material))
        self.cbb_diameter.addItems([str(n) for n in utils.STD_CIRCULAR_DIAMETER])
        self.cbb_diameter.setCurrentText(str(self.section_data.equiv_diameter))
        self.la_duct_height_unit.setVisible(False)
        self.le_duct_height.setVisible(False)
        self.la_duct_width_unit.setVisible(False)
        self.le_duct_width.setVisible(False)
        self.le_flow_rate.setText(str(self.section_data.flow_rate))
        self.le_section_length.setText(str(self.section_data.length))
        self.tV_sing.setModel(self.model)
        self.tV_sing.horizontalHeader().hide()
        self.tV_sing.verticalHeader().hide()
        self.tV_sing.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.majcalculation()

    def setupConnections(self):
        """
        Special configuration for some UI elements.

        Returns:
            None
        """
        self.le_duct_height.textChanged.connect(self.masks)
        self.le_duct_width.textChanged.connect(self.masks)
        self.le_flow_rate.textChanged.connect(self.masks)
        self.le_section_length.textChanged.connect(self.masks)
        self.le_add_APD.textChanged.connect(self.masks)
        self.rbtn_circularduct.toggled.connect(self.shape)
        self.cbb_material.currentIndexChanged.connect(self.material)
        self.cbb_diameter.currentIndexChanged.connect(self.diameter)
        self.le_duct_height.editingFinished.connect(self.height_width)
        self.le_duct_width.editingFinished.connect(self.height_width)
        self.le_flow_rate.editingFinished.connect(self.flow_rate)
        self.le_section_length.editingFinished.connect(self.section_length)
        self.le_add_APD.editingFinished.connect(self.additional_apd)
        self.btn_add_sing.clicked.connect(self.addsingularities)
        self.singform.maj.connect(self.majcalculation)

    def masks(self):
        """
        Run the "intvalidator" function for the UI elements that require it.

        Returns:
            None
        """
        self.le_duct_height.setText(intvalidator(self.le_duct_height.text()))
        self.le_duct_width.setText(intvalidator(self.le_duct_width.text()))
        self.le_flow_rate.setText(intvalidator(self.le_flow_rate.text()))
        self.le_section_length.setText(intvalidator(self.le_section_length.text()))
        self.le_add_APD.setText(self.le_add_APD.text())

    def majcalculation(self):
        """
        Calculate all the characteristics of the duct section. Emit a signal to the main window for update the totals
        values.

        Returns:
            None
        """
        self.le_duct_section.setText(str(self.section_data.section))
        self.le_flow_speed.setText(str(self.section_data.flow_speed))
        self.le_linAPD.setText(str(self.section_data.linear_pressure_drop))
        self.le_singAPD.setText(str(self.section_data.singular_pressure_drop))
        self.data = [[v[-1], v[0]] for v in self.section_data.singularities.values() if v[0] > 0]
        self.model = TableSingularitiesModel(self.data)
        self.tV_sing.setModel(self.model)
        self.maj.emit()

    def shape(self):
        """
        Allow the change the shape of the duct section. Toggle the correct dimension's fields.
        In case of rectangular toggled, default values for the height and the width are filled.
        The attribute equiv_diameter is calculated everytime.

        Returns:
            None
        """
        if self.rbtn_circularduct.isChecked():
            self.la_duct_height_unit.setVisible(False)
            self.le_duct_height.setVisible(False)
            self.la_duct_width_unit.setVisible(False)
            self.le_duct_width.setVisible(False)
            self.cbb_diameter.setVisible(True)
            self.la_diameter.setVisible(True)
            self.la_diameter_unit.setVisible(True)
            self.section_data.update_shape(utils.SHAPE[0])
            self.section_data.update_equiv_diameter(int(self.cbb_diameter.currentText()))
            self.majcalculation()
        if self.rbtn_rectanguladuct.isChecked():
            self.la_duct_height_unit.setVisible(True)
            self.le_duct_height.setVisible(True)
            self.la_duct_width_unit.setVisible(True)
            self.le_duct_width.setVisible(True)
            self.cbb_diameter.setVisible(False)
            self.la_diameter.setVisible(False)
            self.la_diameter_unit.setVisible(False)
            self.section_data.update_shape(utils.SHAPE[1], 200, 200)
            self.le_duct_height.setText("200")
            self.le_duct_width.setText("200")
            self.majcalculation()

    def material(self):
        """
        Allow to change the material of the duct section.

        Returns:
            None
        """
        self.section_data.update_material(self.cbb_material.currentText())
        self.majcalculation()

    def diameter(self):
        """
        Allow to change the diameter of the duct section, if shape is circular.

        Returns:
            None
        """
        self.section_data.update_equiv_diameter(int(self.cbb_diameter.currentText()))
        self.majcalculation()

    def height_width(self):
        """
        Allow to change the height or the width of the duct section if shape is rectangular.

        Returns:
            None
        """
        self.section_data.update_equiv_diameter(int(self.le_duct_height.text()), int(self.le_duct_width.text()))
        self.majcalculation()

    def flow_rate(self):
        """
        Allow to change the flow rate of the air in the duct section.

        Returns:
            None
        """
        self.section_data.update_flow_rate(int(self.le_flow_rate.text()))
        self.majcalculation()

    def section_length(self):
        """
        Allow to change the length of the duct section.

        Returns:
            None
        """
        self.section_data.update_length(int(self.le_section_length.text()))
        self.majcalculation()

    def additional_apd(self):
        """
        Allow to add a valur for additional air pressure drop locally ins the duct section.

        Returns:
            None
        """
        self.section_data.update_optionals_pressure(int(self.le_add_APD.text()))
        self.majcalculation()

    def addsingularities(self):
        """
        Show the singularities window for adding singularities in the duct section.

        Returns:
            None
        """
        # self.singform = Singularities(self.section_data)
        self.singform.show()


class TableSingularitiesModel(QtCore.QAbstractTableModel):
    """
    Define the data model use in the tableView in the duct section window

    Attributes:
        data: singularities data from section window instance

    Methods:
        data:
            return the dataset.
        rowCount :
            Count the number of row in the dataset.
        columnCount:
            Count the number of column in the dataset.
    """
    def __init__(self, data):
        """
        Construct the dataset model

        Args:
            data:
                singularities data from section window instance
        """
        super(TableSingularitiesModel, self).__init__()
        if len(data) > 0:
            self._data = data
        else:
            self._data = [["", ""]]

    def data(self, index, role: int = 0):
        """
        Return the dataset.

        Args:
            index: model index
            role: the role of the data model

        Returns:
            Return rows and column of the dataset
        """
        if role == QtCore.Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index) -> int:
        """
        Count the number of row in the dataset

        Args:
            index: model index

        Returns:
            The number of rows in the dataset
        """
        return len(self._data)

    def columnCount(self, index) -> int:
        """
        Count the number of column in the dataset

        Args:
            index: model index

        Returns:
            The number of column in the dataset
        """
        return len(self._data[0])


class Singularities(QtWidgets.QWidget, Ui_Singularities):
    """
    Display a window for update the number of singularities

    Class attributes:
        maj: QtCore.Signal
            Transmit a classic signal for the duct section window instance

    Instance attributes:
        section_data:
            instance of the duct section
        singularities:
            deepcopy of the singularities dictionary of duct section instance
        labels:
            list of the labels widgets in the windows
        spinboxs:
            list of the spinbox widgets in the window
        names:
            list of the specific names of the singularities in the duct section
        numbers:
            list of the number of singularities in the duct section

    Methods:
        setupcustomUI:
            Special configuration for some UI elements.
        setupConnections:
            Set the different signals of the UI elements.
        validate:
            Transmit the data to the duct section window instance, update the duct section instance and close the
            window.
    """
    maj = QtCore.Signal()

    def __init__(self, section_datas):
        """
        Construct the singularities window and signals.

        Args:
            section_datas: instance of the duct section
            singularities: deepcopy of the singularities dictionary of duct section instance
            labels: list of the labels widgets in the windows
            spinboxs: list of the spinbox widgets in the window
            names: list of the specific names of the singularities in the duct section
            numbers: list of the number of singularities in the duct section
        """
        super(Singularities, self).__init__()
        self.section_data = section_datas
        self.singularities = copy.deepcopy(self.section_data.singularities)
        self.setupUi(self)
        self.labels = [self.la_sing01, self.la_sing02, self.la_sing03, self.la_sing04, self.la_sing05, self.la_sing06,
                       self.la_sing07, self.la_sing08, self.la_sing09, self.la_sing10, self.la_sing11, self.la_sing12,
                       self.la_sing13, self.la_sing14]
        self.spinboxs = [self.sp_sing01, self.sp_sing02, self.sp_sing03, self.sp_sing04, self.sp_sing05, self.sp_sing06,
                         self.sp_sing07, self.sp_sing08, self.sp_sing09, self.sp_sing10, self.sp_sing11, self.sp_sing12,
                         self.sp_sing13, self.sp_sing14]
        self.names = [v[2] for v in self.singularities.values()]
        self.numbers = [v[0] for v in self.singularities.values()]
        self.setupcustomUI()
        self.setupConnections()

    def setupcustomUI(self):
        """
        Special configuration for some UI elements.

        Returns:
            None
        """
        self.le_duct_shape.setText(self.section_data.shape)
        list(map(lambda x, y: x.setText(y), self.labels, self.names))
        list(map(lambda x, y: x.setValue(y), self.spinboxs, self.numbers))

    def setupConnections(self):
        """
        Special configuration for some UI elements.

        Returns:
            None
        """
        self.btn_valider.clicked.connect(self.validate)

    def validate(self):
        """
        Transmit the data to the duct section window instance, update the duct section instance and close the window.

        Returns:
            None
        """
        i = 0
        for v in self.singularities.values():
            v[0] = self.spinboxs[i].value()
            i += 1
        self.section_data.update_singularities(self.singularities)
        self.maj.emit()
        self.close()


app = QtWidgets.QApplication()
Window = MainWindow()
app.exec()
