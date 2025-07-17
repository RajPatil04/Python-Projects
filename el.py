from gtts import gTTS

# Script text
text = """
Black holes — the universe's most enigmatic creations, where gravity rules supreme and light itself cannot escape.
These cosmic giants are born from the explosive death of massive stars, collapsing into a point of infinite density known as a singularity.
Around them lies the event horizon — the point of no return. Cross it, and even time seems to lose meaning.
Black holes don’t just destroy; they shape the universe. They warp space, bend light, and fuel some of the brightest events in the cosmos.
So, what secrets do they hold? What mysteries lie beyond the event horizon?
Join us as we unravel the mysteries of these cosmic marvels — black holes.
"""

# Generate speech
speech = gTTS(text, lang="en", slow=False)

# Save the speech to an MP3 file
speech.save("Black_Hole_Introduction1.mp3")
print("Speech saved as 'Black_Hole_Introduction1.mp3'")
