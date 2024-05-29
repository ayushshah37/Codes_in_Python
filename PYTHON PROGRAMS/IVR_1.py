from freeswitch import *
import sys
import time


def handler(session,args):
        session.answer()
        session.setAutoHangup(False)
        session.set_tts_params("flite", "rms")


        while session.ready() == True:
                session.speak("Welcome user, please press 1 for the default I V R, press 2 to reach Juan, press 3 to reach Jesus, press 0 to exit")
                session.sleep(3000)
                dtmf = session.getDigits(1,"",3000)

                if dtmf == "1":
                        session.transfer("5000","XML", "default")

                elif dtmf == "2":
                        session.transfer("1002","XML","default")
                elif dtmf == "3":
                        session.transfer("1003","XML","default")
                elif dtmf == "0":
                        session.speak("Goodbye")
                        session.hangup("NORMAL_CLEARING")
                else:
                        session.speak("Invalid option")