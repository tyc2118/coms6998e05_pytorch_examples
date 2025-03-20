from main import main

# ncu --target-processes all -o profile --set full python profile_example.py

try:
    main(['-a', 'alexnet', '--dummy', '--lr', '0.01', '-t', '10'])
except TimeoutError as e:
    print(f"Timeout occurred:\n{str(e)}")

try:
    main(['-a', 'resnet18', '--dummy', '-t', '10'])
except TimeoutError as e:
    print(f"Timeout occurred:\n{str(e)}")