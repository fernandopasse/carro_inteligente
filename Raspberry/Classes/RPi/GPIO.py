# coding: utf-8
import random

DEBUG = True

BCM = 4
BOARD = 5

OUT = 2
IN = 1
HIGH = 1
LOW = 0

RISING = 1
FALLING = 2
BOTH = 3

PUD_OFF = 0
PUD_DOWN = 1
PUD_UP = 2

GPIO_NAMES = [
    "3v3", "5v",
    "GPIO2", "5V",
    "GPIO3", "GND",
    "GPIO4", "GPIO14",
    "GND", "GPIO15",
    "GPIO17", "GPIO18",
    "GPIO27", "GND",
    "GPIO22", "GPIO23",
    "3V3", "GPIO24",
    "GPIO10", "GND",
    "GPIO9", "GPIO25",
    "GPIO11", "GPIO8",
    "GND", "GPIO7",
    "I2C", "I2C",
    "GPIO5", "GND",
    "GPIO6", "GPIO12",
    "GPIO13", "GND",
    "GPIO19", "GPIO16",
    "GPIO26", "GPIO20",
    "GND", "GPIO21"
]


def setup(pin, mode, pull_up_down=PUD_OFF):
    if DEBUG:
        print "PINO %d, MODO: %s (setup)" % (pin, "OUT" if mode == 2 else "IN")
    else:
        raise NotImplementedError


def setmode(mode):
    if DEBUG:
        print "SETOU O MODO: %s (setmode)" % ("BOARD" if mode == 5 else "BCM")
    else:
        raise NotImplementedError


def output(pin, value):
    if DEBUG:
        print "PINO: %d, VALOR: %s (output)" % (pin, "LOW" if value else "HIGH")
    else:
        raise NotImplementedError

def input(pin):
        raise NotImplementedError


def set_high(pin):
    raise NotImplementedError


def set_low(pin):
    raise NotImplementedError


def is_high(pin):
    raise NotImplementedError


def is_low(pin):
    raise NotImplementedError


def output_pins(pins):
    raise NotImplementedError


def setup_pins(pins):
    raise NotImplementedError


def input_pins(pins):
    raise NotImplementedError


def add_event_detect(pin, edge):
    raise NotImplementedError


def remove_event_detect(pin):
    raise NotImplementedError


def add_event_callback(pin, callback):
    raise NotImplementedError


def event_detected(pin):
    raise NotImplementedError


def wait_for_edge(pin, edge):
    raise NotImplementedError


def cleanup(pin=None):
    raise NotImplementedError


def _validate_pin(pin):
    raise NotImplementedError
