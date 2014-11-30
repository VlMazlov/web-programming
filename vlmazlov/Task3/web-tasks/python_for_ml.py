__author__ = 'vlmazlov'

def convert_if_possible(to_test):
    try:
        return int(to_test)
    except ValueError:
        #Do nothing
        pass

    try:
        return float(to_test)
    except ValueError:
        #Do nothing
        pass

    return to_test

def read_dataset(filename):
    dataset = []

    answers = []

    for line in open(filename):
        dataset.append(line.split(',')[:-1])
        answers.append(line.split(',')[-1].strip('\n'))

        for i in range(len(dataset[-1])):
            dataset[-1][i] = convert_if_possible(dataset[-1][i])

    return dataset, answers

dataset, answers = read_dataset('crx.data.txt')
print(dataset)
print(answers)
