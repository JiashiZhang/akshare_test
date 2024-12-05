from utils.ak_utils import get_realtime_data, get_stock_history, save_to_csv


def fetch_realtime_data():
    df = get_realtime_data()
    save_to_csv(df, "data/realtime_data.csv")
    print(df.head())  # 打印前几行数据


def fetch_stock_history(symbol, start_date, end_date):
    df = get_stock_history(symbol, start_date, end_date)
    save_to_csv(df, f"data/{symbol}_history.csv")
    print(df.head())  # 打印前几行数据


if __name__ == "__main__":
    # 获取 A 股实时数据
    fetch_realtime_data()

    # 获取单只股票历史数据 (如 平安银行 000001.SZ)
    fetch_stock_history("000001", "20230101", "20231231")
