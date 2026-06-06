# WhatsApp Message Scheduler

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

A small Python utility that schedules and sends a WhatsApp message at a specified time using the `pywhatkit` library and WhatsApp Web.

## Overview

This project demonstrates browser-based WhatsApp automation in Python. Given a recipient's phone number, a message, and a target time, it opens WhatsApp Web and delivers the message automatically at the scheduled minute. It is a focused, single-script example intended as a starting point for personal reminders or simple notification workflows.

## Key Features

- Schedule a message for a specific hour and minute (24-hour clock)
- Automatic WhatsApp Web launch and message delivery via `pywhatkit.sendwhatmsg`
- Basic exception handling that reports failures to the console

## How It Works

The script defines the recipient number (with country code), the message text, and the delivery time, then calls `pywhatkit.sendwhatmsg()`. `pywhatkit` opens WhatsApp Web in the default browser shortly before the scheduled time and sends the message. All logic lives in a single `try/except` block so any errors are caught and printed.

## Tech Stack

- **Language:** Python 3
- **Library:** [pywhatkit](https://pypi.org/project/pywhatkit/)

## Getting Started

### Prerequisites

- Python 3.7 or newer
- A WhatsApp account already logged in to [WhatsApp Web](https://web.whatsapp.com/) in your default browser

### Installation

```bash
git clone https://github.com/iampreetdave-max/Whatsapp.git
cd Whatsapp
pip install pywhatkit
```

### Usage

Edit `test.py` to set your recipient number, message, and delivery time:

```python
phone_number = "+91XXXXXXXXXX"   # recipient, with country code
message      = "Your message here"
hour         = 22                # 24-hour format
minute       = 50
```

Then run:

```bash
python test.py
```

Keep the browser window in focus while the message is being sent.

## Project Structure

```
Whatsapp/
├── test.py      # Message scheduling script
├── LICENSE      # Apache License 2.0
└── README.md
```

## License

Licensed under the [Apache License 2.0](LICENSE).
