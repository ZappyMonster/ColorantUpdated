<h1 align="center">Colorant</h1>

### About

Colorant is an educational project that demonstrates the use of color detection. It also includes an aimbot feature to target and shoot within a specific color range on a screen. The main goal is to detect and interact with the chosen color, aiming and shooting at it.

Implemented in Python, Colorant scans the screen for a defined hsv color range and enables interaction with the identified region. Notably, this process does not involve any manipulation of game memory or files.

The project's primary aim is to serve as a proof of concept, illustrating the potential of computer vision in interacting with real-time screen data.

---
![image](https://github.com/hafyzwithawhy/Colorant/assets/82477000/5e00264d-d4d9-461d-a87d-501cc6e50217)

[![Downloads][downloads-shield]][downloads-link]
[![Discord][discord-shield]][discord-link]
[![Language][language-shield]][language-link]
[![License][license-shield]][license-link]

## Getting started

#### You will need the following prerequisites:
- [ARDUINO LEONARDO](https://www.amazon.com/Arduino-org-A000057-Arduino-Leonardo-Headers/dp/B008A36R2Y)
- [USB HOST SHIELD](https://www.amazon.com/Compatible-Arduino-Support-Android-Function/dp/B0B3TH6H6N)

Setting up initially might pose a challenge as it requires Arduino and USB host shield setup. Keep in mind that some USB shields may be delivered unsoldered, requiring you to solder both 5V ports and the bottom 3.3V port to ensure proper operation. If you need more guidance, refer to [THIS](https://www.youtube.com/watch?v=nBttwvgNOr8) video.

Subsequently, download and install Python, ideally [Version 3.8](https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe) as it was the development version for this project. Once Python is installed, download Colorant and install necessary dependencies using `pip install -r the-requirements.txt`.

To enable Arduino board to function as a computer mouse, choose from the five different sketches provided in the [ArduinoSketches](https://github.com/hafyzwithawhy/Colorant/tree/main/ArduinoSketches) folder. Plug the Arduino board into your computer and open the Arduino IDE software. Select the suitable board and port and upload your chosen sketch. Following these instructions will convert your Arduino board into a working computer mouse, enabling cursor control and click functionalities through the board's hardware. Try out each of the five sketches to find out which suits your mouse best.

Bear in mind that if you chose a sketch other than 1Arduino, you might need to configure move and click functions for compatibility with your Arduino sketch. The Colorant code is optimized for the 1Arduino sketch, so other sketches may require modifications.

With the required software and dependencies installed, execute the main.py file, the main entry point for the program. No code modifications are needed, and it's ready for use.

## Assistance

If you need help or have questions about Colorant, consider joining the community Discord:

[![Discord Banner 2][discord-banner]][discord-link]

## Contributing

Contributions are welcome from the community, and if you have any suggestions or encounter any issues, please do not hesitate to open an [issue](https://github.com/hafyzwithawhy/Colorant/issues) in the repository and provide as much detail as possible. Additionally, if you find this project helpful or interesting, please give it a ⭐.

I'd like to acknowledge and credit the program Firepro, which has been a significant inspiration for Project Colorant. Additionally, I want to clarify that the Arduino sketches included in this project were not created by me.

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
