def second_index(world, letter):
    result = world.find(letter, world.find(letter)+1)
    return result

world = "Hello, hello"
letter = "lo"
print(second_index(world, letter))
