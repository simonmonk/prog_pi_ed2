from Adafruit_7Segment import SevenSegment
import time, datetime
import RPi.GPIO as GPIO

switch_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
disp = SevenSegment(address=0x70)

time_mode, seconds_mode, date_mode = range(3)
disp_mode = time_mode

def display_time():
    # Get the time by separate parts for the clock display
    now = datetime.datetime.now()
    hour = now.hour    
    minute = now.minute
    second = now.second
    # Set hours
    disp.writeDigit(0, int(hour / 10))     # Tens
    disp.writeDigit(1, hour % 10)          # Ones
    # Set minutes
    disp.writeDigit(3, int(minute / 10))   # Tens
    disp.writeDigit(4, minute % 10)        # Ones
    # Toggle colon
    disp.setColon(second % 2)              # Toggle colon at 1Hz

def disply_date():
    now = datetime.datetime.now()
    month = now.month    
    day = now.day
    # Set month
    disp.writeDigit(0, int(month / 10))     # Tens
    disp.writeDigit(1, month % 10)          # Ones
    # Set day
    disp.writeDigit(3, int(day / 10))   # Tens
    disp.writeDigit(4, day % 10)        # Ones

def display_seconds():
    now = datetime.datetime.now()
    secs = now.second    
    disp.writeDigitRaw(0, 0);
    disp.writeDigitRaw(1, 0);
    disp.writeDigit(3, int(secs / 10))     # Tens
    disp.writeDigit(4, secs % 10)          # Ones

while True:
    key_pressed = not GPIO.input(switch_pin)
    if key_pressed:
        disp_mode = disp_mode + 1
        if disp_mode > date_mode:
            disp_mode = time_mode
            time.sleep(0.2)
    if disp_mode == time_mode:
        display_time()
    elif disp_mode == seconds_mode:
        display_seconds()
    elif disp_mode == date_mode:
        disply_date()
    time.sleep(0.1)
    
