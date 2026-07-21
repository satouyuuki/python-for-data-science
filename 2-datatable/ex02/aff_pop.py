from load_csv import load
import seaborn as sns
from matplotlib import pyplot
# import pandas as pd
# import numpy as np


def population(countries: list[str]) -> None:
    try:
        df = load("population_total.csv")
        idx_list = ['country'] + countries
        print(idx_list)
        filter_df = df[df.index.isin(idx_list)]
        print(filter_df.index)
        df_flipped = filter_df.T
        # df_flipped = df_flipped.set_index('country')
        df_flipped = df_flipped.replace({'M': ''}, regex=True).astype(float)
        print(df_flipped)
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
    except KeyError as e:
        print(f"{type(e).__name__}: {e}")
    else:
        my_colors = ['red', 'blue']
        ax = sns.lineplot(data=df_flipped[countries], palette=my_colors)
        # ax = sns.lineplot(data=df_flipped, palette=my_colors)
        years = df.loc['country'].tolist()
        print(years)
        tick_indices = range(0, len(years), 40)
        tick_labels = [years[i] for i in tick_indices]
        ax.set_xticks(tick_indices, labels=tick_labels)
        ax.set_title("Population Projections")
        ax.set_xlabel("Year")
        ax.set_ylabel("Population")
        ax.legend(title='')
        handles, labels = ax.get_legend_handles_labels()
        print(handles, labels)
        ax.legend(handles=handles[-2:], labels=labels[-2:])
        # ax.legend(labels=countries)
        # ax.set_xticks(range(1800, 2050, 40))
        pyplot.show()


def main():
    population(["Belgium", "France"])
    # population(None)


if __name__ == "__main__":
    main()
