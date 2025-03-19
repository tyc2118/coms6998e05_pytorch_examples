from main import main

model_name = ['alexnet', 'resnet18']
for name in model_name:
    try:
        main(['-a', name, '--dummy', '-t', '10'])
    except TimeoutError as e:
        print(f"Timeout occurred:\n{str(e)}")