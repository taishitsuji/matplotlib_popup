# vi-plot-lib

## 概要
CSVデータを簡単に可視化できるPythonライブラリです。
Streamlitアプリとしても動作します。

## 使い方

```python
from vi_plot_lib import create_plot
import pandas as pd

df = pd.read_csv("data.csv")

config = {
    "x": "time",
    "y": ["voltage"],
}

fig = create_plot(df, config)

実行方法

python -m streamlit run app/streamlit_app.py

特徴
・CSV可視化
・複数プロット
・対数スケール対応
