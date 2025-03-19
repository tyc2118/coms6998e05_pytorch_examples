from main import main

try:
    main(['-a', 'alexnet', '--dummy', '-t', '10'])
except TimeoutError as e:
    print(f"Timeout occurred while running alexnet:\n{str(e)}")
try:
    main(['-a', 'resnet18', '--dummy', '-t', '10'])
except TimeoutError as e:
    print(f"Timeout occurred while running resnet18:\n{str(e)}")