from main import main

# ncu --target-processes all -o profile --set full python profile_example.py

try:
    main(['-a', 'alexnet', '--dummy', '--lr', '0.01'])
except TimeoutError as e:
    print(f"Timeout occurred:\n{str(e)}")
