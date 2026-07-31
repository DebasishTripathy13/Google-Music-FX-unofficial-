<p align="center">
  <img src="banner-musicfx.png" alt="Google Music FX (Unofficial)" width="100%">
</p>

# Google Music FX (Unofficial)

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-blue?style=flat-square">
  <img alt="Stars" src="https://img.shields.io/github/stars/DebasishTripathy13/Google-Music-FX-unofficial-?style=flat-square&color=yellow">
</p>

An unofficial Python client for the Google Music FX API that allows you to generate AI-powered music from text prompts.

## 📖 Introduction

Google Music FX is an AI tool that generates music based on text descriptions. This unofficial client provides a simple way to interact with the API, even in regions where the service isn't officially available.

This repository focuses on implementing the Music FX API, which is currently accessible only in a few countries, excluding India. To bypass this restriction, a VPN or VPS can be used to obtain an access key, allowing usage in India or world wide until the key's expires (approximately 8 hours).

## ✨ Features

- Generate music from text descriptions
- Configure generation parameters (count, duration)
- Save audio files locally
- Customizable settings through environment variables

## 🔧 Installation

### Prerequisites

- Python 3.9+
- pip

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/DebasishTripathy13/Google-Music-FX-unofficial-.git
   cd Google-Music-FX-unofficial-
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy the example environment file and add your credentials:
   ```bash
   cp example.env .env
   ```

4. Edit the `.env` file to add your authentication token and session ID.

## 🚀 Usage

### Basic Usage

Run the main script:
```bash
python main.py
```

You will be prompted to enter a description for the music you want to generate. For example:

```
Please enter a description for the music (e.g., 'anime background song for a sad plot twist'):
```

The generated audio files will be saved in the current directory.

### Advanced Usage

You can customize the generation process by modifying the settings in the `.env` file:

```
MAX_GENERATION_COUNT=3
ALLOWED_SOUND_LENGTHS="30,50,70"
```

## ⚙️ Configuration

### Environment Variables
![alt text](<Screenshot 2025-03-12 100501.png>) 


![alt text](<Screenshot 2025-03-12 110323.png>)

| Variable | Description | Default |
|----------|-------------|---------|
| AUTH_TOKEN | Google API authorization token | None (required) |
| SESSION_ID | Google API session ID | None (required) |
| MAX_GENERATION_COUNT | Maximum number of music variations to generate | 3 |
| ALLOWED_SOUND_LENGTHS | Comma-separated list of allowed sound lengths (in seconds) | "30,50,70" |

### Obtaining Credentials

To obtain the AUTH_TOKEN and SESSION_ID:

1. Use a VPN to access a region where Music FX is available
2. Open Chrome DevTools (F12) on the Music FX website
3. Navigate to the Network tab
4. Look for requests to `soundDemo` API endpoints
5. Extract the Authorization token and session ID from request headers

## 📝 API Details

The application uses the Google AI Sandbox API endpoint:
```
https://aisandbox-pa.googleapis.com/v1:soundDemo
```

The main parameters for music generation are:
- `textInput`: Your music description
- `generationCount`: Number of variations (max 3)
- `soundLengthSeconds`: Duration in seconds (30, 50, or 70)
- `loop`: Whether the music should be composed to loop

## 🧪 Testing

Run the test suite using pytest:
```bash
pytest
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This is an unofficial client and not affiliated with Google. Use at your own risk and in accordance with Google's terms of service.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
