import json

def big_bang(limit):
    result = []
    for i in range(1, limit + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("BIGBANG")
        elif i % 3 == 0:
            result.append("BIG")
        elif i % 5 == 0:
            result.append("BANG")
        else:
            result.append(str(i))
    return result

def save_to_json(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

if __name__ == "__main__":
    limit = 100
    result = big_bang(limit)
    save_to_json(result, 'output.json')
