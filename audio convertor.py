from pydub import AudioSegment

def convert_audio(input_file, output_files, output_formats):
    audio = AudioSegment.from_file(input_file)
    for i in range(len(output_formats)):
        audio.export(output_files[i], format=output_formats[i])

input_file = "C:\Users\ibmtr\Desktop\20projects\Audio format convertor\leva.mp3"  # Path to the input audio file
output_files = ["output2.wav"]  # List of output audio files
output_formats = ["wav"]  # List of desired output formats

convert_audio(input_file, output_files, output_formats)
