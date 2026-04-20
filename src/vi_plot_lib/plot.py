import matplotlib.pyplot as plt
from matplotlib import font_manager

# フォント設定
prop_japanese = font_manager.FontProperties(fname="C:/Windows/Fonts/MSPGOTHIC.TTC")
prop_english = font_manager.FontProperties(fname="./fonts/times.ttf")

def create_plot(df, config):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 6))

    x = config["x"]
    y_list = config["y"]

    # ラベル
    x_label = config.get("label", {}).get("x", x)
    y_label = config.get("label", {}).get("y", "")

    # 範囲
    x_range = config.get("range", {}).get("x", [df[x].min(), df[x].max()])
    y_range = config.get("range", {}).get("y", None)

    # スケール
    x_scale = config.get("scale", {}).get("x", "linear")
    y_scale = config.get("scale", {}).get("y", "linear")

    # スタイル
    font_size = config.get("style", {}).get("font_size", 12)

    # プロット
    for y in y_list:
        ax.plot(df[x], df[y], label=y)

    ax.set_xlabel(x_label, fontsize=font_size)
    ax.set_ylabel(y_label, fontsize=font_size)

    ax.set_xlim(x_range)
    if y_range:
        ax.set_ylim(y_range)

    ax.set_xscale(x_scale)
    ax.set_yscale(y_scale)

    ax.legend()
    ax.grid(True)

    return fig