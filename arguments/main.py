# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def main():
    print(greet("milo"))
    print(force(0.1, 'pluto'))


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
    
    


if __name__ == '__main__':
    main()
