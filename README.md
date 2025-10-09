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
* Ambient noise filtering and adjustment
* Multiple language support capability
* Continuous listening mode
* Clear voice command detection

**🧠 Natural Language Processing**
* GPT-4o model integration for advanced understanding
* Context-aware response generation
* Human-like conversation flow
* Multi-turn dialogue support
* Intent recognition and classification
* Intelligent query processing

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
* Cross-platform compatibility
* Extensible command system

---

## 🏗️ System Architecture

### **Workflow Overview**

The assistant follows a streamlined process to handle user interactions:

1. **Audio Input**: Captures voice commands through microphone
2. **Speech Recognition**: Converts spoken words to text using Google's speech recognition
3. **Command Processing**: Analyzes the text to determine action type
4. **Response Generation**: 
   - For web commands → Opens specified websites
   - For queries → Sends to GPT-4o for intelligent responses
5. **Audio Output**: Converts text responses to speech using TTS engine
6. **Playback**: Delivers spoken response to user through speakers

This end-to-end pipeline ensures natural, conversational interactions with minimal latency.

---

## 🔬 How It Works

### **Voice Command Recognition**

The assistant uses the `speech_recognition` library to capture and process voice commands. It automatically adjusts for ambient noise and converts spoken language into text with high accuracy. The system supports multiple languages and can handle various accents and speaking styles.

### **Natural Language Processing with GPT-4o**

OpenAI's GPT-4o model powers the conversational intelligence. When users ask questions or make requests, the text is sent to the GPT-4o API, which generates human-like responses based on context and intent. The model understands complex queries, maintains conversation context, and provides accurate, relevant answers.

### **Text-to-Speech Conversion**

The `pyttsx3` library handles voice synthesis, converting text responses back into natural-sounding speech. The system works offline and offers customizable voice properties including speed, volume, and voice selection. This creates a seamless auditory experience for users.

### **Web Browser Automation**

For commands like "Open Google" or "Search for Python tutorials", the assistant uses the `webbrowser` module to automatically launch websites or perform searches. It recognizes common website names and can execute custom URL commands, making it a powerful productivity tool.

---

## 🛠️ Technologies & Libraries

### **Core Technologies**

**OpenAI GPT-4o**
* Advanced language model for natural language understanding
* Context-aware response generation
* Multi-turn conversation support
* High-quality, human-like text generation

**Speech Recognition**
* Library: `speech_recognition`
* Engine: Google Speech Recognition API
* High-accuracy voice-to-text conversion
* Support for 100+ languages

**Text-to-Speech**
* Library: `pyttsx3`
* Offline voice synthesis
* Customizable voice properties
* Platform-independent audio output

**Web Automation**
* Library: `webbrowser`
* Browser-agnostic URL opening
* Search query execution
* System default browser integration

### **Python Dependencies**

```
openai==1.3.0
speechrecognition==3.10.0
pyttsx3==2.90
pyaudio==0.2.13
python-dotenv==1.0.0
```

---

## 🚀 Setup & Installation

### **Prerequisites**
- Python 3.8 or higher
- OpenAI API key
- Microphone and speakers/headphones
- Internet connection

### **Installation Steps**

**1. Clone the Repository**
```bash
git clone https://github.com/arun-248/gpt-voice-assistant.git
cd gpt-voice-assistant
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Install PyAudio (Platform-specific)**

**Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

**macOS:**
```bash
brew install portaudio
pip install pyaudio
```

**Linux:**
```bash
sudo apt-get install python3-pyaudio
pip install pyaudio
```

**4. Configure API Key**

Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_api_key_here
```

**5. Run the Assistant**
```bash
python main.py
```

---

## 💡 Use Cases

### **Personal Productivity**
* Quick web searches and information lookup
* Hands-free website navigation
* Voice-controlled task management
* Calendar and reminder queries

### **Learning & Education**
* Ask questions about any topic
* Get explanations and definitions
* Learning assistance while multitasking
* Language practice and pronunciation

### **Accessibility**
* Assistive technology for visually impaired users
* Hands-free computer control
* Voice-based information access
* Reduced screen time interaction

### **Smart Home Integration**
* Voice commands for daily tasks
* Quick information retrieval
* Entertainment control (opening music/video sites)
* Productivity enhancement

---

## 🔒 Security & Privacy

**API Key Protection:**
* Secure storage in environment variables
* Never hardcoded in source files
* Excluded from version control

**Data Privacy:**
* Voice data processed in real-time
* No persistent audio storage
* Conversation history optional
* User control over data handling

**Best Practices:**
* Regular API key rotation
* Environment-based configuration
* Secure credential management
* Privacy-focused design

---

## 🚀 Future Enhancements

<details>
<summary><strong>🎯 Short-term Goals</strong></summary>

- [ ] Wake word detection ("Hey Assistant")
- [ ] Conversation history feature
- [ ] Multi-language support expansion
- [ ] GUI interface development
- [ ] File operations (create, read, delete)
- [ ] Email sending capability
- [ ] Calendar integration
- [ ] Reminder and alarm system

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
4. Add documentation for changes
5. Submit a pull request

### 🐛 **Reporting Issues**
- Use GitHub Issues for bugs
- Include error logs if applicable
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
