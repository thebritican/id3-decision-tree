from collections import defaultdict


def is_homogeneous(examples, positive):
    homogeneous = True
    for example in examples:
        if (positive is True and example[-1] is False) or (positive is False and example[-1] is True):
            homogeneous = False
    return homogeneous


def most_common_value(examples):
    class_labels = get_class_label_values(examples)
    if class_labels[True] >= class_labels[False]:
        return True
    return False


def subset(examples, feature_index, feature_value):
    return [example for example in examples if example[feature_index] == feature_value]


def get_class_label_values(examples):
    class_label_values = {True: 0, False: 0}

    class_label_index = len(examples[0]) - 1

    for example in examples:
        class_label = example[class_label_index]
        if class_label in class_label_values:
            class_label_values[class_label] += 1
    return class_label_values


def get_example_values_for_feature(examples, schema, feature_index):

    """
    :param examples: Example data
    :param feature_index: The index you of the feature you want
    :return: A dict containing the possible feature values mapped to the count associated with each.
    """
    feature_values = defaultdict(int)
    print(feature_index)
    features = schema[feature_index]
    print(features)
    test = features.values
    print(test)
    print(type(test))
    for feature_value in test:
        feature_values[feature_value] = 0
    for i in range(0, len(examples)):
        example_value = examples[i][feature_index]
        if example_value in feature_values:
            feature_values[example_value] += 1
    return feature_values