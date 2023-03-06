import math


def get_first_feature_index(headers):
    first_feature = ''

    for header in headers:
        if header.startswith("feature_type"):
            first_feature = header
            break

    check_if_feature_header_is_presented(first_feature)

    return headers.index(first_feature)


def check_if_feature_header_is_presented(header):
    if len(header) == 0:
        raise Exception("There are no feature headers in file!")


def get_mean_stg_values_list(data_list, headers):
    mean_std_list = [[], []]
    first_feature_index = get_first_feature_index(headers)

    for x in range(first_feature_index, len(headers)):
        x_feature = data_list[headers[x]].tolist()

        x_feature_sum = sum(x_feature)
        x_feature_elem_count = len(x_feature)

        mean = x_feature_sum / x_feature_elem_count

        std = 0
        for val in x_feature:
            std += pow((val - mean), 2)

        std = math.sqrt(std / x_feature_elem_count)

        mean_std_list[0].append(mean)
        mean_std_list[1].append(std)

    return mean_std_list


def get_result_headers(headers):
    result_headers = []
    feature_const = "feature_"
    type_const = "type_1_"
    stand_const = "stand_"

    for header in headers:
        new_header = header

        if header.startswith(feature_const):
            split_header_result = header.split(type_const)
            index = split_header_result[1]
            new_header = feature_const + type_const + stand_const + index

        result_headers.append(new_header)

    result_headers.append("max_" + feature_const + type_const + "index")
    return result_headers
