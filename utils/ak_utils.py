import akshare as ak
import pandas as pd
import os

# 获取 A 股实时行情数据
def get_realtime_data():
    df = ak.stock_zh_a_spot()
    return df

# 获取单只股票的历史数据
def get_stock_history(symbol, start_date, end_date, adjust="qfq"):
    df = ak.stock_zh_a_hist(symbol=symbol, period="daily", start_date=start_date, end_date=end_date, adjust=adjust)
    return df

# 保存数据到 CSV
def save_to_csv(df, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)
    print(f"数据已保存至 {file_path}")
