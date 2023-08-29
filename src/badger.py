"""
| Badger CLI.
| Copyright 2017-2023, Voxel51, Inc.
| `voxel51.com <https://voxel51.com/>`_
|
"""

import argparse
import base64
import os
import re
import pyperclip
import yaml
from xml.dom import minidom

BADGER_CONFIG_FILE = os.environ.get("BADGER_CONFIG_FILE", "~/.badger")


RANDOM_SVG_PROMPT = """
Generate a detailed, high-quality SVG logo of a SUBJECT with proper XML 
formatting. Make sure to include the XML header, and keep the design simple but 
visually appealing. The SVG should be suitable for use as a badge logo. Include 
some details in the design, so that it stands out from other badges. Only return
the SVG data and XML header, not any explanatory text. The badge should NOT have
any text in it, as that will be added later.
"""

FIX_BADGE_PROMPT = """
Turn the text below into a working SVG code for SUBJECT. The SVG code should be 
properly formatted and include the XML header. The badge should NOT have any 
text in it, as that will be added later. Just return the SVG data and XML 
header, not any explanatory text. You will be penalized if the SVG code is not
properly formatted, or if it contains any text. The text to correct is:\n\n
"""

# Function to create a default config file with a 'badger' badge
def create_default_config(file_path):
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Build the path to badger.svg relative to the script's location
    badger_svg_path = os.path.join(script_dir, "../assets/badger.svg")

    default_badge = {
        "badger": {
            "url": "https://github.com/voxel51/badger",
            "color": "blue",
            "logo": badger_svg_path,
            "text": "Badger",
            "logoColor": "white",
        }
    }

    with open(file_path, "w") as file:
        yaml.safe_dump({"badges": default_badge}, file)

    print(f"Created default config file at {file_path}")


def parse_badger_file():
    with open(BADGER_CONFIG_FILE, "r") as file:
        config = yaml.safe_load(file)
        return config.get("badges", {})


def add_badge_to_config(badge_name, badge_data):
    try:
        with open(BADGER_CONFIG_FILE, "r") as file:
            config = yaml.safe_load(file)
            if config is None:
                config = {"badges": {}}
            elif "badges" not in config:
                config["badges"] = {}
        config["badges"][badge_name] = badge_data

        with open(BADGER_CONFIG_FILE, "w") as file:
            yaml.safe_dump(config, file)

        print(f"Successfully added badge '{badge_name}'.")

    except Exception as e:
        print(f"An error occurred: {e}")


def delete_badge_from_config(badge_name):
    try:
        with open(BADGER_CONFIG_FILE, "r") as file:
            config = yaml.safe_load(file)
            if (
                config
                and "badges" in config
                and badge_name in config["badges"]
            ):
                del config["badges"][badge_name]

        with open(BADGER_CONFIG_FILE, "w") as file:
            yaml.safe_dump(config, file)

        print(f"Successfully deleted badge '{badge_name}'.")

    except Exception as e:
        print(f"An error occurred: {e}")


def list_badges(badges):
    print("Available badges:")
    print(
        "{:<20} {:<50} {:<20} {:<20}".format(
            "Badge Name", "URL", "Color", "Text"
        )
    )
    print("-" * 110)

    for badge_name, args in badges.items():
        url = args.get("url", "N/A")
        color = args.get("color", "N/A")
        text = args.get("text", "N/A")
        print(
            "{:<20} {:<50} {:<20} {:<20}".format(badge_name, url, color, text)
        )


def change_svg_color(svg_data, new_color="#000000"):
    doc = minidom.parseString(svg_data)

    # Handle fill attributes
    for element_name in ["path", "circle", "rect", "g"]:
        for element in doc.getElementsByTagName(element_name):
            if element.hasAttribute("fill"):
                element.setAttribute("fill", new_color)

    # Handle style tags
    for style in doc.getElementsByTagName("style"):
        css_text = style.firstChild.nodeValue  # Assuming it contains text
        new_css_text = css_text.replace(
            ".st0{fill:#FF6D00;}", f".st0{{fill:{new_color};}}"
        )  # Replace the color for class .st0
        new_css_text = new_css_text.replace(
            ".st1{fill:#9B9B9B;}", f".st1{{fill:{new_color};}}"
        )  # Replace the color for class .st1
        style.firstChild.replaceWholeText(new_css_text)

    return doc.toxml()


def generate_badge_markdown(badge_config):
    text = badge_config.get("text", "N/A")
    color = badge_config.get("color", "blues")
    logo_file_or_url = badge_config.get("logo", "N/A")
    url = badge_config.get("url", "N/A")
    style = badge_config.get("style", "flat")
    logo_color = badge_config.get("logoColor", None)

    if not url.startswith("http"):
        print(f"Invalid URL '{url}'.")
        return
    if logo_file_or_url == "N/A":
        print("No logo file or URL provided.")
        return

    # Check if it's a URL or a local file
    if logo_file_or_url.startswith("http://") or logo_file_or_url.startswith(
        "https://"
    ):
        # Fetch the SVG from the URL
        import requests

        response = requests.get(logo_file_or_url)
        svg_data = response.text
    else:
        logo_file = os.path.expanduser(logo_file_or_url)
        if not os.path.exists(logo_file):
            print(f"Logo file '{logo_file}' not found.")
            return
        # Read the SVG from a local file
        with open(logo_file, "r") as svg_file:
            svg_data = svg_file.read()

    if logo_color:
        svg_data = change_svg_color(svg_data, logo_color)

    if isinstance(svg_data, str):
        svg_data = svg_data.encode("utf-8")
    # Encode in base64 and decode it to ASCII
    b64_logo = base64.b64encode(svg_data).decode("ascii")

    badge_text = text.replace(" ", "%20").strip()

    badge_pattern = (
        f"[![{text} Badge](https://img.shields.io/badge/{badge_text}-{color}.svg?"
        f"style={style}&logo=data:image/svg+xml;base64,{b64_logo})]({url})"
    )
    return badge_pattern


def generate_random_svg(subject):
    import openai

    openai.api_key = os.getenv("OPENAI_API_KEY")
    print("Calling the OpenAI API... (this may take a few seconds)")
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": RANDOM_SVG_PROMPT.replace("SUBJECT", subject),
            },
        ],
    )
    response = completion.choices[0].message["content"]

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": FIX_BADGE_PROMPT.replace("SUBJECT", subject)
                + response,
            },
        ],
    )
    response = completion.choices[0].message["content"]

    svg = response.replace('\\"', '"').replace("\\n", "\n").strip()
    svg = re.search(r"<svg.*?</svg>", svg, re.DOTALL)
    if svg:
        return svg.group(0).encode("utf-8")
    else:
        print("GPT-3.5 failed to generate a valid SVG. Please try again.")
        return


def generate_trial_badge(svg_data, subject):
    # Encode in base64 and decode it to ASCII
    b64_logo = base64.b64encode(svg_data).decode("ascii")

    subject = subject.replace(" ", "%20").strip()

    badge_pattern = (
        f"[![Trial Badge](https://img.shields.io/badge/{subject}-blue.svg?"
        f"style=flat&logo=data:image/svg+xml;base64,{b64_logo})](https://github.com/voxel51/badger)"
    )
    return badge_pattern


def main():
    parser = argparse.ArgumentParser(
        description="Manage custom badges for GitHub READMEs."
    )
    subparsers = parser.add_subparsers(dest="command")

    create_parser = subparsers.add_parser("create", help="Create a new badge.")
    create_parser.add_argument(
        "badge_name", nargs="?", default=None, help="Name of the new badge."
    )

    delete_parser = subparsers.add_parser("delete", help="Delete a badge.")
    delete_parser.add_argument(
        "badge_name", help="Name of the badge to delete."
    )

    copy_parser = subparsers.add_parser(
        "copy", help="Copy badge Markdown to clipboard."
    )
    copy_parser.add_argument("badge_name", help="Name of the badge to copy.")
    copy_parser.add_argument("--text", help="Text override.")
    copy_parser.add_argument("--color", help="Color override.")
    copy_parser.add_argument("--logo", help="Logo file override.")
    copy_parser.add_argument("--url", help="URL override.")
    copy_parser.add_argument("--style", help="Style override.")
    copy_parser.add_argument("--logoColor", help="Logo color override.")

    print_parser = subparsers.add_parser(
        "print", help="Print badge Markdown to terminal."
    )
    print_parser.add_argument("badge_name", help="Name of the badge to print.")
    print_parser.add_argument("--text", help="Text override.")
    print_parser.add_argument("--color", help="Color override.")
    print_parser.add_argument("--logo", help="Logo file override.")
    print_parser.add_argument("--url", help="URL override.")
    print_parser.add_argument("--style", help="Style override.")
    print_parser.add_argument("--logoColor", help="Logo color override.")

    go_wild_parser = subparsers.add_parser(
        "go-wild", help="Generate a random SVG badge."
    )
    go_wild_parser.add_argument(
        "--prompt", help="Subject of the SVG to generate.", default="badger"
    )

    subparsers.add_parser("list", help="List available badges.")
    subparsers.add_parser("help", help="List available commands.")

    args = parser.parse_args()

    badges = parse_badger_file()

    if args.command in ["copy", "print"]:
        if args.badge_name in badges:
            badge_config = badges[args.badge_name]
            # Override the defaults with any provided command line arguments
            for key in ["text", "color", "logo", "url", "style", "logoColor"]:
                if getattr(args, key, None):
                    badge_config[key] = getattr(args, key)

            badge_markdown = generate_badge_markdown(badge_config)

            if args.command == "copy":
                pyperclip.copy(badge_markdown)
                print(f"Copied badge '{args.badge_name}' to clipboard.")
            elif args.command == "print":
                print(badge_markdown)
        else:
            print(f"Badge '{args.badge_name}' not found.")

    elif args.command == "list":
        list_badges(badges)

    elif args.command == "help":
        parser.print_help()

    elif args.command == "create":
        badge_name = (
            args.badge_name
            if args.badge_name
            else input("Enter the name of the new badge: ")
        )
        # Check for duplicate badge name
        while badge_name in badges:
            overwrite = input(
                f"A badge with the name '{badge_name}' already exists. Do you want to overwrite it? (y/n): "
            ).lower()
            if overwrite == "y":
                break
            elif overwrite == "n":
                badge_name = input("Enter a new name for the badge: ")
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        url = input("Enter the URL the badge will point to: ")
        logo = input("Enter the path to the logo file: ")
        # List of common colors and semantic labels
        common_colors = [
            "brightgreen",
            "green",
            "yellowgreen",
            "yellow",
            "orange",
            "red",
            "blue",
            "lightgrey",
            "success",
            "important",
            "critical",
            "informational",
            "inactive",
        ]
        print("Commonly used colors:")
        for i, color in enumerate(common_colors, 1):
            print(f"{i}. {color}")

        color_choice = input(
            "Enter the color of the badge (or choose a number from the list above): "
        )

        # If the user enters a number, map it to the corresponding color
        if color_choice.isdigit():
            color_choice = int(color_choice) - 1
            if 0 <= color_choice < len(common_colors):
                color = common_colors[color_choice]
            else:
                print("Invalid choice, using default color 'blue'.")
                color = "blue"
        else:
            color = color_choice
        text = input("Enter the text of the badge: ")
        style = input(
            "Enter the style of the badge (flat, flat-square, plastic, for-the-badge, social), or press Return to skip: "
        )
        logo_color = input(
            "Enter the logo color of the badge, or press Return to skip: "
        )

        new_badge_data = {
            "url": url,
            "color": color,
            "text": text,
            "style": style,
            "logoColor": logo_color,
            "logo": logo,
        }
        add_badge_to_config(badge_name, new_badge_data)

    elif args.command == "delete":
        # Confirmation prompt
        confirmation = input(
            f"Are you sure you want to delete the badge '{args.badge_name}'? (y/n): "
        ).lower()
        if confirmation == "y":
            delete_badge_from_config(args.badge_name)
        elif confirmation == "n":
            print("Operation cancelled.")
        else:
            print("Invalid input. Operation cancelled.")

    elif args.command == "go-wild":
        try:
            import openai
        except ImportError:
            print(
                "The openai package is not installed. Please install it by running 'pip install openai'"
            )
            return

        if not os.getenv("OPENAI_API_KEY"):
            print("Please set the OPENAI_API_KEY environment variable.")
            return

        svg_data = generate_random_svg(args.prompt)
        if not svg_data:
            return
        # Copy to clipboard
        pyperclip.copy(generate_trial_badge(svg_data, args.prompt))

        # pyperclip.copy(svg_data)

        print("SVG code has been copied to your clipboard.")

        save_option = input("Do you want to save this SVG? (y/n): ")
        if save_option.lower() == "y":
            file_name = input(
                "Enter the filename to save as (without extension): "
            )
            file_name = f"{os.path.expanduser(file_name)}.svg"
            with open(file_name, "w") as f:
                if isinstance(svg_data, bytes):
                    f.write(svg_data.decode("utf-8"))
                else:
                    f.write(svg_data)
            print(f"SVG saved as {file_name}")

            # Walk the user through the steps to save this as a badge
            print("Let's save this as a badge.")

            badge_name = input("Enter a name for this badge: ")
            badge_text = input("Enter the badge text: ")
            badge_color = input("Enter the badge color: ")
            badge_url = input("Enter the badge URL: ")
            badge_style = input(
                "Enter the badge style (flat, flat-square, plastic, for-the-badge, social): "
            )
            badge_logo_color = input("Enter the badge logo color: ")

            new_badge = {
                "text": badge_text,
                "color": badge_color,
                "logo": f"{file_name}",
                "url": badge_url,
                "style": badge_style,
                "logoColor": badge_logo_color,
            }

            with open(BADGER_CONFIG_FILE, "r") as file:
                config = yaml.safe_load(file)
            config["badges"][badge_name] = new_badge
            with open(BADGER_CONFIG_FILE, "w") as file:
                yaml.safe_dump(config, file)

            print(f"New badge '{badge_name}' has been saved.")


if __name__ == "__main__":
    main()
