import numpy as np


def logistic_function(util, base_utility):
    return np.exp(util) / base_utility


def calculate_probabilities(parameters, data, utilities):
    all_utilities = np.array([utility_function(parameters, data)
                              for utility_function in utilities])

    sum_of_utilites = np.sum(np.exp(all_utilities))

    probabilities = [logistic_function(
        utility, sum_of_utilites) for utility in all_utilities]

    return {f'P{i+1}': prob for i, prob in enumerate(probabilities)}


def utility_function_1(parameters, data):
    return parameters['β01'] + sum(parameters['β1'] * float(x) for x in data['X1']) + sum(parameters['β2'] * float(x) for x in data['X2'])


def utility_function_2(parameters, data):
    return parameters['β02'] + sum(parameters['β1'] * float(x) for x in data['X1']) + sum(parameters['β2'] * float(x) for x in data['X2'])


def utility_function_3(parameters, data):
    return parameters['β03'] + sum(parameters['β1'] * float(x) for x in data['Sero']) + sum(parameters['β2'] * float(x) for x in data['Sero'])


data = {
    'X1': [2.0, 3.0, 5.0, 7.0, 1.0, 8.0, 4.0, 5.0, 6.0, 7.0],
    'X2': [1.0, 5.0, 3.0, 8.0, 2.0, 7.0, 5.0, 9.0, 4.0, 2.0],
    'Sero': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

parameters = {
    'β01': 0.1,
    'β1': 0.5,
    'β2': 0.5,
    'β02': 1,
    'β03': 0
}

utilities = [utility_function_1, utility_function_2, utility_function_3]

probabilities = calculate_probabilities(parameters, data, utilities)

# Print and save to a text file
print(probabilities)
with open('output_probabilities.txt', 'w') as file:
    file.write(str(probabilities))
