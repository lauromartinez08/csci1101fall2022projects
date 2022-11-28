import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("game-ratings-by-top-10-platforms.csv")

#group by metrics
df_platform_follow = df.groupby(["platform_name"])["follow_count"].sum().reset_index()

df_platform_folllow = df_platform_follow.rename(columns = {"follow_count": "total_follow"})

df_platform_type = df.groupby(["platform_name"])["type_count"].sum().reset_index()

df_platform_type = df_platform_type.rename(columns = {"type_count": "total_types"})

#analyze data
bar_width = 0.4

plt.bar(df_platform_follow.index - bar_width / 2, df_platform_follow["total_follows"], color = "blue", label = "number of follows", width = bar_width)
plt.bar(df_platform_type.index - bar_width /2, df_platform_type["total_types"], color = "red", label = "Number of Types", width = bar_width)

plt.xticks(df_platform_follow.index, df_platform_follow["platform_name"])

plt.legend(loc = "upper left")

plt.show()