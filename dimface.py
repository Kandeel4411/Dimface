#! /usr/bin/env python3
import pathlib as pl
import time

import click
import cv2
import wmi

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
@click.pass_context
def dimface(ctx):
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

    face_cascade = cv2.CascadeClassifier(
        str(BASE_DIR / pl.Path('haarcascade_frontalface_default.xml')))

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            1.3, 5
        )

        wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[
            0].WmiSetBrightness(0 if len(faces) == 0 else 100, 0)

        time.sleep(seconds)

    video_capture.release()


if __name__ == "__main__":
    dimface()
