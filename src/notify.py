
from win10toast import ToastNotifier
from playsound import playsound

# Custom Modules
from tts import text_to_speech
from console import log
from date_time import date_time


def special_notification(result, args):
    happy_audio = './files/piece-of-cake.mp3'
    sad_audio = './files/martian-gun.mp3'

    # Special notifcation for download speed
    if result['downloadSpeed'] >= args.dupper:
        playsound(happy_audio)

    elif result['downloadSpeed'] <= args.dlower:
        playsound(sad_audio)

    # Special notifcation for upload speed
    if result['uploadSpeed'] >= args.uupper:
        playsound(happy_audio)

    elif result['uploadSpeed'] <= args.ulower:
        playsound(sad_audio)


def notify(result, args):
    # Make special, voice and toast True by default as initially args.nospecial, args.novoice and args.notoast are False
    special = not args.nospecial
    voice = not args.novoice
    toast = not args.notoast

    if special is True:
        special_notification(result, args)

    download_speed = str(result['downloadSpeed'])
    upload_speed = str(result['uploadSpeed'])
    description = f'Download Speed: {download_speed} MBPS\nUpload Speed: {upload_speed} MBPS'

    title = 'Internet Speed'

    # While in fullscreen mode, notifaction doesn't work in Windows
    # Convert text to speech and play the text
    if voice is True:
        text_to_speech(description)

    # Print as Windows 10 notification
    if toast is True:
        toaster = ToastNotifier()
        toaster.show_toast(title, description)

    # Print in the colsole
    log(f'\nTime: {date_time()}\n{description}')
