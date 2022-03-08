import math

from API import utils


class Air:
    """
    Define and calculate the air characteristics for air pressure drop calculation.

    Attributes:
        temperature : int
            temperature of the air in celsius degrees (default value : 20 °C)
        altitude : int
            altitude above sea level in meters (default value : 0 m)

    Methods
        density:
            Property methods providing the density property of air
        viscosity:
            Property methods providing the viscosity property of air
        update_air_datas():
            methods for update the air characteristics
                Args:
                    temperature (int) : air temperature of air in °C
                    altitude (int) : altitude above sea level in m
    """
    def __init__(self):
        """
        Construct all the attributes for air characteristics.

        Args:
            temperature : int
                temperature of the air in celsius degrees (default value : 20 °C)
            altitude : int
                altitude above sea level in meters (default value : 0 m)
        """
        self.temperature: int = 20
        self.altitude: int = 0

    def __str__(self) -> str:
        return f"temperature: {self.temperature}°C - altitude: {self.altitude}"

    @property
    def density(self) -> float:
        """
        Property methods providing the density property of air.

        Returns:
            float value of air density
        """
        atm_pressure = (760.85 * math.exp(
            (-0.2840437333 * self.altitude) / (8.31432 * (self.temperature + 273.15)))) * 133.32
        return ((atm_pressure * 28.976) / (8.3144621 * (self.temperature + 273.15))) / 1000

    @property
    def viscosity(self) -> float:
        """
        Property methods providing the viscosity property of air.

        Returns:
            float value of air viscosity
        """
        return (8.8848 * 10 ** (-15) * (self.temperature + 273.15) ** 3 - 3.2398 * 10 ** (-11) * (
                self.temperature + 273.15) ** 2 + 6.2657 * 10 ** (-8) * (
                        self.temperature + 273.15) + 2.3544 * 10 ** (-6)) / (
                       353.05 / (self.temperature + 273.15))

    def update_air_datas(self, temperature: int, altitude: int) -> None:
        """
        Methods for update the air characteristics.

        Args:
            temperature (int) : new temperature in °C
            altitude (int) : new altitude in m

        Returns:
            None
        """
        self.temperature = temperature
        self.altitude = altitude


AIR = Air()


class DuctSection:
    """
    Define characteristics of an air duct section and calculate the air pressure drop.

    Attributes
        density : float
            air density value from AIR class
        viscosity : float
            air viscosity value from AIR class
        shape : str
            shape of the duct section. Circular or rectangular. See "utils" module.
        material : str
            material of the duct section. See "utils" module.
        flow_rate : int
            flow rate of the air in cubic meter per hour (m³/h)
        equiv_diameter : float
            equivalent diameter of the duct section in millimeter.
        length : int
             linear length of the duct section in meter
        singularities : dict
            complex list of principals duct singularities, with numbers, singularity value and complete name
        optionals_pressure : int
            value of optionals pressure

        Methods
            section (property):
                calculation of duct section (in m²)
            flow_speed (property):
                calculation of air flow speed in duct (in m/s)
            linear_pressure_drop (property):
                calculation of linear air pressure drop of duct section with Colebrook formula (in Pa)
            singular_pressure_drop (property):
                calculation of singular air pressure drop of different singularities in attribute "singularities"
            optionals_pressure_drop (property):
                return values of attribute "optionals_pressure"
            total_pressure_drop (property):
                calculation of total pressure drop of the duct section
            update_shape:
                method for update the shape of the duct section and update the equiv_diameter attribute in the same time
                if shape is rectangular and 2 more integer arguments are given (typically height and width of duct).
                    Args:
                        shape (str) : new shape of the duct section
                        *args (int) : height and width of the rectangular duct
            update_material:
                method for update the material of the duct section
                    Args:
                        material (str) : new material of the duct section
            update_flow_rate:
                method for update the air flow rate in duct section
                    Args:
                        flow_rate (int) : new flow rate in duct section
            update_equiv_diameter:
                method for update the diameter or equivalent diameter of the duct section
                    Args:
                        dim1 (int) : new circular diameter or new height of rectangular duct
                        dim2 (int) : new width of rectangular duct
            update_length:
                method for update the length of linear duct section
                    Args:
                        length (int) : new length of duct section
            update_singularities:
                method for update dictionary of duct singularities
                    Args:
                        singularities (dict) : new dictionary of singularities
            update_optionals_pressure:
                method for update optionals pressure
                    Args:
                        opt_pressure (int) : new optional pressure
    """
    def __init__(self):
        """
        Construct all the attributes for duct section characteristics.

        Args:
            density : float
                air density value from AIR class
            viscosity : float
                air viscosity value from AIR class
            shape : str
                shape of the duct section. Circular or rectangular. See "utils" module.
            material : str
                material of the duct section. See "utils" module.
            flow_rate : int
                flow rate of the air in cubic meter per hour (m³/h)
            equiv_diameter : float
                equivalent diameter of the duct section in millimeter.
            length : int
                 linear length of the duct section in meter
            singularities : dict
                complex list of principals duct singularities, with numbers, singularity value and complete name
            optionals_pressure : int
                value of optionals pressure
        """
        self.density: float = AIR.density
        self.viscosity: float = AIR.viscosity
        self.shape: str = "circular"
        self.material: str = "galvanised steel"
        self.flow_rate: int = 1000
        self.equiv_diameter: float = 250
        self.length: int = 1
        self.singularities: dict = utils.SING_CIRC
        self.optionals_pressure: int = 0

    def __str__(self):
        duct_section = f"Shape: {self.shape},\nMaterial: {self.material},\nFlow rate: {self.flow_rate} m³/h,\n" \
                      f"Equivalent diameter: {self.equiv_diameter} mm,\nLength: {self.length} m,\n" \
                      f"Singularities:\n{self.singularities},\nOptionnals pressure drop: {self.optionals_pressure}"
        return duct_section

    def __repr__(self):
        return f'Duct section'

    @property
    def section(self) -> float:
        """
        Property method for calculation of duct section (in m²)

        Returns:
            float : section value rounded to 3 decimal places
        """
        section = (math.pi * (self.equiv_diameter / 1000) ** 2) / 4
        return round(section, 3)

    @property
    def flow_speed(self) -> float:
        """
        Property method for calculation of air flow speed in duct (in m/s)

        Returns:
            float : flow speed value rounded to 3 decimal places
        """
        return round((self.flow_rate / 3600) / self.section, 3)

    @property
    def linear_pressure_drop(self) -> float:
        """
        Property method for calculation of linear air pressure drop of duct section with Colebrook formula (in Pa)

        Returns:
            float : linear pressure drop value rounded to 3 decimal places
        """
        reynolds = (self.flow_speed * (self.equiv_diameter * 10 ** -3)) / self.viscosity
        laminar_lambda = 64 / reynolds
        if reynolds <= 2400:
            return (laminar_lambda * self.length * self.density *
                    (self.flow_speed ** 2)) / (2 * (self.equiv_diameter / 1000))
        else:
            roughness = utils.ROUGHNESS.get(self.material)
            b = 2.51 / reynolds
            roughness_lambda = (1 / (-2 * math.log10(roughness))) ** 2
            i = 0
            lambda_list = [(1 / (-2 * math.log10(roughness + b * (1 / math.sqrt(roughness_lambda))))) ** 2]
            while i < 12:
                temp_lambda = (1 / (-2 * math.log10(roughness + b * (1 / math.sqrt(lambda_list[-1]))))) ** 2
                lambda_list.append(temp_lambda)
                i += 1
            lambda_list2 = [i - roughness_lambda for i in lambda_list]
            min_lambda2 = min(lambda_list2[2:])
            lambda_def = lambda_list[lambda_list2[:6].index(min_lambda2)]
            return round((lambda_def * self.length * self.density * (self.flow_speed ** 2)) /
                         (2 * (self.equiv_diameter / 1000)), 3)

    @property
    def singular_pressure_drop(self) -> float:
        """
        Property method for calculation of singular air pressure drop of different singularities in attribute
        "singularities"

        Returns:
            float : singular pressure drop value rounded to 3 decimal places
        """
        total_sing = 0
        for key, value in self.singularities.items():
            sing = value[0] * value[1]
            total_sing += sing
        return round(total_sing * self.density * (self.flow_speed ** 2) / 2, 3)

    @property
    def optionals_pressure_drop(self) -> int:
        """
        Property method who return values of attribute "optionals_pressure"

        Returns:
            int : optional pressure drop value
        """
        return int(self.optionals_pressure)

    @property
    def total_pressure_drop(self) -> float:
        """
        Property method for calculation of total pressure drop of the duct section

        Returns:
            float : total pressure drop value rounded to 3 decimal places
        """
        return round(self.linear_pressure_drop + self.singular_pressure_drop + self.optionals_pressure_drop, 3)

    def update_shape(self, shape: str, *args: int) -> bool:
        """
        Method for update the shape of the duct section and update the equiv_diameter attribute in the same time
        if shape is rectangular and 2 more integer arguments are given (typically height and width of duct).

        Args:
            shape (str) : new shape of the duct section
            *args (int) : height and width of the rectangular duct

        Returns:
            Bool value, True if ok, False if error

        Raises:
            ValueError if shape is not "circular" or "rectangular"
        """
        if shape not in utils.SHAPE:
            raise ValueError("Shape should be only circular or rectangular")
        self.shape = shape
        if shape == "circular":
            self.singularities = utils.SING_CIRC
        if shape == "rectangular":
            self.singularities = utils.SING_RECT
            if len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
                self.equiv_diameter = utils.equiv_diameter(*args)
        return True

    def update_material(self, material: str) -> bool:
        """
        Method for update the material of the duct section.

        Args:
            material (str) : new material of the duct section

        Returns:
            Bool value, True if ok, False if error

        Raises:
            ValueError if material is not in the roughness dictionary
        """
        if material not in utils.ROUGHNESS.keys():
            raise ValueError("Wrong material")
        self.material = material
        return True

    def update_flow_rate(self, flow_rate: int) -> bool:
        """
        Method for update the air flow rate in duct section.

        Args:
            flow_rate (int) : new flow rate in duct section

        Returns:
            Bool value, True if ok, False if error

        Raises:
            ValueError if value is less or equal than 0
        """
        if flow_rate <= 0:
            raise ValueError("Flow rate must greater than zero")
        self.flow_rate = flow_rate
        return True

    def update_equiv_diameter(self, dim1: int, dim2: int = 0) -> bool:
        """
        Method for update the diameter or equivalent diameter of the duct section.

        Args:
            dim1 (int) : new circular diameter or new height of rectangular duct
            dim2 (int) : new width of rectangular duct

        Returns:
            Bool value, True if ok, False if error

        Raises:
            ValueError if dim2 is less o equal than 0 if shape is rectangular
            ValueError if dim2 is less or equal than 0
        """
        if self.shape == "circular" and dim1 > 0:
            self.equiv_diameter = dim1
            return True
        elif self.shape == "rectangular" and dim2 > 0:
            self.equiv_diameter = utils.equiv_diameter(dim1, dim2)
            return True
        elif self.shape == "rectangular" and dim2 <= 0:
            raise ValueError("The second dimension of a rectangular shape must be greater than zero")
        elif dim1 <= 0:
            raise ValueError("Values must be greater than zero")

    def update_length(self, length: int) -> bool:
        """
        Method for update the length of linear duct section.

        Args:
            length (int) : new length of duct section

        Returns:
            Bool value, True if ok, False if error

        Raises:
            ValueError if value is less or equal than 0
        """
        if length <= 0:
            raise ValueError("Length value must be greater than zero")
        else:
            self.length = length
            return True

    def update_singularities(self, singularities: dict) -> bool:
        """
        Method for update dictionary of duct singularities.

        Args:
            singularities (dict) : new dictionary of singularities

        Returns:
            Bool value, True if ok, False if error

        Raises:
            TypeError if argument is not a dictionary
        """
        if not isinstance(singularities, dict):
            raise TypeError("The singularities entry must be a dictionary")
        else:
            self.singularities = singularities
            return True

    def update_optionals_pressure(self, opt_pressure: int) -> bool:
        """
        Method for update optionals pressure.

        Args:
            opt_pressure (int) : new optional pressure

        Returns:
            Bool value, True if ok, False if error

        Raises:
            ValueError if value is less or equal than 0
        """
        if opt_pressure < 0:
            raise ValueError("Value must be greater or equal than zero")
        else:
            self.optionals_pressure = opt_pressure
            return True


if __name__ == "__main__":
    # print(AIR)
    # print(AIR.density, AIR.viscosity)
    # AIR.update_air_datas(0, 2000)
    # print(AIR)
    # print(AIR.density, AIR.viscosity)

    S1 = DuctSection()

    # print(S1)
    # S1.update_optionals_pressure()
    # print(S1)

    print(S1.flow_speed)
    S1.update_equiv_diameter(500)
    print(S1.flow_speed)
