import pandas as pd
import matplotlib.pyplot as plt

def analyze_data():
    data = {
        'Player Name': [
            'Rilee Russouw', 'Phil Salt', 'Yash Dhull',
            'Axer Patel', 'Lalit Yadav', 'Aman Khan', 'Kuldeep Yadav'
        ],
        'CP': [2, 1, 3, 2, 1, 4, 3],
        'GT': [1, 2, 1, 3, 2, 1, 0],
        'C':  [1, 0, 2, 1, 1, 0, 1],
        'DC': [0, 1, 0, 0, 0, 0, 1],
        'S':  [0, 0, 0, 1, 0, 0, 0],
        'RO': [0, 1, 0, 0, 0, 1, 0],
        'MR': [0, 0, 1, 0, 0, 0, 0],
        'DH': [1, 0, 0, 0, 1, 0, 1],
        'RS': [2, -1, 3, 0, -2, 1, 4]
    }

    df = pd.DataFrame(data)

    # Performance Score formula
    df['PS'] = (
        df['CP'] * 1 +
        df['GT'] * 1 +
        df['C'] * 3 -
        df['DC'] * 3 +
        df['S'] * 3 +
        df['RO'] * 3 -
        df['MR'] * 2 +
        df['DH'] * 2 +
        df['RS']
    )

    # Save text report
    with open("reports/analysis_report.txt", "w") as f:
        for _, row in df.iterrows():
            f.write(f"{row['Player Name']}: Performance Score = {row['PS']}\n")

    # Create bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(df['Player Name'], df['PS'], color='royalblue')
    plt.xlabel("Player Name")
    plt.ylabel("Performance Score")
    plt.title("IPL Player Performance Scores")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("reports/score_trends.png")

    print("✅ Analysis complete. Output saved in 'reports/' folder.")
