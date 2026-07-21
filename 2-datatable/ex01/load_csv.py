import pandas as pd


def make_lalign_formatter(df, cols=None):
    if cols is None:
        cols = df.columns

    formatters = {}
    for col in cols:
        formatters[col] = lambda x: "" if pd.isna(x) else f"{x:<}"
    return formatters


def load(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path, index_col=0, header=None)
    except FileNotFoundError as e:
        print(f"{type(e).__name__}: {e.strerror}")
    except pd.errors.EmptyDataError as e:
        print(f"{type(e).__name__}: {e}")
    except pd.errors.ParserError as e:
        print(f"{type(e).__name__}: {e}")
    else:
        array = df.to_numpy()
        print(f"Loading dataset of dimensions {array.shape}")
        print(df.to_string(max_cols=10, header=False, index_names=False))
        return df


def main():
    load()


if __name__ == "__main__":
    main()
