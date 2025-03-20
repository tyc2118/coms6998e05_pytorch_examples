from main import main
import time

# ncu --target-processes all -o profile --set full python profile_example.py

try:
    main(['-a', 'alexnet', '--dummy', '--lr', '0.01', '-t', '20'])
except TimeoutError as e:
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"Timeout occurred at {current_time}:\n{str(e)}")

try:
    main(['-a', 'resnet18', '--dummy', '-t', '20'])
except TimeoutError as e:
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"Timeout occurred at {current_time}:\n{str(e)}")