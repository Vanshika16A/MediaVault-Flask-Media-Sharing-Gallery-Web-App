def create_video(image_list, audio_flag, audio_file, fps=25):
    import cv2
    from moviepy.editor import VideoClip, concatenate_videoclips

    # frame_list = []
    # for image_path in image_list:
    #     frame = cv2.imread(image_path)
    #     frame_list.append(frame)
    first_image = cv2.imread(image_list[0])
    height, width, _ = first_image.shape

    # Initialize an array to store resized frames
    resized_frames = []

    # Resize images and store in resized_frames
    for image_path in image_list:
        frame = cv2.imread(image_path)
        resized_frame = cv2.resize(frame, (width, height))
        resized_frames.append(resized_frame)

    # Calculate duration and frame rate
    duration = len(image_list) / fps

    # Create video_clip from frames
    def make_frame(t):
        idx = int(t * fps)
        if idx < len(resized_frames):
            return resized_frames[idx]
        else:
            return resized_frames[-1]  # If time exceeds video duration, repeat the last frame

    video_clip = VideoClip(make_frame, duration=duration)
    
    # Calculate duration and frame rate
    duration = len(image_list) / fps

    # Create video_clip from frames
    video_clip = VideoClip(lambda t: resized_frames[int(t * fps)], duration=duration)
    
    # Set fps attribute
    video_clip.fps = fps

    if audio_flag:
        from moviepy.editor import AudioFileClip
        audio_clip = AudioFileClip(audio_file)
        video_clip = video_clip.set_audio(audio_clip)

    # Write video_clip to file
    output_video_path = 'output_video6.mp4'
    video_clip.write_videofile(output_video_path, codec='libx264')

   
    return output_video_path,

# Example usage:
image_list = ['/home/dexter/Pictures/stock/2Untitled.jpeg', '/home/dexter/Pictures/stock/3Untitled.jpeg', '/home/dexter/Pictures/stock/best-cool-luminous-fox-40lkhq7b7tl3p1qw.jpg']
audio_flag = True
audio_file = '/home/dexter/Downloads/OneDrive_1_23-2-2024/151.mp3'
fps = 25  # Adjust the frame rate as needed

output_video_path= create_video(image_list, audio_flag, audio_file, fps)
print("Output video path:", output_video_path)

