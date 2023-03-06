import utils.helpers as hlp
from pandas import read_csv
import csv

file_name = "test.csv"

# constants
feature_const = "feature_"
type_const = "type_1_"
stand_const = "stand_"

data = read_csv(file_name)

headers = data.columns.tolist()

# get index of first feature
first_feature_index = hlp.get_first_feature_index(headers)

result = [hlp.get_result_headers(headers)]


mean_std_list = hlp.get_mean_stg_values_list(data, headers)

with open(file_name, 'r') as file:
    csvFileReader = csv.reader(file)

    for row in csvFileReader:
        if len(row[0]) == 0:
            continue

        std_row = []

        max_val = -999
        max_val_index = -1

        for index, item in enumerate(row):
            value = item

            if index >= first_feature_index:
                feature_index = index - first_feature_index
                value = (float(item) - mean_std_list[0][feature_index]) / mean_std_list[1][feature_index]

                if value > max_val:
                    max_val = value
                    max_val_index = feature_index

            std_row.append(value)

        std_row.append(max_val_index)
        result.append(std_row)


file = open('out.csv', 'w+', newline='')

with file:
    write = csv.writer(file)
    write.writerows(result)

