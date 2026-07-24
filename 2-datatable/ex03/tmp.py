import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

raw_data = {
        "勉強時間": [2, 5, 1, 8, 4, 7, 3, 6, 9, 5],
        "テスト点数": [45, 70, 30, 95, 60, 85, 55, 75, 98, 65],
        "受験コース": ["文系", "理系", "文系", "理系", "文系", "理系", "文系", "理系", "理系", "文系"],
}
df = pd.DataFrame(raw_data)
sns.set_theme(style='darkgrid')
# sns.set_theme(style='whitegrid')
plt.rcParams["font.family"] = "sans-serif"
# fmri = sns.load_dataset("fmri")
sns.scatterplot(
        data=df,
        x="勉強時間",
        y="テスト点数",
        hue="受験コース",
        s=100,
)

# sns.scatterplot(x="timepoint", y="signal", data=fmri)
plt.title("勉強時間とテスト点数の相関グラフ")
plt.show()
