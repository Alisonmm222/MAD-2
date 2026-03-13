import pandas as pd

df = pd.read_csv("./data/evaluation mad/convergence_of_480_toxic_random_discussions_topic_16.csv", sep =",")

print(df.columns)

print(df["reason_for_convergence"].agg("value_counts"))
print(df["which_agent_is_toxic"].agg("value_counts"))
df["toxicity_level"].agg("value_counts")

df.groupby("toxicity_level")
