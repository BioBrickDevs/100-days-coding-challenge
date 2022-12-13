import pandas


data = pandas.read_csv("Squirrel_Data.csv")

list_of_s = data["Primary Fur Color"].to_list()
print(list_of_s)

print(list_of_s.count("Gray"))

print(list_of_s.count("Black"))

print(list_of_s.count("Cinnamon"))

Squirrel_data ={
    "Gray": int(list_of_s.count("Gray")),
    "Black": int(list_of_s.count("Black")),
    "Cinnamon": int(list_of_s.count("Cinnamon"))
}
print(Squirrel_data)
index_for_data = [i for i in range(3)]

panda_df = pandas.DataFrame(Squirrel_data, index=index_for_data)
print(panda_df)
panda_df.to_csv("data.csv", index="#")