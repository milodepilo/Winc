# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'


# Add your code after this line
def main():
    print(greet("milo"))
    print(force(0.1, 'pluto'))
    print(pull(0.1,5.972 * 10 ** 24,6371))


def greet(name, greeting='Hello, <name>!'):
    greeting = greeting.replace('<name>', name)
    return greeting


def force(mass, body='earth'):
    surface_graivty = {
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.1,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6
    }
    return (mass * surface_graivty.get(body))

def pull(m1,m2,d):
    G = 6.674 * 10 ** -11
    F = G * ((m1 * m2) / d **2) 
    return F

if __name__ == '__main__':
    main()
