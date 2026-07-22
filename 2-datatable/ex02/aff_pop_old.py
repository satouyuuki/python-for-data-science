from load_csv import load
import seaborn as sns
from matplotlib import pyplot, ticker
# import pandas as pd
# import numpy as np


def parse(val: str):
    if not isinstance(val, str):
        return val
    val = val.upper().strip()
    multipliers = {'K': 1_000, 'M': 1_000_000, 'B': 1_000_000_000}
    if val[-1] in multipliers:
        unit = val[-1]
        return int(float(val[:-1]) * multipliers[unit])
    return int(float(val))


def y_fmt(x, _):
    if x >= 1_000_000_000:
        return f'{x * 1e-9:g}B'
    elif x >= 1_000_000:
        return f'{x * 1e-6:g}M'
    elif x >= 1_000:
        return f'{x * 1e-3:g}K'
    return f'{x:g}'


def population(countries: list[str]) -> None:
    try:
        df = load("population_total.csv")
        idx_list = ['country'] + countries
        print(idx_list)
        filter_df = df[df.index.isin(idx_list)]
        # print(filter_df.index)
        df_flipped = filter_df.T
        # df_flipped = df_flipped.set_index('country')
        df_flipped['country'] = df_flipped['country'].astype(int)
        df_flipped = df_flipped[(df_flipped['country'] >= 1800) & (df_flipped['country'] <= 2050)].copy()
        df_flipped['country'] = df_flipped['country'].astype(str)

        print(df_flipped)
        # print(df_flipped['country'].astype(int).to_list())
        for country in countries:
            df_flipped[country] = df_flipped[country].apply(parse)
        # df_flipped = df_flipped.replace({'M': ''}, regex=True).astype(float)
        print(df_flipped.info())
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
    except KeyError as e:
        print(f"{type(e).__name__}: {e}")
    else:
        my_colors = ['red', 'blue']
        ax = sns.lineplot(data=df_flipped[countries], palette=my_colors)
        # ax = sns.lineplot(data=df_flipped, palette=my_colors)
        # years = df.loc['country'].tolist()
        # # print(years)
        # tick_indices = range(0, len(years), 40)
        # tick_labels = [years[i] for i in tick_indices]
        # ax.set_xticks(tick_indices, labels=tick_labels)
        # ax.set_xlim(1800, 2050)
        ax.set_title("Population Projections")
        ax.set_xlabel("Year")
        ax.set_ylabel("Population")
        ax.legend(title='')
        handles, labels = ax.get_legend_handles_labels()
        # print(handles, labels)
        ax.legend(handles=handles[-2:], labels=labels[-2:])
        # ax.set_xlim(df_flipped['country'].min(), df_flipped['country'].max())
        # ax.legend(labels=countries)
        # ax.set_xticks(range(1800, 2050, 40))
        ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=4))
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(y_fmt))
        pyplot.show()


def main():
    population(["Belgium", "France"])
    # population(None)


if __name__ == "__main__":
    main()
