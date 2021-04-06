

def hello():
    with open('../README.md') as f:
        print(f.read())

if __name__ == '__main__':
    hello()