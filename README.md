# Jarvis Voice Assistant

A Python-based voice assistant inspired by Iron Man's JARVIS, designed specifically for macOS. This assistant uses speech recognition to listen for voice commands and responds with both voice feedback and actions.

## Features

- **Voice Recognition**: Uses Google Speech Recognition API to understand voice commands
- **AI-Powered Responses**: Integrates with Google's Gemini AI for intelligent responses to general questions
- **Web Navigation**: Quick commands to open popular websites (Google, YouTube, Facebook, Twitter, Instagram, Reddit, GitHub, LinkedIn)
- **Music Control**: Built-in music library with voice commands to play specific songs
- **Voice Feedback**: Uses macOS built-in `say` command for text-to-speech responses
- **Wake Word**: Activates when you say "Jarvis"
- **Audio Feedback**: Provides beeping sounds during AI processing

## Prerequisites

- macOS (required for the `say` command and audio playback)
- Python 3.x
- Microphone access
- Google Gemini API key

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Jarvis-Voice-Assistant
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   ```

3. **Activate virtual environment**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

5. **Set up environment variables**
   Create a `.env` file in the project root and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

1. **Start the program**
   ```bash
   python3 main.py
   ```

2. **Activate the assistant**
   - Say "Jarvis" to wake up the assistant
   - Wait for the "Yes?" response
   - Give your command

## Available Commands

### Web Navigation
- "Open Google"
- "Open YouTube"
- "Open Facebook"
- "Open Twitter"
- "Open Instagram"
- "Open Reddit"
- "Open GitHub"
- "Open LinkedIn"

### Music Control
- "Play pal pal"
- "Play qatal"
- "Play diamond"
- "Play millionaire"
- "Play unforgettable"
- "Play heer"
- "Play haseen"
- "Play maand"

### General Questions
- Ask any general question and Jarvis will use Gemini AI to provide an intelligent response

## How It Works

1. The program continuously listens for the wake word "Jarvis"
2. When detected, it responds with "Yes?" and starts listening for your command
3. Commands are processed through:
   - Built-in web navigation functions
   - Music library lookup
   - Gemini AI for general questions
4. Responses are provided via voice using macOS text-to-speech
5. During AI processing, a beeping sound indicates the system is working

## Project Structure

- `main.py` - Main application with voice recognition and command processing
- `musicLibrary.py` - Dictionary of song names and their YouTube URLs
- `requirements.txt` - Python dependencies
- `.env` - Environment variables (create this file with your API key)

## Dependencies

Key dependencies include:
- `google-generativeai` - For AI-powered responses
- `speech_recognition` - For voice command recognition
- `PyAudio` - For audio input/output
- `python-dotenv` - For environment variable management

## Notes

- This assistant is specifically designed for macOS due to its use of the `say` command and `afplay` for audio
- Requires an active internet connection for speech recognition and AI responses
- The music library can be expanded by adding more songs to `musicLibrary.py`

## Troubleshooting

- Ensure your microphone permissions are enabled
- Check that your Gemini API key is correctly set in the `.env` file
- Make sure you're in a quiet environment for better voice recognition
- Verify that all dependencies are properly installed in the virtual environment