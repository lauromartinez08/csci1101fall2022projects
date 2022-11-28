import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("game-ratings-by-top-10-genres.csv")

#group by metrics
df_genre_follow = df.groupby(["genre_name"])["follow_count"].sum().reset_index()

df_genre_folllow = df_genre_follow.rename(columns = {"follow_count": "total_follow"})

df_genre_type = df.groupby(["genre_name"])["type_count"].sum().reset_index()

df_genre_type = df_genre_type.rename(columns = {"type_count": "total_types"})

#analyze data
bar_width = 0.4

plt.bar(df_genre_follow.index - bar_width / 2, df_genre_follow["total_follows"], color = "blue", label = "number of follows", width = bar_width)
plt.bar(df_genre_type.index - bar_width /2, df_genre_type["total_types"], color = "red", label = "Number of Types", width = bar_width)

plt.xticks(df_genre_follow.index, df_genre_follow["genre_name"])

plt.legend(loc = "upper left")

plt.show()