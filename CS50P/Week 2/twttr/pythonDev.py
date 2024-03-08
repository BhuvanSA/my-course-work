import numpy as np


def logistic_function(util, base_utility):
    return np.exp(util) / base_utility


def calculate_probabilities(parameters, data, utilities):
    alternatives = len(utilities)
    probabilities = {}

    base_utility = []

    for i in range(alternatives):
        utility = utilities[i](parameters, data)
        base_utility.append(utility)

    print(base_utility)
    base = sum(np.exp(x) for x in base_utility)

    for i, util in enumerate(base_utility):
        probabilities[f'P{i+1}'] = logistic_function(util, base)

    print(probabilities)
    return probabilities


def utility_function_1(parameters, data):
    # return parameters['β01'] + sum(parameters['β1'] * float(x) for x in data['X1']) + sum(parameters['β2'] * float(x) for x in data['X2'])
    ls = []
    for i in range(len(data['X1'])):
        ls.append(parameters['β01'] + parameters['β1'] *
                  data['X1'][i] + parameters['β2'] * data['X2'][i])
    return ls


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
