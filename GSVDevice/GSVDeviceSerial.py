from .gsv8 import gsv8


class GSVDeviceSerial(gsv8):
    """
            A wrapped version of the gsv8 class with simplified english-only methods/attributes. All functionality of the
            gsv8 class is maintained and this class can be treated as such. This class only works with serial/USB
            communication.
            :param port: Serial port to connect to.
                        Unix example: "/dev/ttyACM0"
                        Windows example: 1   <-- USB port number
            :param baudrate: serial communication bauddrate
            """
    def __init__(self, port, baudrate=115200):
        super().__init__(port, baudrate)

    def start_constant_transmission(self):
        return self.StartTransmission()

    def stop_constant_transmission(self):
        return self.StopTransmission()

    def read_data(self):
        """
        Sends a request to the device for the current reading when not constantly streaming (start_constant_streaming()
        has not been called). Otherwise returns the latest value from the data transmission stream. When this function
        is called faster than the transmission rate, the previous value is simply returned again.

        :return: Response code and any error text :type list
        """
        return self.ReadValue()

    def set_transmission_rate(self, rate):
        """
        Set the rate at which the device automatically sends data readings to this computer.
        :param rate: The transmission rate in Hz
        :return: None
        """
        return self.writeDataRate(rate)