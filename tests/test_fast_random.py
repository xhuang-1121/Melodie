from Melodie.boost.fastrand import sample


def test_sample():
    # dense sample, 3 from 5
    value_dict = {i: 0 for i in range(5)}
    mean = 30000 * (1 / 6)
    stdev = 30000 * (1 / 6) * (1 - 1 / 6)
    for _ in range(10000):
        sampled = sample(list(range(5)), 3)
        for value in sampled:
            value_dict[value] += 1
    for value in value_dict.values():
        assert 5800 < value < 6200
    print(value_dict, mean, stdev)
    # sparse sample, 2 from 200
    value_dict = {i: 0 for i in range(200)}
    l = list(range(200))
    for _ in range(100000):
        sampled = sample(l, 2)
        for value in sampled:
            value_dict[value] += 1
    print(value_dict)
    for value in value_dict.values():
        assert 800 < value < 1200
