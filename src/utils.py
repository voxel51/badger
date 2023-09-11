"""
| Badger Utils.
| Copyright 2017-2023, Voxel51, Inc.
| `voxel51.com <https://voxel51.com/>`_
|
"""

import base64
import os
from xml.dom import minidom


def list_badges(badges):
    """
    List available badges in a formatted manner.
    """
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


def print_badge_info(badge_name, config):
    """
    Print the details of the given badge.
    """
    # Check if the badge exists
    if badge_name not in config:
        print(f"No badge found with the name '{badge_name}'.")
        return

    badge_config = config[badge_name]
    print(f"Badge: {badge_name}")
    print("-" * 110)

    props = [
        ("URL", "url"),
        ("Color", "color"),
        ("Text", "text"),
        ("Logo", "logo"),
        ("Style", "style"),
        ("Label", "label"),
        ("Label Color", "labelColor"),
        ("Logo Width", "logoWidth"),
        ("Logo Color", "logoColor"),
    ]

    for prop in props:
        print(f"{prop[0]}: {badge_config.get(prop[1], 'N/A')}")


def change_svg_color(svg_data, new_color="#000000"):
    """
    Change the color attributes in the given SVG data.
    """
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
    # Validate and fetch URL and logo details
    url = badge_config.get("url", "N/A")
    logo_file_or_url = badge_config.get("logo", "N/A")

    if not url.startswith("http"):
        print(f"Invalid URL '{url}'.")
        return

    if logo_file_or_url == "N/A":
        print("No logo file or URL provided.")
        return

    # Fetch the SVG data
    if logo_file_or_url.startswith("http://") or logo_file_or_url.startswith(
        "https://"
    ):
        import requests

        response = requests.get(logo_file_or_url)
        svg_data = response.text
    else:
        logo_file = os.path.expanduser(logo_file_or_url)
        if not os.path.exists(logo_file):
            print(f"Logo file '{logo_file}' not found.")
            return
        with open(logo_file, "r") as svg_file:
            svg_data = svg_file.read()

    # Change SVG color if needed
    if badge_config.get("logoColor"):
        svg_data = change_svg_color(svg_data, badge_config["logoColor"])

    # Base64 encode the SVG
    if isinstance(svg_data, str):
        svg_data = svg_data.encode("utf-8")
    b64_logo = base64.b64encode(svg_data).decode("ascii")

    # Dynamic URL construction
    base_url = "https://img.shields.io/badge/"
    badge_text = badge_config.get("text", "N/A").replace(" ", "%20").strip()
    color = badge_config.get("color", "blue")

    badge_url = f"{base_url}{badge_text}-{color}.svg?"

    optional_keys = [
        "style",
        "label",
        "labelColor",
        "logoWidth",
        "logoPosition",
    ]
    optional_params = [f"logo=data:image/svg+xml;base64,{b64_logo}"]

    for key in optional_keys:
        value = badge_config.get(key)
        if value:
            optional_params.append(f"{key}={value}")

    badge_url += "&".join(optional_params)

    # Generate Markdown
    badge_markdown = f"[![{badge_text} Badge]({badge_url})]({url})"

    return badge_markdown


def save_svg_file(svg_data):
    file_name = input("Enter the filename to save as: ")
    file_name = f"{os.path.expanduser(file_name)}"
    if ".svg" not in file_name:
        file_name += ".svg"
    with open(file_name, "w") as f:
        if isinstance(svg_data, bytes):
            f.write(svg_data.decode("utf-8"))
        else:
            f.write(svg_data)
    print(f"SVG saved as {file_name}")
    return file_name


def save_as_badge(file_name, config):
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
        "logo": file_name,
        "url": badge_url,
        "style": badge_style,
        "logoColor": badge_logo_color,
    }

    badges = config.load_config()
    badges[badge_name] = new_badge
    config.update_config(badges)

    print(f"New badge '{badge_name}' has been saved.")


def extract_name_from_github(username):
    import requests
    from bs4 import BeautifulSoup

    # Fetch the HTML content of the GitHub profile
    url = f"https://github.com/{username}"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the tag containing the user's name
        name_tag = soup.find(
            "span", {"class": "p-name vcard-fullname d-block overflow-hidden"}
        )

        if name_tag:
            # Extract and print the name
            name = name_tag.text.strip()
            return name
        else:
            return None
    else:
        return None
