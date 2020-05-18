
from win10toast import ToastNotifier

# Custom Modules
from tts import text_to_speech

toaster = ToastNotifier()


def notify(download_speed, upload_speed):
    download_speed = str(download_speed)
    upload_speed = str(upload_speed)
    description = f'Download Speed: {download_speed} MBPS\nUpload Speed: {upload_speed} MBPS'

    title = 'Internet Speed'

    # Print in the colsole
    # print('{0}\n{1}'.format(title, description))

    # While in fullscreen mode, notifaction doesn't work in Windows
    # Convert text to speech and play the text
    text_to_speech(description)

    # Print as Windows 10 notification
    toaster.show_toast(title, description)
