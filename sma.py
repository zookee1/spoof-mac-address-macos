#!/usr/bin/env python
import random
import os

macaddress = "52:54:00:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        )

os.system("sudo ifconfig en1 ether "+macaddress)
os.system("sudo ifconfig en1 down")
os.system("sudo ifconfig en1 up")
