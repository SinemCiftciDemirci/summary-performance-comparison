# 📊 Summary Performance Comparison

This repository provides a Python script to visualize and compare the performance of multiple text summarization models using **ROUGE** and **BERTScore** metrics. It automatically generates insightful plots from the provided data in an Excel format.

---
🔗 Related Projects This project is part of a modular research framework for evaluating and improving fairy tale summarization models. Below are the related repositories:

| Children's Tale Summarizer - Flask App | The main Flask-based API that generates fairy tale summaries. (https://github.com/SinemCiftciDemirci/childrens-tale-summarizer-flask-app) |

| GPT Summarizer | Creates GPT-based fairy tale summaries. (https://github.com/SinemCiftciDemirci/gpt-summarizer) |

| Cosine Similarity Summarizer | Performs extractive summarization using cosine similarity. (https://github.com/SinemCiftciDemirci/cosine-similarity-summarizer) |

| Single Summary Evaluation | Measures the performance of a single summary using BERTScore and ROUGE score. (https://github.com/SinemCiftciDemirci/single-summary-evaluation) |

| Batch Summary Performance Evaluation | Compares model-generated summaries with GPT and Cosine-based reference summaries, calculating ROUGE and BERTScore collectively. (https://github.com/SinemCiftciDemirci/batch-summary-performance-evaluation) |

| Summary Performance Comparison | Creates visual performance comparisons from the Model_Performance.xlsx file produced in the Batch Summary Evaluation repo. (https://github.com/SinemCiftciDemirci/summary-performance-comparison) |

| Vision Model Test | Translates the generated summaries into English and creates three visuals: introduction, development, and conclusion. (https://github.com/SinemCiftciDemirci/vision-model-test) |

Each repository serves a unique role in evaluating or improving summarization models. You can use them individually or together for deeper analysis.

## 🚀 Features

- **Visual comparison** of multiple summarization models.
- Generates detailed bar charts for key metrics:
  - ✅ **ROUGE-1, ROUGE-2, ROUGE-L**
  - ✅ **BERTScore (F1-score)**
  - ✅ **Overall Average** across all metrics
- Provides clear visual insights into the strengths and weaknesses of different summarization approaches.

---

## 📂 Project Structure

```
summary-performance-comparison/
├── performance_comparison.py
├── split_story_model_names.py
├── metrics/
│   ├── Model_Performance.xlsx
│   └── Model_Performance_Updated.xlsx
├── README.md

```

---

## 📌 Installation

Install the required dependencies:

```bash
pip install pandas matplotlib seaborn openpyxl
```

---

## 🎯 Usage

1. **Prepare your Data**

Ensure you have an Excel file with your summarization performance metrics named:

```
metrics/Model_Performance.xlsx
```

2. **Prepare the .xlsx file using split_story_model_names.py**

The Model_Performance.xlsx file initially contains only a "File Name" column. Running split_story_model_names.py will generate two new columns: Story Name and Model Name.

```bash
python split_story_model_names.py
```

3. **Run the Visualization**

```bash
python performance_comparison.py
```

The script will generate and save:
- Model performance graphs
- Story-based performance comparison graphs

Graphs will be automatically saved under:
```
metrics/
```

---

## 📈 Outputs

Generated visualizations:
- `ROUGE-1_Model_Performance_Sorted.png`
- `ROUGE-2_Model_Performance_Sorted.png`
- `ROUGE-L_Model_Performance_Sorted.png`
- `BERT_Model_Performance_Sorted.png`
- `Overall Average_Model_Performance_Sorted.png`
- `ROUGE-1_Story_Performance_Sorted.png`
- `ROUGE-2_Story_Performance_Sorted.png`
- `ROUGE-L_Story_Performance_Sorted.png`
- `BERT_Story_Performance_Sorted.png`
- `Overall Average_Story_Performance_Sorted.png`

Each image clearly illustrates how each summarization model or each story performed according to various metrics.

---

## ⚙️ Troubleshooting

- Verify that Model_Performance.xlsx is correctly formatted.
- Verify that Model_Performance_Updated.xlsx is correctly formatted.
- Ensure required libraries are installed and updated.
- Check terminal logs for detailed error information.

---

## 📜 License

This project is licensed under the MIT License. Feel free to modify and distribute it.

