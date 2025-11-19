AI Engineer Technical Challenge - 01
Problem Context
Trust & Safety (T&S) teams maintain policies in many formats - PDFs, Word docs,
PowerPoints, Google Docs, text files, internal wiki pages, etc. These documents are written
for humans, not LLMs. As a result:
● Policies lack consistent structure or labeling
● Key decision rules are buried inside long paragraphs, tables, or diagrams
● Different teams produce differently formatted versions of the same policy
● LLMs cannot reliably ingest or apply these documents without extensive
preprocessing
At the same time, modern T&S workflows increasingly rely on open-source LLMs (e.g.,
OSS GPT “Safeguard” 20B/120B or similar models) for content classification,
moderation, and risk scoring. Companies want to run these models in their own
environments for privacy, cost, and compliance reasons - but often lack the infrastructure to
do so safely and reliably. We want a system that:
1. Standardizes unstructured T&S policy documents into a machine-actionable policy
format, and
2. Exposes an API for content moderation using a self-hosted OSS safeguard model.
These are the examples of what trust & safety policies look like:
https://www.facebook.com/help/instagram/477434105621119/
https://www.patreon.com/policy/guidelines
https://www.care.com/about/safety/community-guidelines/
https://www.linkedin.com/legal/professional-community-policies
https://help.x.com/en/rules-and-policies
https://www.youtube.com/intl/en_us/howyoutubeworks/policies/community-guidelines/
Objective
Create a detailed technical design proposal for this project.
You may use ChatGPT or other tools to help you, but to stand out you must go into minute
technical details on architecture, trade-offs, and rationale - as if you were going to lead the
implementation with a small team. Also include the number of weeks of efforts it will take to
implement etc. We are looking for senior engineers, so showcase to us that y

# Emotion Detector

Detect emotions in text using IBM Watson NLU or other NLP models.

## Features
- Analyzes text for emotions (joy, anger, sadness, etc.)
- Simple API integration
- Useful for chatbots and sentiment analysis

## Getting Started
```bash
git clone https://github.com/TamerDotWork/EmotionDetector.git
cd EmotionDetector
pip install -r requirements.txt
python app.py
```




