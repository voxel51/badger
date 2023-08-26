# 🦡 Badger - Custom Badges Made Easy 🌈

[![Badger Badge](https://img.shields.io/badge/Badger-blue.svg?style=flat&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiA/PjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgICA8IS0tIEJhY2tncm91bmQgLS0+CiAgICA8cmVjdCB4PSIwIiB5PSIwIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgZmlsbD0id2hpdGUiLz4KICAgIAogICAgPCEtLSBCYWRnZXIgQm9keSAtLT4KICAgIDxlbGxpcHNlIGN4PSIxMDAiIGN5PSIxMDAiIHJ4PSI4MCIgcnk9IjYwIiBmaWxsPSIjMDAwMDAwIi8+CiAgICAKICAgIDwhLS0gQmFkZ2VyIEZhY2UgLS0+CiAgICA8ZWxsaXBzZSBjeD0iMTAwIiBjeT0iMTAwIiByeD0iNTAiIHJ5PSI0MCIgZmlsbD0iI2ZmZmZmZiIvPgogICAgCiAgICA8IS0tIEJhZGdlciBTdHJpcGVzIC0tPgogICAgPHJlY3QgeD0iMjUiIHk9IjYwIiB3aWR0aD0iMTAiIGhlaWdodD0iODAiIGZpbGw9IndoaXRlIi8+CiAgICA8cmVjdCB4PSIxNjUiIHk9IjYwIiB3aWR0aD0iMTAiIGhlaWdodD0iODAiIGZpbGw9IndoaXRlIi8+CiAgICAKICAgIDwhLS0gQmFkZ2VyIEV5ZXMgLS0+CiAgICA8Y2lyY2xlIGN4PSI4MCIgY3k9IjkwIiByPSI1IiBmaWxsPSJ3aGl0ZSIvPgogICAgPGNpcmNsZSBjeD0iMTIwIiBjeT0iOTAiIHI9IjUiIGZpbGw9IndoaXRlIi8+CiAgICAKICAgIDwhLS0gRXllIEhpZ2hsaWdodHMgLS0+CiAgICA8Y2lyY2xlIGN4PSI4MiIgY3k9Ijg4IiByPSIxIiBmaWxsPSJ3aGl0ZSIvPgogICAgPGNpcmNsZSBjeD0iMTIyIiBjeT0iODgiIHI9IjEiIGZpbGw9IndoaXRlIi8+CiAgICAKICAgIDwhLS0gQmFkZ2VyIE5vc2UgLS0+CiAgICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMTAiIHI9IjUiIGZpbGw9IndoaXRlIi8+CiAgICAKICAgIDwhLS0gTm9zZSBIaWdobGlnaHQgLS0+CiAgICA8Y2lyY2xlIGN4PSIxMDIiIGN5PSIxMDgiIHI9IjEiIGZpbGw9IndoaXRlIi8+CiAgICAKICAgIDwhLS0gQmFkZ2VyIEVhcnMgLS0+CiAgICA8ZWxsaXBzZSBjeD0iNzAiIGN5PSI3MCIgcng9IjEwIiByeT0iMTUiIGZpbGw9IiMwMDAwMDAiLz4KICAgIDxlbGxpcHNlIGN4PSIxMzAiIGN5PSI3MCIgcng9IjEwIiByeT0iMTUiIGZpbGw9IiMwMDAwMDAiLz4KPC9zdmc+)](https://github.com/voxel51/badger)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://github.com/voxel51/badger/blob/main/LICENSE)

---

## 🚀 Introduction

Ever felt the need to spice up your GitHub README with cool badges, but found it too tedious? Want to personalize your badges to showcase your style? **Badger** is here to the rescue! 🎉

**Badger** is a Python CLI tool that allows you to generate custom badges for your GitHub README or any other markdown files. With a simple command, you can create, manage, and insert badges like a pro. 🌟

## 🌟 Features

- Create badges with custom text, colors, and logos 🎨
- Save badge configurations for future use 📂
- Generate badges on-the-fly and copy them to clipboard 📋
- List, delete, and manage your badges effortlessly 🛠

## 📦 Installation

Installing **Badger** is as simple as pie:

```bash
git clone https://github.com/voxel51/badger.git
cd badger
pip install -e .
```

## 📝 Usage

Here's how you can use Badger:

### 🏗️ Create a New Badge

```bash
badger create badge_name
```

This will walk you through a series of prompts to customize your badge.

```bash
badger create voxel51_ada
```

Begins the process of creating an ADA compliant badge for Voxel51 named `voxel51_ada`:

```plaintext
> Enter the URL the badge will point to: https://github.com/voxel51/fiftyone

> Enter the path to the logo file: https://gist.githubusercontent.com/jacobmarks/eb18cc90596f7310e4dad1be2526c070/raw/e05e51be697a9501f64fe8d1b7008fc5ebe56369/fiftyone_icon.svg

Commonly used colors:
1. brightgreen
2. green
3. yellowgreen
4. yellow
5. orange
6. red
7. blue
8. lightgrey
9. success
10. important
11. critical
12. informational
13. inactive

> Enter the color of the badge (or choose a number from the list above): blue

> Enter the text of the badge: Voxel51

> Enter the style of the badge (flat, flat-square, plastic, for-the-badge, social), or press Return to skip: flat

> Enter the logo color of the badge, or press Return to skip: white

> Successfully added badge 'voxel51_ada'.
```

💡 You can also create a badge from an SVG at a URL! If you do so, the content of the SVG will be retrieved at badge generation time using `requests`.

### 📋 Copy a Badge to Clipboard

```bash
badger copy badge_name
```

This copies the badge markdown to your clipboard. Paste it wherever you like!

For instance, we can copy the badge we just created:

```bash
badger copy voxel51_ada
```

[![voxel51 Badge](https://img.shields.io/badge/voxel51-blue.svg?style=flat&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiA/PjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiBpZD0iTGF5ZXJfMSIgeD0iMHB4IiB5PSIwcHgiIHZpZXdCb3g9IjAgMCA1MjAuNyA0NzIuNyIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgNTIwLjcgNDcyLjc7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4KPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KCS5zdDB7ZmlsbDp3aGl0ZTt9Cgkuc3Qxe2ZpbGw6d2hpdGU7fQo8L3N0eWxlPgo8ZyBpZD0ic3VyZmFjZTEiPgoJPHBhdGggY2xhc3M9InN0MCIgZD0iTTEyMC45LDQzLjJjMC0yLjIsMS4zLTMuNSwyLjItMy44YzAuNi0wLjMsMS4zLTAuNiwyLjItMC42YzAuNiwwLDEuNiwwLjMsMi4yLDAuNmwxMy43LDhMMTY3LjYsMzJsLTI2LjgtMTUuMyAgIGMtOS42LTUuNC0yMS4xLTUuNC0zMSwwYy05LjYsNS44LTE1LjMsMTUuNy0xNS4zLDI2Ljh2Mjg2LjNsMjYuMiwxNS4zdi0zMDJoMC4yVjQzLjJ6Ii8+Cgk8cGF0aCBjbGFzcz0ic3QwIiBkPSJNMTI3LjksNDI5LjZjLTEuOSwxLTMuOCwwLjYtNC41LDBjLTEtMC42LTIuMi0xLjYtMi4yLTMuOHYtMTUuN0w5NSwzOTQuN3YzMWMwLDExLjIsNS44LDIxLjEsMTUuMywyNi44ICAgYzQuOCwyLjksMTAuMiw0LjIsMTUuMyw0LjJjNS40LDAsMTAuNS0xLjMsMTUuMy00LjJMNDAyLDMwMS43di0zMC40TDEyNy45LDQyOS42eiIvPgoJPHBhdGggY2xhc3M9InN0MCIgZD0iTTQ3Mi40LDIwNy44bC0yNDgtMTQzLjJsLTI2LjUsMTVMNDU5LDIzMC41YzEuOSwxLjMsMi4yLDIuOSwyLjIsMy44cy0wLjMsMi45LTIuMiwzLjhsLTExLjgsNi43djMwLjQgICBsMjQuOS0xNC40YzkuNi01LjQsMTUuMy0xNS43LDE1LjMtMjYuOEM0ODcuNywyMjMuMSw0ODIsMjEzLjIsNDcyLjQsMjA3Ljh6Ii8+Cgk8cGF0aCBjbGFzcz0ic3QxIiBkPSJNNzkuNywzNjguNWwyMi43LDEzLjFsMjYuMiwxNS4zbDcuNyw0LjVsNS40LDMuMmw5NS41LTU1LjN2LTk1LjJjMC0xMi4xLDYuNC0yMy4zLDE2LjktMjkuNGw4Mi40LTQ3LjYgICBMMTkwLjIsOTIuOGwtMjIuNy0xMy4xbDIyLjctMTMuMWwyNi4yLTE1LjNsNy43LTQuNWw3LjcsNC41bDE2MSw5My4zbDMuMi0xLjljOS4zLTUuNCwyMS4xLDEuMywyMS4xLDEyLjF2My44bDE1LDguNlYxNDIgICBjMC0xMi41LTYuNy0yNC0xNy4zLTMwTDI1NC41LDE5LjNjLTEwLjktNi40LTI0LTYuNC0zNC44LDBMMTM2LDY3LjZ2MzAzLjJsLTIyLjctMTMuMUw4NywzNDIuM2wtNy4zLTQuMnYtMjM4bC0yMC4xLDExLjUgICBjLTEwLjksNi4xLTE3LjMsMTcuNi0xNy4zLDMwdjE4NWMwLDEyLjUsNi43LDI0LDE3LjMsMzBMNzkuNywzNjguNXoiLz4KCTxwYXRoIGNsYXNzPSJzdDEiIGQ9Ik00MTcuMSwyMjMuOHY5NC45YzAsMTIuMS02LjQsMjMuMy0xNi45LDI5LjRsLTE0MS45LDgyLjFjLTkuMyw1LjQtMjEuMS0xLjMtMjEuMS0xMi4xdi0zLjhMMTk3LjksNDM3ICAgbDIxLjcsMTIuNWMxMC45LDYuNCwyNCw2LjQsMzQuOCwwTDQxNC42LDM1N2MxMC45LTYuNCwxNy4zLTE3LjYsMTcuMy0zMHYtOTQuNkw0MTcuMSwyMjMuOHoiLz4KPC9nPgo8L3N2Zz4=)](https://github.com/voxel51/fiftyone)

### 🖨️ Print a Badge Markdown

```bash
badger print badge_name
```

Prints the badge markdown to the terminal.

### 📂 List All Badges

```bash
badger list
```

Lists all the badges you have created.

```plaintext
Available badges:
Badge Name           URL                                                Color                Text
--------------------------------------------------------------------------------------------------------------
badger               https://github.com/voxel51/badger                  blue                 Badger
voxel51_ada          https://github.com/voxel51/fiftyone                blue                 voxel51
voxel51              https://github.com/voxel51/fiftyone                blue                 voxel51
```

### 🗑️ Delete a Badge

```bash
badger delete badge_name
```

Deletes the badge from your config file.

### ✨ Go Wild!

```bash
badger go-wild
```

Generates a random badge using AI and copies it to your clipboard. 🤪 This takes a `--prompt` argument that allows you to specify the prompt to use for generating the badge.

For example:

```bash
badger go-wild --prompt turtle
```

Creates a trial badge for the turtle prompt.

[![Trial Badge](https://img.shields.io/badge/turtle-blue.svg?style=flat&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiIGlkPSJMYXllcl8xIiB4PSIwcHgiIHk9IjBweCIgdmlld0JveD0iMCAwIDEwMCAxMDAiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDEwMCAxMDA7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4KCTxnPgoJICA8Y2lyY2xlIHN0eWxlPSJmaWxsOiM1NThCMkY7IiBjeD0iNTAiIGN5PSI0MCIgcj0iMzUiLz4KCSAgPHBhdGggc3R5bGU9ImZpbGw6IzMzNjkxRTsiIGQ9Ik0yNSw0MGMwLTEzLjgsMTEuMi0yNSwyNS0yNXMyNSwxMS4yLDI1LDI1cy0xMS4yLDI1LTI1LDI1UzI1LDUzLjcsMjUsNDAgTTE1LDQwYzAsMTkuMzMsMTUuNjcsMzUsMzUsMzUgICBzMzUtMTUuNjcsMzUtMzVTNjkuMzMsNSw1MCw1UzE1LDIwLjY3LDE1LDQwIi8+CgkgIDxjaXJjbGUgc3R5bGU9ImZpbGw6I0ZGRkZGRjsiIGN4PSIzNyIgY3k9IjMzIiByPSI1Ii8+CgkgIDxjaXJjbGUgc3R5bGU9ImZpbGw6I0ZGRkZGRjsiIGN4PSI2MyIgY3k9IjMzIiByPSI1Ii8+CgkgIDxwYXRoIHN0eWxlPSJmaWxsOiMyMTIxMjE7IiBkPSJNNTAsNTNjLTYuNiwwLTEyLTUuNC0xMi0xMkg2MkM2Miw0Ny42LDU2LjYsNTMsNTAsNTN6Ii8+CgkgIDxjaXJjbGUgc3R5bGU9ImZpbGw6IzIxMjEyMTsiIGN4PSIzNyIgY3k9IjMzIiByPSIyIi8+CgkgIDxjaXJjbGUgc3R5bGU9ImZpbGw6IzIxMjEyMTsiIGN4PSI2MyIgY3k9IjMzIiByPSIyIi8+Cgk8L2c+Cjwvc3ZnPg==)](https://github.com/voxel51/badger)

You can then save the badge to your config file by entering `y` when prompted and follow the instructions to save the badge.

And:

```bash
badger go-wild --prompt flamingo
```

[![Trial Badge](https://img.shields.io/badge/flamingo-blue.svg?style=flat&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgPGRlZnM+CiAgICA8cmFkaWFsR3JhZGllbnQgaWQ9ImdyYWRpZW50IiBjeD0iNTAlIiBjeT0iNTAlIiByPSI1MCUiIGZ4PSI1MCUiIGZ5PSI1MCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdHlsZT0ic3RvcC1jb2xvcjpyZ2IoMjU1LDEwNSwxODApO3N0b3Atb3BhY2l0eToxIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0eWxlPSJzdG9wLWNvbG9yOnJnYigyNTUsMjAsMTQ3KTtzdG9wLW9wYWNpdHk6MSIgLz4KICAgIDwvcmFkaWFsR3JhZGllbnQ+CiAgPC9kZWZzPgogIDxlbGxpcHNlIGN4PSI1MCUiIGN5PSI1NSUiIHJ4PSI1MCIgcnk9IjYwIiBmaWxsPSJ1cmwoI2dyYWRpZW50KSIgLz4KICA8cGF0aCBkPSJNNjAsMzAgUTkwLDUwIDYwLDkwIFEzMCw1MCA2MCwzMCIgZmlsbD0id2hpdGUiIC8+CiAgPHBhdGggZD0iTTkwLDIwIFE2MCw0MCAzMCwyMCBUOTAsMjAiIGZpbGw9ImJsYWNrIiAvPgo8L3N2Zz4=)](https://github.com/voxel51/badger)

> 💡 This uses your OpenAI API Key to call GPT 4

### ❓ Get Help

```bash
badger help
```

Prints the help message.

### 🎨 Customization

- Custom Colors
- Custom Logos
- Custom Text
- Custom Styles
- ... and much more! 🌈

Once you have created a badge (added it to your config), you can work with modified versions of that badge incredibly easily using the following command line arguments, which can be passed along with the `copy` and `print` commands:

- `--color`: The color of the badge
- `--logo`: The logo color of the badge
- `--text`: The text of the badge
- `--style`: The style of the badge
- `--url`: The URL the badge points to

### Editing the Config File

You can also edit the config file directly to customize your badges. The config file is located at `~/.badger` and has the following format:

```yml
badges:
  badger:
    color: blue
    logo: /Users/jacobmarks/Desktop/work/badger/src/badger.svg
    logoColor: white
    text: Badger
    url: https://github.com/voxel51/badger
  voxel51_ada:
    color: blue
    logoColor: white
    logo: /Users/jacobmarks/Desktop/work/badger/src/fiftyone.svg
    text: voxel51
    url: https://github.com/voxel51/fiftyone
  voxel51:
    color: blue
    logo: https://gist.githubusercontent.com/jacobmarks/eb18cc90596f7310e4dad1be2526c070/raw/e05e51be697a9501f64fe8d1b7008fc5ebe56369/fiftyone_icon.svg
    text: voxel51
    url: https://github.com/voxel51/fiftyone
```

You can add, remove, and edit badges as you see fit. Badger will automatically detect changes to the config file and update your badges accordingly.

## 💡 Why You Absolutely Need This

- Saves Time: No need to manually write markdown or HTML for badges. 🕒
- Be Unique: Stand out from the crowd with personalized badges. 🦄
- Stay Organized: Keep all your badges in one place, ready to be used anytime. 🗂
- It's Cool: Because let's face it, who doesn't like badges? 😎
