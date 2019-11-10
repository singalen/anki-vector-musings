import anki_vector
import anki_vector.util
from pathlib import Path
import os


def play_mp3(mp3_path):
    wav_filename = Path('wav/' + Path(mp3_path).name + '.wav').absolute()

    if not wav_filename.exists():
        status = os.system('ffmpeg -i "{}" -ac 1 -ar 16025 -sample_fmt s16 "{}"'.format(mp3_path, wav_filename))
        if status != 0:
            return

    print('converted')

    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        robot.behavior.say_text("Let's play some music!")
        robot.audio.stream_wav_file(str(wav_filename))


if __name__ == "__main__":
    play_mp3('/Users/vic/Music/GLMV/Angel of darkness.mp3')
