def restructure_df(df):
    df = df.iloc[2:]
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header

    df = df.reset_index(drop=True)
    return df
