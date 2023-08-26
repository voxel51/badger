# 🦡 Badger - Custom Badges Made Easy 🌈

[![Badger Badge](https://img.shields.io/badge/Badger-blue.svg?style=flat&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiA/PjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+CiAgICA8IS0tIEJhY2tncm91bmQgLS0+CiAgICA8cmVjdCB4PSIwIiB5PSIwIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgZmlsbD0id2hpdGUiLz4KICAgIAogICAgPCEtLSBCYWRnZXIgQm9keSAtLT4KICAgIDxlbGxpcHNlIGN4PSIxMDAiIGN5PSIxMDAiIHJ4PSI4MCIgcnk9IjYwIiBmaWxsPSIjMDAwMDAwIi8+CiAgICAKICAgIDwhLS0gQmFkZ2VyIEZhY2UgLS0+CiAgICA8ZWxsaXBzZSBjeD0iMTAwIiBjeT0iMTAwIiByeD0iNTAiIHJ5PSI0MCIgZmlsbD0iI2ZmZmZmZiIvPgogICAgCiAgICA8IS0tIEJhZGdlciBTdHJpcGVzIC0tPgogICAgPHJlY3QgeD0iMjUiIHk9IjYwIiB3aWR0aD0iMTAiIGhlaWdodD0iODAiIGZpbGw9IndoaXRlIi8+CiAgICA8cmVjdCB4PSIxNjUiIHk9IjYwIiB3aWR0aD0iMTAiIGhlaWdodD0iODAiIGZpbGw9IndoaXRlIi8+CiAgICAKICAgIDwhLS0gQmFkZ2VyIEV5ZXMgLS0+CiAgICA8Y2lyY2xlIGN4PSI4MCIgY3k9IjkwIiByPSI1IiBmaWxsPSJ3aGl0ZSIvPgogICAgPGNpcmNsZSBjeD0iMTIwIiBjeT0iOTAiIHI9IjUiIGZpbGw9IndoaXRlIi8+CiAgICAKICAgIDwhLS0gRXllIEhpZ2hsaWdodHMgLS0+CiAgICA8Y2lyY2xlIGN4PSI4MiIgY3k9Ijg4IiByPSIxIiBmaWxsPSJ3aGl0ZSIvPgogICAgPGNpcmNsZSBjeD0iMTIyIiBjeT0iODgiIHI9IjEiIGZpbGw9IndoaXRlIi8+CiAgICAKICAgIDwhLS0gQmFkZ2VyIE5vc2UgLS0+CiAgICA8Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMTAiIHI9IjUiIGZpbGw9IndoaXRlIi8+CiAgICAKICAgIDwhLS0gTm9zZSBIaWdobGlnaHQgLS0+CiAgICA8Y2lyY2xlIGN4PSIxMDIiIGN5PSIxMDgiIHI9IjEiIGZpbGw9IndoaXRlIi8+CiAgICAKICAgIDwhLS0gQmFkZ2VyIEVhcnMgLS0+CiAgICA8ZWxsaXBzZSBjeD0iNzAiIGN5PSI3MCIgcng9IjEwIiByeT0iMTUiIGZpbGw9IiMwMDAwMDAiLz4KICAgIDxlbGxpcHNlIGN4PSIxMzAiIGN5PSI3MCIgcng9IjEwIiByeT0iMTUiIGZpbGw9IiMwMDAwMDAiLz4KPC9zdmc+)](https://github.com/voxel51/badger)
[![Build Status](https://img.shields.io/travis/com/yourusername/badger)](https://travis-ci.com/yourusername/badger) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

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
python setup.py install
```

## 📝 Usage

Here's how you can use Badger:

### 🏗️ Create a New Badge

```bash
badger create badge_name
```

This will walk you through a series of prompts to customize your badge.

### 📋 Copy a Badge to Clipboard

```bash
badger copy badge_name
```

This copies the badge markdown to your clipboard. Paste it wherever you like!

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

### 🗑️ Delete a Badge

```bash
badger delete badge_name
```

Deletes the badge from your config file.

### ✨ Go Wild!

```bash
badger go-wild
```

Generates a random badge using AI and copies it to your clipboard. 🤪

:note: This uses your OpenAI API Key to call GPT 3.5

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

## 📚 Examples

Here are some examples of badges you can create with Badger:

## 💡 Why You Absolutely Need This

- Saves Time: No need to manually write markdown or HTML for badges. 🕒
- Be Unique: Stand out from the crowd with personalized badges. 🦄
- Stay Organized: Keep all your badges in one place, ready to be used anytime. 🗂
- It's Cool: Because let's face it, who doesn't like badges? 😎
