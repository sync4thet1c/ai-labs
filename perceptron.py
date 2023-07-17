import numpy as np


def perceptron(weights, inputs, bias):

    model = np.add(np.dot(inputs, weights), bias)
    logit = activation_function(model, type="sigmoid")
    return np.round(logit)


def activation_function(model, type="sigmoid"):

    return {
        "sigmoid": 1 / (1 + np.exp(-model))
    }[type]


def compute(data, logic_gate, weights, bias):
    weights = np.array(weights)
    output = np.array([ perceptron(weights, datum, bias) for datum in data ])

    return output


def print_template(dataset, name, data):
    # act = name[6:]
    print("Logic Function: {}".format(name.upper()))
    print("X0\tX1\tX2\tY")
    toPrint = ["{1}\t{2}\t{3}\t{0}".format(output, *datas) for datas, output in zip(dataset, data)]
    for i in toPrint:
        print(i)


def main():
    dataset = np.array([
      [0, 0, 0],
      [0, 0, 1],
      [0, 1, 0],
      [0, 1, 1],
      [1, 0, 0],
      [1, 0, 1],
      [1, 1, 0],
      [1, 1, 1]
    ])
    gates = {
        "and": compute(dataset, "and", [1, 1, 1], -2),
        "nor": compute(dataset, "nor", [-1, -1, -1], 1),
    }

    for gate in gates:
        print_template(dataset, gate, gates[gate])



if __name__ == '__main__':
    main()