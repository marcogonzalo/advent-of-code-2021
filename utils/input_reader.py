def get_input_array(filename, parse_as='string'):
    with open(filename, 'r') as f:
        lines = f.readlines()
        input = []
        for line in lines:
            value = line.strip()
            if parse_as == 'integer':
                value = int(value)
            elif parse_as == 'float':
                value = float(value)
            input.append(value)
        return input
