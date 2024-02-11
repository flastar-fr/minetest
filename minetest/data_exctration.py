""" Data Manager File """
from json import load
from moviepy.editor import VideoFileClip, ImageSequenceClip


def read_json_file(file_path: str) -> {}:
    """ Function to read a json file
        :param file_path: str -> data json file path

        :return json file output
    """
    with open(file_path, "r", encoding="utf-8") as file_reader:
        file = load(file_reader)
    return file


def reduce_frame_rate(video_file: str, target_fps: int) -> ImageSequenceClip:
    """ Function to reduce the video frame rate
        :param video_file: str -> video file path
        :param target_fps: int -> FPS to get in the video

        :return ImageSequenceClip -> video in 3 FPS
    """
    video = VideoFileClip(video_file)

    frames_to_keep = int(video.duration * target_fps)

    selected_frames = []
    for i, frame in enumerate(video.iter_frames()):
        if i % (video.fps / target_fps) == 0:
            selected_frames.append(frame)
            if len(selected_frames) == frames_to_keep:
                break

    reduced_video = ImageSequenceClip(selected_frames, fps=target_fps)

    return reduced_video
