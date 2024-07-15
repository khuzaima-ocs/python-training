import pandas as pd

if __name__ == "__main__":
    series = pd.Series(['Hello', "World", "Series", "Tournament"], [66,55,44,77])

    print(series)
    print("-------------")
    print( series[66])
    print("-------------")
    print(series.iloc[1])
    print("-------------")
    print(series.count())
    print("-------------")
    print(series.head(2))
    print("-------------")
    print(series.tail(2))
    print("-------------")
    print(series.sort_values())
    print("-------------")
    print(series.sort_index())



