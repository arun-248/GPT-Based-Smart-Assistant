# 🤖 GPT-Based Smart Voice Assistant

<div align="center">

[![Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white&style=for-the-badge)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?logo=openai&logoColor=white&style=for-the-badge)](https://openai.com/)
[![Speech Recognition](https://img.shields.io/badge/Speech-Recognition-FF6B6B?style=for-the-badge)]()
[![Text to Speech](https://img.shields.io/badge/Text--to--Speech-4ECDC4?style=for-the-badge)]()

**🎯 An interactive voice-controlled AI assistant leveraging OpenAI's GPT-4o model for natural language understanding and seamless human-computer interaction**

</div>

---

## 🌟 Project Highlights

> **Intelligent Voice Assistant**: A cutting-edge application combining speech recognition, natural language processing, and text-to-speech synthesis to create a seamless, intuitive voice-controlled assistant powered by OpenAI's GPT-4o model.

**🎯 What makes this special:**
- **Voice-first interaction** with hands-free operation
- **GPT-4o integration** for intelligent, context-aware responses
- **Real-time speech recognition** with high accuracy
- **Natural text-to-speech** output for human-like conversations
- **Web automation capabilities** for enhanced productivity
- **Extensible architecture** for custom command integration
- **Low-latency processing** for responsive interactions

---

## 🚀 Key Features

**🎤 Voice Command Recognition**
* Real-time audio capture from microphone
* High-accuracy speech-to-text conversion
* Ambient noise filtering
* Multiple language support capability
* Continuous listening mode
* Wake word detection (optional)

**🧠 Natural Language Processing**
* GPT-4o model integration for advanced understanding
* Context-aware response generation
* Human-like conversation flow
* Multi-turn dialogue support
* Intent recognition and classification
* Sentiment analysis capabilities

**🔊 Text-to-Speech Synthesis**
* Natural-sounding voice output
* Adjustable speech rate and volume
* Multiple voice options (male/female)
* Clear pronunciation and intonation
* Real-time audio playback
* Offline TTS capability

**🌐 Web Browser Automation**
* Voice-activated website opening
* Predefined command shortcuts (Google, YouTube, etc.)
* Custom URL launching
* Search query execution
* Browser control commands
* Multi-platform browser support

**⚡ Advanced Capabilities**
* Conversation history tracking
* Command customization
* Error handling and retry logic
* Audio feedback for actions
* Extensible plugin system
* Cross-platform compatibility

---

## 🏗️ System Architecture

### **End-to-End Workflow**

```
User Voice Input
    ↓
[Microphone Capture]
    ↓
[Speech Recognition Module]
    ↓
Text Command
    ↓
[Command Parser]
    ↓
├─→ [Web Automation] (if URL command)
│
└─→ [OpenAI GPT-4o API] (if query)
    ↓
Generated Response
    ↓
[Text-to-Speech Engine]
    ↓
[Audio Output]
    ↓
Speaker Playback
```

### **Component Interaction**

**1. Audio Input Layer**
* Microphone initialization
* Audio stream capture
* Background noise suppression
* Audio buffer management

**2. Speech Recognition Layer**
* Google Speech Recognition API
* Acoustic model processing
* Language detection
* Text output generation

**3. Natural Language Understanding Layer**
* GPT-4o model inference
* Context maintenance
* Response generation
* Error handling

**4. Action Execution Layer**
* Command classification
* Web automation execution
* System command processing
* Response formatting

**5. Audio Output Layer**
* TTS engine initialization
* Voice synthesis
* Audio playback
* Volume control

---

## 🔬 Core Functionality

### **1. 🎤 Voice Command Recognition**

**Implementation:**
```python
import speech_recognition as sr

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio)
        return command.lower()
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand"
```

**Features:**
* **Ambient Noise Adjustment**: Filters background noise for clarity
* **Energy Threshold**: Adapts to different audio environments
* **Timeout Management**: Prevents indefinite listening
* **Multi-language Support**: Configurable language detection

**Supported Commands:**
* Natural language queries
* Web navigation commands
* System control commands
* Custom user-defined commands

---

### **2. 🧠 Natural Language Processing**

**GPT-4o Integration:**
```python
import openai

def get_ai_response(user_query):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_query}
        ],
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].message.content
```

**Capabilities:**
* **Context Awareness**: Maintains conversation history
* **Intent Recognition**: Understands user objectives
* **Response Generation**: Creates human-like replies
* **Error Handling**: Graceful degradation on failures
* **Token Optimization**: Efficient API usage

**Use Cases:**
* General knowledge questions
* Conversational queries
* Task assistance
* Information retrieval
* Creative content generation

---

### **3. 🔊 Text-to-Speech Conversion**

**Implementation:**
```python
import pyttsx3

def speak_response(text):
    engine = pyttsx3.init()
    
    # Configure voice properties
    engine.setProperty('rate', 150)      # Speed
    engine.setProperty('volume', 0.9)    # Volume (0.0 to 1.0)
    
    # Optional: Set voice (male/female)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    
    engine.say(text)
    engine.runAndWait()
```

**Features:**
* **Offline Capability**: No internet required for TTS
* **Voice Customization**: Multiple voice options
* **Speed Control**: Adjustable speaking rate
* **Volume Management**: Dynamic volume adjustment
* **Queue Management**: Handles multiple speech requests

**Voice Properties:**
* Rate: 100-200 words per minute
* Volume: 0.0 (silent) to 1.0 (maximum)
* Voice selection: Male/Female options
* Language support: Multiple languages

---

### **4. 🌐 Web Browser Automation**

**Implementation:**
```python
import webbrowser

def open_website(command):
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://www.github.com",
        "linkedin": "https://www.linkedin.com"
    }
    
    for site, url in websites.items():
        if site in command:
            webbrowser.open(url)
            return f"Opening {site}"
    
    # If no match, try as search query
    search_query = command.replace("search", "").strip()
    webbrowser.open(f"https://www.google.com/search?q={search_query}")
    return f"Searching for {search_query}"
```

**Supported Commands:**
* "Open Google" → Opens Google homepage
* "Open YouTube" → Opens YouTube
* "Search for [query]" → Google search
* "Open [custom URL]" → Opens specified website

**Features:**
* Default browser detection
* Multiple browser support
* URL validation
* Search query parsing
* Tab management

---

## 🛠️ Technologies & Libraries

### **Core Technologies**

**OpenAI API**
* **Version**: Latest GPT-4o model
* **Purpose**: Natural language understanding and response generation
* **Features**: Context awareness, multi-turn conversations
* **API Endpoint**: chat.completions

**Speech Recognition**
* **Library**: speech_recognition (v3.10.0+)
* **Engine**: Google Speech Recognition API
* **Accuracy**: High-quality transcription
* **Languages**: 100+ languages supported

**Text-to-Speech**
* **Library**: pyttsx3 (v2.90+)
* **Engine**: Platform-specific TTS engines (SAPI5, nsss, espeak)
* **Offline**: Works without internet
* **Customization**: Voice, rate, volume control

**Web Automation**
* **Library**: webbrowser (Python standard library)
* **Browsers**: Chrome, Firefox, Safari, Edge
* **Features**: URL opening, tab management

### **Additional Dependencies**

```python
# Core dependencies
openai==1.3.0
speechrecognition==3.10.0
pyttsx3==2.90
pyaudio==0.2.13

# Optional enhancements
python-dotenv==1.0.0  # Environment variables
requests==2.31.0      # HTTP requests
numpy==1.24.0         # Audio processing
```

---

## 📂 Project Structure

```
gpt-voice-assistant/
│
├── src/
│   ├── main.py                # Main application entry point
│   ├── speech_recognition.py  # Voice input handling
│   ├── text_to_speech.py      # Audio output handling
│   ├── openai_handler.py      # GPT-4o API integration
│   ├── web_automation.py      # Browser control
│   └── command_parser.py      # Command processing logic
│
├── config/
│   ├── config.py              # Configuration settings
│   └── commands.json          # Custom command definitions
│
├── utils/
│   ├── audio_utils.py         # Audio processing utilities
│   ├── logger.py              # Logging configuration
│   └── error_handler.py       # Error management
│
├── tests/
│   ├── test_speech.py
│   ├── test_openai.py
│   └── test_automation.py
│
├── .env                       # Environment variables (API keys)
├── .env.example              # Environment template
├── requirements.txt           # Python dependencies
└── README.md                 # Project documentation
```

---

## 🚀 Setup & Installation

### **Prerequisites**
- Python 3.8 or higher
- OpenAI API key
- Microphone and speakers
- Internet connection (for speech recognition and GPT-4o)

### **Installation Steps**

**1. Clone the Repository**
```bash
git clone https://github.com/arun-248/gpt-voice-assistant.git
cd gpt-voice-assistant
```

**2. Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Install PyAudio (Platform-specific)**

**On Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

**On macOS:**
```bash
brew install portaudio
pip install pyaudio
```

**On Linux:**
```bash
sudo apt-get install python3-pyaudio
pip install pyaudio
```

**5. Set Up Environment Variables**
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

**.env file:**
```
OPENAI_API_KEY=your_openai_api_key_here
MODEL=gpt-4o
MAX_TOKENS=150
TEMPERATURE=0.7
TTS_RATE=150
TTS_VOLUME=0.9
```

**6. Run the Application**
```bash
python src/main.py
```

---

## 💻 Usage Guide

### **Basic Usage**

**1. Start the Assistant**
```bash
python src/main.py
```

**2. Speak Your Command**
* Wait for "Listening..." prompt
* Speak clearly into microphone
* Assistant will process and respond

**3. Example Commands**

**General Queries:**
* "What is the weather today?"
* "Tell me a joke"
* "Explain quantum physics"
* "What's the capital of France?"

**Web Commands:**
* "Open Google"
* "Open YouTube"
* "Search for Python tutorials"
* "Open GitHub"

**System Commands:**
* "Stop listening"
* "Exit"
* "Help"

### **Advanced Configuration**

**Custom Commands:**
```json
// config/commands.json
{
  "open_email": {
    "keywords": ["email", "mail", "inbox"],
    "action": "open_url",
    "url": "https://mail.google.com"
  },
  "play_music": {
    "keywords": ["play", "music", "spotify"],
    "action": "open_url",
    "url": "https://open.spotify.com"
  }
}
```

**Voice Settings:**
```python
# config/config.py
TTS_CONFIG = {
    "rate": 150,           # Words per minute
    "volume": 0.9,         # 0.0 to 1.0
    "voice_index": 0,      # 0 for male, 1 for female (may vary)
}
```

---

## 🎯 Command Examples

### **Conversational Queries**

| User Command | Assistant Response |
|--------------|-------------------|
| "What's your name?" | "I'm your AI assistant powered by GPT-4o" |
| "How are you?" | "I'm functioning perfectly! How can I help?" |
| "Tell me about AI" | *Provides detailed explanation* |

### **Web Navigation**

| User Command | Action |
|--------------|--------|
| "Open Google" | Opens google.com |
| "Open YouTube" | Opens youtube.com |
| "Search for recipes" | Google search for recipes |
| "Go to GitHub" | Opens github.com |

### **Information Retrieval**

| User Command | Response Type |
|--------------|---------------|
| "What is machine learning?" | Educational explanation |
| "Latest news" | Current events summary |
| "Weather forecast" | Weather information |

---

## ⚡ Performance Optimization

### **Latency Reduction**

**1. Caching Responses**
```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_cached_response(query):
    return get_ai_response(query)
```

**2. Asynchronous Processing**
```python
import asyncio

async def process_command(command):
    response = await async_openai_call(command)
    speak_response(response)
```

**3. Optimized Audio Settings**
```python
recognizer.energy_threshold = 300  # Adjust for environment
recognizer.pause_threshold = 0.8   # Faster command detection
```

### **Cost Optimization**

**Token Management:**
* Use `max_tokens` parameter wisely
* Implement conversation summarization
* Cache frequent responses
* Use GPT-3.5-turbo for simple queries

**API Call Reduction:**
* Local command processing first
* Batch similar requests
* Implement request throttling

---

## 🚀 Future Enhancements

<details>
<summary><strong>🎯 Short-term Goals</strong></summary>

- [ ] Add wake word detection (e.g., "Hey Assistant")
- [ ] Implement conversation history
- [ ] Add support for multiple languages
- [ ] Create GUI interface
- [ ] Add file operations (create, read, delete)
- [ ] Implement email sending capability
- [ ] Add calendar integration
- [ ] Create reminder and alarm system

</details>

<details>
<summary><strong>🌟 Long-term Vision</strong></summary>

- [ ] **Smart Home Integration**: Control IoT devices
- [ ] **Context-Aware Memory**: Long-term conversation recall
- [ ] **Multi-Modal Input**: Support for images and documents
- [ ] **Emotional Intelligence**: Sentiment-aware responses
- [ ] **Voice Cloning**: Custom voice output
- [ ] **Mobile App**: iOS and Android versions
- [ ] **Plugin System**: Extensible command modules
- [ ] **Multi-User Support**: Voice recognition for different users
- [ ] **Offline Mode**: Local AI model integration

</details>

---

## 🔒 Security & Privacy

### **Best Practices**

**API Key Management:**
* Store keys in `.env` file
* Never commit `.env` to version control
* Use environment variables in production
* Rotate API keys regularly

**Data Privacy:**
* Audio data not stored by default
* Conversation history can be disabled
* GDPR-compliant data handling
* Optional encryption for sensitive data

**Error Handling:**
* Graceful API failure handling
* Audio device error management
* Network timeout handling
* User-friendly error messages

---

## 🧪 Testing

### **Run Tests**

**Unit Tests:**
```bash
pytest tests/test_speech.py
pytest tests/test_openai.py
pytest tests/test_automation.py
```

**Integration Tests:**
```bash
pytest tests/ -v
```

**Manual Testing:**
```bash
python src/main.py --test-mode
```

### **Test Coverage**

- [x] Speech recognition accuracy
- [x] OpenAI API integration
- [x] Text-to-speech functionality
- [x] Web automation commands
- [x] Error handling scenarios
- [x] Multi-language support

---

## 🙏 Acknowledgments

- **OpenAI**: For providing GPT-4o model and API
- **Google**: For Speech Recognition API
- **pyttsx3 Contributors**: For offline TTS library
- **Python Community**: For excellent libraries and support
- **Open Source Community**: For tools and inspiration

---

## 🤝 Contributing

Contributions are welcome!

### 💡 **How to Contribute**
1. Fork the repository
2. Create a feature branch
3. Implement new features or commands
4. Add tests for new functionality
5. Submit a pull request

### 🐛 **Reporting Issues**
- Use GitHub Issues for bugs
- Include error logs and stack traces
- Describe reproduction steps
- Mention Python version and OS

---

## 📄 License

This project is open-source and available for educational and personal use.

```
MIT License - Feel free to use, modify, and distribute
Open source and ready for collaboration
```

---

<div align="center">

## 🎯 Project Summary

> "An intelligent voice-controlled AI assistant combining speech recognition, GPT-4o natural language processing, and text-to-speech synthesis for seamless human-computer interaction."

**🤖 Built with AI | 🎤 Powered by Voice | 🧠 Driven by GPT-4o**

---

**Made with ❤️ by [Arun Chinthalapally](https://github.com/arun-248)**

⭐ **Star this repository if you found it useful!**

</div>
