import os
import sys
from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_file):
    # Check if file exists
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        return False

    # Check if file is mp4
    if not input_file.lower().endswith('.mp4'):
        print("Error: Please upload an mp4 file.")
        return False

    try:
        # Get the filename without extension
        filename = os.path.splitext(os.path.basename(input_file))[0]
        
        # Convert video to audio
        video = VideoFileClip(input_file)
        audio = video.audio
        
        # Save as mp3
        output_file = f"{filename}.mp3"
        audio.write_audiofile(output_file)
        
        # Close the video and audio objects
        audio.close()
        video.close()
        
        print(f"Conversion successful. Audio saved as '{output_file}'")
        return True
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        return False

def main():
    while True:
        input_file = input("Enter the path to the MP4 file (or 'q' to quit): ")
        
        if input_file.lower() == 'q':
            print("Exiting the program.")
            break

        success = convert_mp4_to_mp3(input_file)
        
        if success:
            print("You can now download the converted audio file.")
        
        print("\n")  # Add a newline for better readability

if __name__ == "__main__":
    main()
