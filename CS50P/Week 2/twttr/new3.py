import numpy as np


def calculate_probabilities(parameters, data, utilities):
    # Error handling for mismatched dimensions
    for util in utilities:
        utility_values = util(parameters, data)
        if utility_values.shape[0] != len(data['X1']):
            raise ValueError(f"Mismatched dimensions in utility function {util.__name__}. "
                             f"Expected {len(data['X1'])} data points, got {utility_values.shape[0]}.")

    utility_values = np.array([util(parameters, data) for util in utilities])
    normalization_factor = np.sum(np.exp(utility_values), axis=0)
    probabilities = np.exp(utility_values) / normalization_factor

    return {f'P{i+1}': prob.tolist() for i, prob in enumerate(probabilities)}


def utility_function_1(parameters, data):
    return parameters['β01'] + parameters['β1'] * data['X1'] + parameters['β2'] * data['X2']


def utility_function_2(parameters, data):
    return parameters['β02'] + parameters['β1'] * data['X1'] + parameters['β2'] * data['X2']


def utility_function_3(parameters, data):
    return parameters['β03'] + parameters['β1'] * data['Sero'] + parameters['β2'] * data['Sero']


data = {
    'X1': np.array([2.0, 3.0, 5.0, 7.0, 1.0, 8.0, 4.0, 5.0, 6.0, 7.0]),
    'X2': np.array([1.0, 5.0, 3.0, 8.0, 2.0, 7.0, 5.0, 9.0, 4.0, 2.0]),
    'Sero': np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
}

parameters = {
    'β01': 0.1,
    'β1': 0.5,
    'β2': 0.5,
    'β02': 1,
    'β03': 0
}

utilities = [
    utility_function_1,
    utility_function_2,
    utility_function_3
]


def main():
    try:
        probabilities = calculate_probabilities(parameters, data, utilities)

        # Print and save to a text file
        print(probabilities)
        with open('output_probabilities.txt', 'w') as file:
            file.write(str(probabilities))

    except ValueError as e:
        print(f"Error: {e}")
