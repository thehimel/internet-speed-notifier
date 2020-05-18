
from win10toast import ToastNotifier

# Custom Modules
from tts import text_to_speech
from console import log
from date_time import date_time

toaster = ToastNotifier()


def notify(download_speed, upload_speed):
    download_speed = str(download_speed)
    upload_speed = str(upload_speed)
    description = f'Download Speed: {download_speed} MBPS\nUpload Speed: {upload_speed} MBPS'

    title = 'Internet Speed'

    # While in fullscreen mode, notifaction doesn't work in Windows
    # Convert text to speech and play the text
    text_to_speech(description)

    # Print as Windows 10 notification
    toaster.show_toast(title, description)

    # Print in the colsole
    log(f'\nTime: {date_time()}\n{description}')
