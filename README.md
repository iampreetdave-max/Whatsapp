# WhatsApp Automation

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=flat&logo=whatsapp&logoColor=white)

> A Python script for scheduling and sending automated WhatsApp messages using pywhatkit.

## About

A simple WhatsApp automation tool that uses the `pywhatkit` library to schedule and send messages to specified phone numbers at a given time. Opens WhatsApp Web automatically and sends the message at the scheduled time.

## Tech Stack

- **Language:** Python 3
- **Library:** pywhatkit

## Features

- **Scheduled messaging** — set exact hour and minute for delivery
- **Automated browser launch** — opens WhatsApp Web automatically
- **Error handling** — catches and reports failures gracefully

## Getting Started

### Prerequisites

- Python 3.7+
- WhatsApp account linked to WhatsApp Web

### Installation

```bash
git clone https://github.com/iampreetdave-max/Whatsapp.git
cd Whatsapp
pip install pywhatkit
```

### Run

```bash
python test.py
```

Edit `test.py` to set the recipient phone number, message, and scheduled time.

## How It Works

1. Set the recipient's phone number (with country code), message text, and delivery time
2. `pywhatkit.sendwhatmsg()` opens WhatsApp Web in your browser at the specified time
3. The message is typed and sent automatically

## Project Structure

```
Whatsapp/
├── test.py      # WhatsApp message scheduler
├── LICENSE
└── README.md
```

## License

This project is licensed under the [Apache License 2.0](LICENSE).
