"""
Napalm driver for ArubaOS 505 Wi-Fi Device using SSH.
Read https://napalm.readthedocs.io for more information.
"""

from napalm.base import NetworkDriver
from napalm.base.exceptions import (
    ConnectionException,
    SessionLockedException,
    MergeConfigException,
    ReplaceConfigException,
    CommandErrorException,
    )

import json
from helpers import ssh_connector, send_single_cmd

class ArubaOSDriver(NetworkDriver):
    """Napalm driver for ArubaOS 505 Wi-Fi Device."""

    def __init__(self, hostname, username, password, timeout=60, optional_args=None):
        """Initializer."""
        if not optional_args:
            optional_args = {}
        self.hostname = hostname
        self.username = username
        self.password = password
        self.timeout = timeout

        self.platform = "ArubaOS"
        self.profile = [self.platform]
        self.session_info = None
        self.isAlive = False
        self.candidate_config = ''
        self.profile = ['arubaOS']


    def open(self):
        """
        Implementation of NAPALM method 'open' to open a connection to the device.
        """
        try:
            self.session_info = ssh_connector(hostname=self.hostname,username=self.username,
                                              password=self.password)
            self.isAlive = True
            print(f"connected to {self.hostname}\n")
        except ConnectionError as error:
            # Raised if device not available
            #raise ConnectionException(str(error))
            print(f"Failed to connect to {self.hostname}\n")


    def close(self):
        """
        Implementation of NAPALM method 'close'. Closes the connection to the device and does
        the necessary cleanup.
        """
        self.isAlive = False
        self.session_info.close()


    def is_alive(self):
        """
        Implementation of NAPALM method 'is_alive'. This is used to determine if there is a
        pre-existing connection that must be closed.
        :return: Returns a flag with the state of the connection.
        """
        return {"is_alive": self.isAlive}


    def get_config(self, retrieve="all", full=False, sanitized=False):
        """
        :return: The object returned is a dictionary with a key for each configuration store:
            - running(string) - Representation of the  running configuration
        """
        cmd = "show running-config"
        configs = {
            "running": "",
        }

        try:
            config = send_single_cmd(cmd, self.session_info)
            configs['running'] = config
        except:
            print(f"Failed to run the get_config from ArubaOS Driver\n")
        else:
            return configs
