import speech_recognition as sr

def command():
    recording = sr.Recognizer()
    with sr.Microphone() as source: 
        recording.adjust_for_ambient_noise(source)
        print("Yes! I'm ready, Start Speaking...")
        # while speaking, machine will take time of 0.6ms to transcript.
        # recording.pause_threshold = 0.6
        audio = recording.listen(source)

        try:
            speech = recording.recognize_google(audio, language= 'en-us')
            print(f"You said: {speech}")
        except Exception as e:
            print("I'm unable to understand. Speak Again, Please!",e)
            return ""
        
        return speech
    
command()