import sys

file_path = 'E:/PANDIRAAGENCY/SAE-AQIQAH/Report-website/index.html'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    target = '''  .mobile-nav-toggle .bar {
    width: 25px;
    height: 2px;
    background-color: var(--theme-text);
    border-radius: 2px;
    transition: all var(--transition-fast) ease-in-out;
  }'''
    replacement = '''  .mobile-nav-toggle .bar {
    width: 25px;
    height: 2px;
    background-color: var(--theme-text-primary);
    border-radius: 2px;
    transition: all var(--transition-fast) ease-in-out;
  }'''

    if target in content:
        content = content.replace(target, replacement)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Fixed --theme-text')
    else:
        print('Target not found')

except Exception as e:
    print(f'Error: {e}')
