from load_csv import load
import seaborn as sns
from matplotlib import pyplot
# import pandas as pd


def population(countries: list[str]) -> None:
    try:
        df = load("population_total.csv")
        idx_list = ['country'] + countries
        print(idx_list)
        filter_df = df[df.index.isin(idx_list)]
        print(filter_df.index)
        df_flipped = filter_df.T
        df_flipped = df_flipped.set_index('country')
        df_flipped = df_flipped.replace({'M': ''}, regex=True).astype(float)
        print(df_flipped)
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
    except KeyError as e:
        print(f"{type(e).__name__}: {e}")
    else:
        ax = sns.lineplot(data=df_flipped)
        ax.set_title("Population Projections")
        ax.set_xlabel("Year")
        ax.set_ylabel("Population")
        pyplot.show()


def main():
    population(["Belgium", "France"])
    # population(None)


if __name__ == "__main__":
    main()
