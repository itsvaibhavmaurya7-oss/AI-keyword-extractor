# 🔑 AI Keyword Extractor

An AI-powered Keyword Extractor built with **Python**, **Streamlit**, and **YAKE (Yet Another Keyword Extractor)**. This application extracts the most important keywords from a paragraph or text file without requiring any machine learning model training.

## 🚀 Features

- Extract keywords from pasted text
- Upload `.txt` files for keyword extraction
- Select different languages (English, Hindi, French, German, Spanish)
- Adjust the number of keywords to extract
- Choose the maximum keyword phrase length (1–3 words)
- Display keyword relevance scores
- Download extracted keywords as a CSV file
- Simple and interactive Streamlit interface

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- YAKE

## 📂 Project Structure

```
AI-Keyword-Extractor/
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
    └── app.png
```

## 📦 Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Keyword-Extractor.git
```

2. Navigate to the project folder

```bash
cd AI-Keyword-Extractor
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

The application will open automatically in your browser.

## 📸 Screenshot

Add a screenshot of your application here.

Example:

```
screenshots/app.png
```

## 📄 Example Output

| Keyword | Score |
|---------|--------|
| Artificial Intelligence | 0.00125 |
| Machine Learning | 0.00243 |
| Data Science | 0.00310 |

> Lower YAKE scores indicate more important keywords.

## 📥 Download Results

Users can download the extracted keywords as a CSV file for further analysis.

## 🔮 Future Improvements

- PDF keyword extraction
- Word document support
- Keyword visualization using charts
- Stop-word customization
- Keyword highlighting inside the text
- Dark mode support

## 📜 License

This project is licensed under the MIT License.
