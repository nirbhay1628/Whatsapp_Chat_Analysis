# WhatsApp Chat Analyzer

A Streamlit web app that converts exported WhatsApp chats into clear visual insights.

It helps you analyze:
- Total messages, words, media, and links
- Monthly and daily activity trends
- Most active days and months
- Weekly activity heatmap
- Most active users
- Wordcloud and most common words
- Emoji usage distribution

## Live Demo

If deployed on Streamlit Cloud, open your app URL here:
- https://github.com/nirbhay1628/Whatsapp_Chat_Analysis

## Features

- Clean and modern Streamlit UI
- Main-page controls (no sidebar dependency)
- WhatsApp parser support for multiple date/time styles
- Handles AM/PM chats and hidden Unicode spacing in exported files
- Graceful handling for empty/no-data chart conditions
- Footer branding: "Made with love by Nirbhay"

## Tech Stack

- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- WordCloud
- Emoji
- URLExtract

## Project Structure

```text
Watsapp-Chat-Analysis-Project-main/
├── app.py
├── helper.py
├── preprocessor.py
├── requirements.txt
├── procfile
├── setup.sh
├── stop_hinglish.txt
├── notes.ipynb
└── whatsappchatanalysis.ipynb
```

## How It Works

1. Upload exported WhatsApp .txt file
2. App preprocesses raw chat text in preprocessor.py
3. It builds a structured dataframe with date/time/user/message columns
4. helper.py computes analytics and chart-ready data
5. app.py renders metrics and plots in Streamlit

## Input Chat Format

The parser supports common WhatsApp exports such as:

- 17/02/24, 1:42 am - Name: Message
- 17/02/2024, 14:30 - Name: Message

It also handles system notifications like:
- Messages and calls are end-to-end encrypted
- Group created/added messages

## Local Setup

### 1. Clone Repository

```bash
git clone https://github.com/nirbhay1628/Whatsapp_Chat_Analysis.git
cd Whatsapp_Chat_Analysis
```

### 2. Create and Activate Virtual Environment

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows (CMD):

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run App

```bash
streamlit run app.py
```

Open browser at:
- http://localhost:8501

## Deployment (Streamlit Cloud)

1. Push project to GitHub
2. Open Streamlit Cloud
3. Create new app from repository
4. Set:
   - Branch: main
   - Main file path: app.py
5. Deploy

## Troubleshooting

### 1) No messages were parsed from the file

- Ensure file is exported from WhatsApp as .txt
- Export "Without Media"
- Verify chat lines contain date, time, and separator with hyphen:
  - Example: 09/02/24, 11:47 pm - User: Message

### 2) Deployment stuck on "Your app is in the oven"

- Reboot app in Streamlit Cloud
- Hard refresh browser (Ctrl+F5)
- Clear browser cache/site data for streamlit.app
- Confirm app.py is selected as entrypoint
- Confirm dependencies install from requirements.txt

### 3) Dynamic import module fetch errors

- Usually frontend cache mismatch after new deployments
- Hard refresh or open app in incognito
- Reboot app from Streamlit Cloud dashboard

## Important Notes

- This app analyzes exported text chats only
- Keep private chats safe; avoid committing personal chat exports
- Add chat export patterns to .gitignore if needed

## Future Improvements

- Sentiment analysis for messages
- Interactive filters by date range
- Downloadable analytics report
- Comparative analytics between users

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

## License

Add your preferred license (MIT recommended) in a LICENSE file.

## Author

Nirbhay
