import numpy as np
import sounddevice as sd

mood_frequencies = {
    "happy": 432,
    "relaxed": 528,
    "focused": 963,
    "sleepy": 174,
    "stressed": 285,
    "sad": 396,
    "energetic": 639,
    "meditative": 741,
    "confident": 852,
    "creative": 417,
    "anxious": 432,
    "angry": 528,
    "lonely": 639,
    "overwhelmed": 285,
    "motivated": 852, 
}

def oscillate(frequency,duration, sample_rate = 44100):
    print(duration)
    samples = int(duration*sample_rate)
    amplitude = 0.5
    time = np.linspace(0,duration,samples,False)
    wave = amplitude*np.sin(2*np.pi*frequency*time)

    fade_samples = int(0.5 * sample_rate) 
    envelope = np.ones(samples)
    envelope[:fade_samples] = np.linspace(0, 1, fade_samples) 
    envelope[-fade_samples:] = np.linspace(1, 0, fade_samples)
    wave *= envelope 
    sd.play(wave,sample_rate)
    sd.wait()

while True:
    mood = input('How are you feeling? (happy/relaxed/focused/sleepy/anxious/energetic/meditative/confident/creative/angry/lonely/overwhelmed/motivated/sad/tired/stressed) or "quit" to exit): ').lower().strip()
    if mood == "quit":
        print("Bye")
        break
    elif mood in mood_frequencies:
        print(f'Playing {mood_frequencies[mood]} Hz to improve your mood.. please use headphones!')
        oscillate(mood_frequencies[mood],10)
    else:
        print("Sorry, I don't recognize your mood")


