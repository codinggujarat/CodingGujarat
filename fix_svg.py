import re

def fix_file(filename, x_val):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Collapse the formatting spaces that got added.
    content = re.sub(r'</tspan>\s+<tspan', '</tspan><tspan', content)
    content = re.sub(r'</tspan>:\s+<tspan', '</tspan>:<tspan', content)
    content = re.sub(r'</tspan>\s*<tspan class="key">', '</tspan><tspan class="key">', content)
    content = re.sub(r'</tspan>\.\s+<tspan', '</tspan>.<tspan', content)
    content = re.sub(r'\(\s+<tspan', '( <tspan', content)
    content = re.sub(r'</tspan>\s+<tspan class="value"', '</tspan><tspan class="value"', content)
    content = re.sub(r'{\s+<tspan', '{<tspan', content)
    content = re.sub(r'</tspan>}', '</tspan>}', content)
    content = re.sub(r'\|\s+<tspan', '| <tspan', content)
    content = re.sub(r'\+\+</tspan>,\s+<tspan', '++</tspan>, <tspan', content)
    content = re.sub(r'--</tspan>\s+\)', '--</tspan> )', content)

    # We need to find the right panel <text> block. It contains @CodingGujarat.
    # It might be x="500" or x="520"
    text_block_match = re.search(r'(<text[^>]*x="' + x_val + r'"[^>]*>)(.*?)(</text>)', content, re.DOTALL)
    if text_block_match:
        inner = text_block_match.group(2)
        # Remove all newlines and spaces that are purely for indentation
        inner = re.sub(r'\n\s+', '', inner)
        
        # Add newlines back before the line starts so source code isn't 1 giant line
        inner = inner.replace('<tspan x="' + x_val + '"', '\n<tspan x="' + x_val + '"')
        
        content = content[:text_block_match.start(2)] + '\n' + inner.strip() + '\n' + content[text_block_match.end(2):]

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

fix_file('dark_mode.svg', '500')
fix_file('light_mode.svg', '520')
