"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    import pandas as pd
    import matplotlib.pyplot as plt
    from pathlib import Path
    import os
    from pathlib import Path

    output_dir = Path("files/plots")

    new_output = Path("files/plots/news.png")

    plt.Figure()

    colors ={
        'Television':'dimgray',
        'Newspaper':'grey',
        'Internet':'tab:blue',
        'Radio':'lightgrey'
    }

    zorder={
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1
    }
    linewidths={
        'Television': 2,
        'Newspaper': 2,
        'Internet': 4,
        'Radio': 2
    }


    news_dir = Path("files/input/news.csv")

    df = pd.read_csv(news_dir, index_col=0)

    for col in df.columns:
        plt.plot(
            df[col],
            color=colors[col],
            label=col,
            zorder=zorder[col],
            linewidth=linewidths[col]    
        )

    plt.title("How people get their news",fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)


    for col in df.columns:
        frist_year = df.index[0]
        plt.scatter(
            x=frist_year,
            y=df[col][frist_year],
            color = colors[col],
            zorder=zorder[col]
        )

        plt.text(
            frist_year -0.2,
            df[col][frist_year],
            col +" "+str(df[col][frist_year])+"%",
            ha='right',
            va='center',
            color=colors[col],
        )

        last_year = df.index[-1]
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color = colors[col],
            zorder=zorder[col]
        )

        plt.text(
            last_year -0.2,
            df[col][last_year],
            str(df[col][last_year])+"%",
            ha='left',
            va='center',
            color=colors[col],
        )
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    plt.tight_layout()
    plt.savefig(new_output)

    plt.show()

pregunta_01()