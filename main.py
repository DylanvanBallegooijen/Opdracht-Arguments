# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# part 1


def main():
    print(greet(name='Bob'))
    print(force(81, 'mars'))
    print(pull(100, 100, 5))


def greet(name, greeting='Hello, <name>!'):
    return greeting.replace('<name>', name)

# part 2


def force(mass, body='earth'):
    surface_gravity = {'sun': 274,
                       'jupiter': 24.9,
                       'neptune': 11.2,
                       'saturn': 10.4,
                       'earth': 9.8,
                       'uranus': 8.9,
                       'venus': 8.9,
                       'mars': 3.7,
                       'mercury': 3.7,
                       'moon': 1.6,
                       'pluto': 0.6}
    return mass * surface_gravity[body]

# part 3


def pull(m1, m2, d):
    return ((6.674E-11) * ((m1 * m2))/d**2)


if __name__ == '__main__':
    main()
