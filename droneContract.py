'''

    This script demonstrate how to exploit the droneContract smart contract.

'''


import tonos_ts4.ts4 as ts4

# Set a directory where the artifacts of the used contracts are located
ts4.set_tests_path('')

# Toggle to print additional execution info
ts4.set_verbose(False)

#Load the contract
dron = ts4.BaseContract('droneContract', {})



class dron(ts4.BaseContract):
    def __init__(self):
        self.create_keypair()
        # We pass a public key to the constructor that will identify the contract owner
        super(dron, self).__init__('droneContract', {}, pubkey = self.public_key_)

    # Create a method to call setNumber without the owner's signature
    def setNumber(self, value, expect_ec = 0):
        return self.call_method('setNumber', {'value': value}, expect_ec = expect_ec)

    # Create a method to call setNumber with the owner's signature
    def setNumber_signed(self, value, expect_ec = 0):
        return self.call_method_signed('setNumber', {'value': value}, expect_ec = expect_ec)

t_number = 123

# Call the unsigned method and expect an error because
# the owner's key is not specified and its validation failed
dron.setNumber(t_number, expect_ec = 101)

# Check that the value has not been changed
assert eq(0, dron.call_getter('m_number'))

# Сall the method by message that signed with owner key
dron.setNumber_signed(t_number)

# Check that the value has changed
assert eq(t_number, dron.call_getter('m_number'))

# Set a new keypair in the contract that is different
# from the one that the contract was deployed with
dron.create_keypair()

# Сall the method by message that signed with foreign key
# and expect an error because the owner's key validation failed
dron.setNumber_signed(t_number * 2, expect_ec = 101)

# Check that the value has not changed
assert eq(t_number, dron.call_getter('m_number'))


# Call an temperature getter and ensure that we received correct value
print("Fetching 'temperature'... ", end='')
expected_value0 = 37
assert eq(expected_value0, dron.call_getter('temp'))
print('ok')

# Call  Light Intensity getter and ensure that we received correct value
print("Fetching 'light Intensity'... ", end='')
expected_value1 = 10
assert eq(expected_value1, dron.call_getter('lightInt'))
print('ok')

# Call the getter and ensure that we received correct address
print("Fetching 'm_address'... ", end='')
expected_address = ts4.Address('0:c4a31362f0dd98a8cc9282c2f19358c888dfce460d93adb395fa138d61ae5069')
assert eq(expected_address, dron.call_getter('m_address'))
print('ok')

#Call Drone Password getter and ensure that we received correct value
print("Fetching 'drone password'... ", end='')
expected_password='password'
assert eq(expected_password, ts4.bytes2str(dron.call_getter('dronePassword')))
print('ok')

#Call Drone Username getter and ensure that we received correct value
print("Fetching 'drone Username'... ", end='')
expected_username='username'
assert eq(expected_username, ts4.bytes2str(dron.call_getter('droneUsername')))
print('ok')

# Call the getter For GPSlocation and ensure that we received correct array value
print("Fetching 'GPSLOCATION'... ", end='')
expected_array = [41,24,12,2,10,26]
assert eq(expected_array, dron.call_getter('GPSlocation'))
print('ok')

# Structures are represented as dictionaries on Python side
print("Fetching 'get_struct'... ", end='')
expected_struct = dict(
    DronePassword  = expected_password,
    DroneUsername = expected_username,
)
assert eq(expected_struct, dron.call_getter('get_struct'))
print('ok')




