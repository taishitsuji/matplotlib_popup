# vi-plot-lib

## 概要

CSVデータを簡単に可視化できるPythonライブラリです。
Webアプリ（Streamlit）としても動作し、UIとロジックを分離した設計になっています。

---

## 使い方

```python
from vi_plot_lib import create_plot
import pandas as pd

# CSV読み込み
df = pd.read_csv("data.csv")

# 設定
config = {
    "x": "time",
    "y": ["voltage"],
}

# グラフ生成
fig = create_plot(df, config)
```

---

## 実行方法（アプリ）

```bash
python -m streamlit run app/streamlit_app.py
```

---

## 特徴

* CSVデータの簡単な可視化
* 複数データの同時プロット対応
* 対数スケール（log）対応
* configベースのシンプルなAPI設計

---

## ディレクトリ構成

```
.
├── app/                # Streamlitアプリ
├── src/
│   └── vi_plot_lib/    # ライブラリ本体
├── pyproject.toml
```

---

## 工夫した点

* UI（Streamlit）とデータ処理を分離し、再利用可能な構成にした
* config形式を採用し、拡張しやすい設計にした

---
