<h1 align="center">Colorant</h1>

### Overview

Colorant is a Python-based project built for educational purposes, showcasing real-time color-based object tracking using computer vision techniques. The project interacts with hardware components such as Arduino, adding an extra layer of security.

---
![image](https://github.com/hafyzwithawhy/Colorant/assets/82477000/5e00264d-d4d9-461d-a87d-501cc6e50217)

[![Downloads][downloads-shield]][downloads-link]
[![Discord][discord-shield]][discord-link]
[![Language][language-shield]][language-link]
[![License][license-shield]][license-link]

## Components

### The Colorant project comprises several Python files:

- main.py: This is the main executable of the application that initiates the color tracking process and manages key events.

- colorant.py: Houses the Colorant class, which manages image processing and color tracking tasks.

- other.py: Contains the Mouse and Settings classes for Arduino communication and settings configuration, respectively. The Capture class responsible for screen capture operations is also defined here.

- settings.ini: The configuration file that stores various settings for colorant.

## Getting Started
### Prerequisites
For the mouse movement functionality of Colorant, an Arduino Leonardo is required. You can purchase it from [Amazon](https://www.amazon.com/Arduino-Leonardo-ATmega32U4-without-headers/dp/B008A36R2Y) or any local store in your region.

### Installation

You can either clone the repository and run the Python script directly, or you can download the precompiled executable from the releases page. The latest release is v1.0, released on 26 May 2023. This version is compiled into an executable for easier usage, and it doesn't require Python or any dependencies to be installed.

For the Python Script Version:
1. Clone the repository or download it directly.
2. Navigate into the project directory.
3. Run the main script: `python main.py`.

For the Executable Version:
1. Download the latest release from the [releases page](https://github.com/hafyzwithawhy/Colorant/releases/latest).
2. Unzip the downloaded file.
3. Run the SetupColorant.exe setup executable then Colorant.exe to start using colorant.

## Assistance

If you need help or have questions about Colorant, consider joining the community Discord:

[![Discord Banner 2][discord-banner]][discord-link]

## Contributing

Contributions are welcome! Feel free to fork the project and submit a pull request with your changes. Additionally, if you find this project helpful or interesting, please give it a ⭐.

I'd like to acknowledge and credit the program Firepro, which has been a significant inspiration for Project Colorant.

## Disclaimer
> **Warning** **Educational Use Only**
Please understand that this project, Colorant, has been developed solely for EDUCATIONAL PURPOSES. It provides a demonstration of the capabilities of computer vision and hardware interaction, not to facilitate cheating or unauthorized activities in games or other digital environments.

> **Warning** **Not for Unfair Advantage**
While this project might present functionalities that could be used to gain an unfair advantage in a game, such use is expressly discouraged. Misuse of this project to cheat or disrupt the gameplay experience for others is contrary to the intended purpose of this educational tool.

> **Warning** **Potential Consequences**
Be aware that, even though the project does not interact with game memory or files making it undetectable, this does not make it unbannable. Gaming companies have the right to ban users they suspect of cheating. We take no responsibility for any actions taken against users for misusing this project, including but not limited to, being banned from a game or platform.

> **Warning** **Ethical Usage**
We strongly advocate for ethical usage of programming skills and tools. Cheating and hacking not only ruin the gaming experience for others but also breach trust and violate privacy. Use this tool responsibly to learn and grow as a developer, not to cheat or hack.

By using Colorant, you acknowledge that you have read and understood these disclaimers and that you agree to comply with them.

[discord-shield]: https://img.shields.io/discord/1102647720981831750?color=purple&label=Support&logo=discord&logoColor=white&style=for-the-badge
[discord-link]: https://discord.gg/RExkpUdwjH
[discord-banner]: https://discordapp.com/api/guilds/1102647720981831750/widget.png?style=banner2

[downloads-shield]: https://img.shields.io/github/downloads/hafyzwithawhy/Colorant/total?color=purple&logo=GitHub&style=for-the-badge
[downloads-link]: https://github.com/hafyzwithawhy/Colorant/releases/latest

[language-shield]: https://img.shields.io/github/languages/top/hafyzwithawhy/Colorant?color=purple&logo=python&logoColor=white&style=for-the-badge
[language-link]: https://www.python.org/

[license-shield]: https://img.shields.io/github/license/hafyzwithawhy/Colorant?color=purple&logo=github&style=for-the-badge
[license-link]: https://github.com/hafyzwithawhy/Colorant/blob/main/LICENSE
