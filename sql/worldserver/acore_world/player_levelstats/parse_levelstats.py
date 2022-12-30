import pandas as pd



df = pd.read_csv("player_levelstats.csv")
df = df[["class_id", "level", "new_str", "new_agi", "new_sta", "new_inte", "new_spi"]]

with open("player_levelstats.sql", "w") as sql_file:

    stats = ["str", "agi", "sta", "inte", "spi"]
    for _, row in df.iterrows():
        for stat in stats:
            (
                sql_file.write(
                    "UPDATE player_levelstats SET {} = {} WHERE class = {} AND level = {};\n"
                    .format(
                        stat,
                        row["new_" + stat],
                        row["class_id"],
                        row["level"]
                    )
                )
            )