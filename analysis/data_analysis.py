import pandas as pd
import matplotlib.pyplot as plt
import os

# 移动均线计算
def calculate_moving_average(df, window):
    df[f"MA{window}"] = df["收盘"].rolling(window=window).mean()
    return df

# 绘制价格趋势和移动均线
def plot_stock_data(symbol):
    file_path = f"data/{symbol}_history.csv"
    if not os.path.exists(file_path):
        print(f"{file_path} 不存在，请先运行主脚本获取数据。")
        return

    df = pd.read_csv(file_path)
    df["日期"] = pd.to_datetime(df["日期"])
    df = df.sort_values("日期")
    df = calculate_moving_average(df, 10)
    df = calculate_moving_average(df, 20)

    plt.figure(figsize=(12, 6))
    plt.plot(df["日期"], df["收盘"], label="收盘价")
    plt.plot(df["日期"], df["MA10"], label="10日均线")
    plt.plot(df["日期"], df["MA20"], label="20日均线")
    plt.title(f"{symbol} 收盘价与移动均线")
    plt.xlabel("日期")
    plt.ylabel("价格")
    plt.legend()
    plt.show()

# 示例调用
if __name__ == "__main__":
    plot_stock_data("000001")
