data = []

def create(item):
    data.append(item)
    return True

def read():
    return data

def update(index, new_item):
    if 0 <= index < len(data):
        data[index] = new_item
        return True
    return False

def delete(index):
    if 0 <= index < len(data):
        data.pop(index)
        return True
    return False