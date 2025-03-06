# performance_comparison.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_path = "./metrics/Model_Performance_Updated.xlsx"
df = pd.read_excel(file_path)

# Numeric columns to process
numeric_columns = [
    'ROUGE-1 Precision', 'ROUGE-1 Recall', 'ROUGE-1 F1',
    'ROUGE-2 Precision', 'ROUGE-2 Recall', 'ROUGE-2 F1',
    'ROUGE-L Precision', 'ROUGE-L Recall', 'ROUGE-L F1',
    'BERT Precision', 'BERT Recall', 'BERT F1'
]

# Convert columns to numeric
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Fill missing values
df.fillna(0, inplace=True)

# Extract F1-scores for convenience
df['ROUGE-1'] = df['ROUGE-1 F1']
df['ROUGE-2'] = df['ROUGE-2 F1']
df['ROUGE-L'] = df['ROUGE-L F1']
df['BERT']    = df['BERT F1']

# Calculate overall average (only F1-scores)
df['Overall Average'] = df[['ROUGE-1', 'ROUGE-2', 'ROUGE-L', 'BERT']].mean(axis=1)

# Color Palette
palette = sns.color_palette("hsv", len(df['Model Name'].unique()))

# Calculate and plot averages by model
model_means = {}
for metric_name in ['ROUGE-1', 'ROUGE-2', 'ROUGE-L', 'BERT', 'Overall Average']:
    model_means[metric_name] = df.groupby('Model Name')[metric_name].mean()
    means = model_means[metric_name].sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    bars = plt.bar(means.index, means.values, color=palette, edgecolor='black')
    plt.title(f'{metric_name} Model Performance', fontsize=14)
    plt.ylabel('Score', fontsize=12)
    plt.xlabel('Model', fontsize=12)
    plt.ylim(0, 1)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Display values on each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.02, f'{yval:.3f}', 
                 ha='center', fontsize=10)

    plt.tight_layout()
    plt.savefig(f'./metrics/{metric_name}_Model_Performance_Sorted.png')
    plt.show()

# Calculate and plot averages by story name
grouped_by_story = {}
for metric_name in ['ROUGE-1', 'ROUGE-2', 'ROUGE-L', 'BERT', 'Overall Average']:
    grouped_by_story[metric_name] = df.groupby('Story Name')[metric_name].mean()
    means = grouped_by_story[metric_name].sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    bars = plt.bar(means.index, means.values, color=palette, edgecolor='black')
    plt.title(f'{metric_name} Story Performance', fontsize=14)
    plt.ylabel('Score', fontsize=12)
    plt.xlabel('Story', fontsize=12)
    plt.ylim(0, 1)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Display values above each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.02, f'{yval:.3f}', 
                 ha='center', fontsize=10)

    plt.tight_layout()
    plt.savefig(f'./metrics/{metric_name}_Story_Performance_Sorted.png')
    plt.show()

print("All plots have been successfully saved.")