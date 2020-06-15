#! /usr/bin/env python3
import pathlib as pl
import time

import click
import cv2
import wmi
from pynput import mouse

BASE_DIR = pl.Path(__file__).parent


######################################
###        Starting command        ###
######################################
@click.group(
    help=click.style(
        "A script to dim the screen brightness if no face is detected on the screen to save battery power",
        fg="yellow",
    ),
)
def dimface():
    pass


#######################################
####       Command:  dimface run    ###
#######################################
@dimface.command(help=click.style("Runs the script with frames taken each n seconds", fg="yellow"))
@click.option(
    "--seconds", type=int, required=True,
)
def run(seconds):
    click.secho("Running..", fg="green")

    # Opening web camera and loading face classifier
    face_cascade = cv2.CascadeClassifier(
        str(BASE_DIR / pl.Path('haarcascade_frontalface_default.xml')))
    video_capture = cv2.VideoCapture(0)

    # Flag to check if screen is bright or not
    bright = True

    while True:
        with mouse.Events() as events:
            try:

                # Blocks thread until a mouse event is recieved within (seconds)
                # else it throws an Exception
                event = events.get(seconds)

            # CTRL+C was pressed
            except KeyboardInterrupt:
                click.secho("Exiting..", fg="red")
                video_capture.release()
                break

            # No mouse event was detected - proceeds to detect face
            except Exception as e:
                if face_detected(face_cascade, video_capture):
                    if not bright:
                        change_brightness(brightness=100)
                        bright = True
                else:
                    if bright:
                        change_brightness(brightness=0)
                        bright = False

            # Mouse event was detected - sleeps for (seconds) instead
            else:
                if not bright:
                    change_brightness(brightness=100)
                    bright = True
                time.sleep(seconds)


def face_detected(face_cascade, video_capture):
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        1.3, 5
    )
    return len(faces) != 0


def change_brightness(brightness):
    wmi.WMI(namespace="wmi").WmiMonitorBrightnessMethods()[
        0].WmiSetBrightness(brightness, 0)


if __name__ == "__main__":
    dimface()
