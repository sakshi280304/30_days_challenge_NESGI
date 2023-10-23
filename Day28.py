def hello_world(times):
    if times > 0:
        print("Hello, world")
        hello_world(times - 1)

hello_world(1000)
