class Commands:
    def __init__(self):
        self.x = 10

    def show():
        print('a - for adding new item')
        print('a - for adding new item')
        print('a - for adding new item')
        print('a - for adding new item')

    def cmd_a(self):
        """ This is a command for adding item

        """
        print('Adding item')

    def cmd_d(self):
        print('Delete item')

    def cmd_e(self):
        print('Edit item')

    def cmd_z(self):
        print('Zetting item')

    """
    def __setattr__(self, name, value):
        if name == 'x' and type(value) != int:
            raise ValueError("x should be an integer")

        print(f"setting {name} to {value}")
    """

    def __getattr__(self, name):
        return lambda: print(f'Invalid attribute: {name}')


cmd = input("What to do (a, d or e): ")


"""
commands = {'a': 'add_item',
            'd': 'delete_item',
            'e': 'edit_item'}
"""

# globals()[commands.get(cmd)]()
# commands.get(cmd)()

commands_obj = Commands()

# commands_obj.x = 20
# commands_obj.x = "adsf"

getattr(commands_obj, f"cmd_{cmd}")()

"""
if cmd == 'a':
    add_item()
elif cmd == 'd':
    delete_item()
elif cmd == 'e':
    edit_item()
"""
