from load_csv import load
import seaborn as sns
from matplotlib import pyplot


def life_expectancy(country: str) -> None:
    try:
        assert country is not None and country != "", "invalid input"
        df = load("life_expectancy_years.csv")
        ax = sns.lineplot(data=df, x=df.loc["country"], y=df.loc[country])
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
    except KeyError as e:
        print(f"{type(e).__name__}: {e}")
    else:
        ax.set_title(f"{country} Life expectancy Projections")
        ax.set_xlabel("Year")
        ax.set_ylabel("Life expectancy")
        pyplot.show()


def main():
    # life_expectancy("France")
    # life_expectancy("Japan")
    life_expectancy("Japans")
    # life_expectancy("")
    # life_expectancy(None)


if __name__ == "__main__":
    main()
# columnsは1~301のx軸(int64)
# print(df.columns)
# indexはcountry~Zimbabweのy軸(objectタイプ、196 len)
# print(type(df.index))
# valuesは中身
# print(df.values)
# print(df.info())
