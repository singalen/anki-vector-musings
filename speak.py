import anki_vector


def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        while True:
            line = input()
            if not line:
                break
            robot.behavior.say_text(line)


if __name__ == "__main__":
    main()
