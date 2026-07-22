import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# 5. 単位付き文字列（M, k）を数値に変換する関数
def parse_shorthand(val_str):
    if not isinstance(val_str, str):
        return val_str
    val_str = val_str.upper().strip()
    multipliers = {'K': 1_000, 'M': 1_000_000, 'B': 1_000_000_000}
    if val_str[-1] in multipliers:
        return int(float(val_str[:-1]) * multipliers[val_str[-1]])
    return int(float(val_str))


def population(countries: list[str]) -> None:
    try:
        # 1. CSVデータの読み込み
        df = pd.read_csv('population_total.csv')

        # ★ 2. プロットしたい2つの国を抽出する（例: Japan と America）
        countries_to_plot = ['Belgium', 'France']
        df_selected = df[df['country'].isin(countries_to_plot)]

        # ★ 3. データを「縦長形式」に変形（melt）してSeaborn用に整える
        # これにより、列に並んでいた「年（1800, 1801...）」が縦一列のデータになります
        df_melted = df_selected.melt(
            id_vars=['country'],
            var_name='Year',
            value_name='Value_Str'
        )
        print(df_melted.info())

        # 4. 年（Year）を文字列から整数（int）に変換し、1800〜2050年に絞り込む
        df_melted['Year'] = df_melted['Year'].astype(int)
        df_filtered = df_melted[(df_melted['Year'] >= 1800) & (df_melted['Year'] <= 2050)].copy()
        print(df_filtered.info())
        # 数値変換を適用
        df_filtered['Value_Num'] = df_filtered['Value_Str'].apply(parse_shorthand)

        # x='Year'（横軸は年）、y='Value_Num'（縦軸は数値）、hue='country'（国ごとに色分け）
        ax = sns.lineplot(data=df_filtered, x='Year', y='Value_Num', hue='country', linewidth=2)

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles=handles, labels=labels, title="")

        # X軸の表示範囲を1800〜2050にぴったり合わせる（lineplotなのでこれで正常に動きます）
        ax.set_xlim(1800, 2050)

        # Y軸の目盛りを動的に3分割（4点表示）＆ M表記にカスタマイズ
        ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=4))
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x*1e-6:g}M' if x >= 1e6 else f'{x:g}'))

        plt.title("Population Projections")
        plt.ylabel("Population")
        plt.show()
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
    except KeyError as e:
        print(f"{type(e).__name__}: {e}")


def main():
    population(["Belgium", "France"])
    # population(None)


if __name__ == "__main__":
    main()
