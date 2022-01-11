import textwrap

text = "this is musk, we are going to mars. I am an alien. Who the heck is this senator. Blooody ***k"
print(f'Wrapped Text: {textwrap.fill(text, 50)}')

print(f'Wrapped Text: {textwrap.fill(text, 50, initial_indent="    ")}')

print(f'Wrapped Text: {textwrap.fill(text, 50, subsequent_indent="    ")}')