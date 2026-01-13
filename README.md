# Resume Gap Analyzer

An explainable Python-based system that analyzes skill gaps between resumes and job descriptions using transparent text processing, rule-based NLP, and deterministic scoring.

Unlike black-box AI resume tools, this project focuses on **clarity, correctness, and interview-readiness**.

---

## 🎯 Problem Statement

Recruiters and hiring managers often need to quickly understand:
- Whether a candidate meets job requirements
- Which skills are missing
- Why a candidate is (or isn’t) a good fit

Most existing tools rely on opaque AI models that provide little insight into their decisions.

This project solves that by building an **explainable decision pipeline** that clearly shows:
- Extracted skills
- Matched vs missing requirements
- Exact reasoning behind the match score

---

## 🧠 System Design Overview

The system follows a clean, step-by-step pipeline:

```
Resume / Job Description
↓
Text Cleaning & Normalization
↓
Skill Extraction (Rule-Based)
↓
Gap Analysis (Matched / Missing / Extra)
↓
Scoring Engine (Explainable Math)
↓
Human-Readable Explanations & Recommendations
```


Each stage is independent, testable, and transparent.

---

## 🧩 Key Components

### 1. Text Cleaner
Normalizes raw text by:
- Lowercasing
- Removing punctuation
- Normalizing whitespace

This ensures consistent and deterministic skill matching.

### 2. Skill Extractor
Uses a predefined skill dictionary to:
- Detect single-word and multi-word skills
- Categorize skills (languages, frameworks, tools, cloud, etc.)
- Avoid false positives and black-box inference

### 3. Gap Analyzer
Compares resume skills with job requirements to identify:
- Matched skills
- Missing required skills
- Extra / bonus skills

### 4. Scoring Engine
Calculates a match percentage using transparent logic:

Match Score = (Matched Required Skills / Total Required Skills) * 100



Every score is fully explainable.

### 5. Explanation & Recommendation Engine
Converts raw analysis into:
- Clear strengths
- Concrete gaps
- Actionable improvement recommendations

---

## 🛠 Tech Stack

- Python
- Regex-based text processing
- Rule-based NLP (no black-box ML)

---

## ✅ Why This Project Stands Out

- Deterministic & explainable logic
- Interview-safe design decisions
- Clean separation of concerns
- Easy to extend with ML or LLMs later

---

## 🚀 Future Enhancements

- Skill importance weighting
- Required vs nice-to-have classification
- Semantic similarity matching
- LLM-assisted explanation refinement
- REST API or Web UI

---

## 📌 Project Status

✅ Core pipeline complete  
🚧 Enhancements planned


