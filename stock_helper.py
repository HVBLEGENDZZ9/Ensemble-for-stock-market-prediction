def prepare_data(df):
    import pandas as pd
    import numpy as np
    import pandas_ta as ta
    import matplotlib.pyplot as plt
    # bollinger bands
    bbands = df.ta.bbands(close='Close', length=20)
    # macd indicator
    macd = df.ta.macd(close='Close')
    macd.drop(["MACD_12_26_9", "MACDs_12_26_9"], axis=1, inplace=True)
    # rsi indicator
    rsi = df.ta.rsi(close='Close').to_frame()
    # aroon indicator
    aroon = df.ta.aroon(close="Close")
    aroon.drop(["AROOND_14", "AROONU_14"], axis=1, inplace=True)
    df.drop(["Open", "High", "Low", "Adj Close", "Volume"], axis=1, inplace=True)
    df_ti = pd.concat([df, bbands, macd, rsi, aroon], axis=1)
    df_ti.dropna(inplace=True)
    window_size = 7
    horizon = 1
    df_ti_win = df_ti.copy()
    for i in range(window_size):
        df_ti_win[f'Close + {i+1}'] = df_ti["Close"].shift(periods=i+1, axis=0)
        df_ti_win[f'BBL_20_2.0 + {i+1}'] = df_ti["BBL_20_2.0"].shift(
            periods=i+1, axis=0)
        df_ti_win[f'BBM_20_2.0 + {i+1}'] = df_ti["BBM_20_2.0"].shift(
            periods=i+1, axis=0)
        df_ti_win[f'BBU_20_2.0 + {i+1}'] = df_ti["BBU_20_2.0"].shift(
            periods=i+1, axis=0)
        df_ti_win[f'BBB_20_2.0 + {i+1}'] = df_ti["BBB_20_2.0"].shift(
            periods=i+1, axis=0)
        df_ti_win[f'BBP_20_2.0 + {i+1}'] = df_ti["BBP_20_2.0"].shift(
            periods=i+1, axis=0)
        df_ti_win[f'MACDh_12_26_9 + {i+1}'] = df_ti["MACDh_12_26_9"].shift(
            periods=i+1, axis=0)
        df_ti_win[f'RSI_14 + {i+1}'] = df_ti["RSI_14"].shift(
            periods=i+1, axis=0)
        df_ti_win[f'AROONOSC_14 + {i+1}'] = df_ti["AROONOSC_14"].shift(
            periods=i+1, axis=0)
    x = df_ti_win.dropna().drop("Close", axis=1).astype(np.float32)
    y = df_ti_win.dropna()["Close"].astype(np.float32)
    return x, y
