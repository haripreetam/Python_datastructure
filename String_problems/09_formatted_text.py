import textwrap

def formatted_text(text,width):
    print(textwrap.fill(text,width=width))

text = "Python is a widely used high-level, general-purpose, interpreted, dynamic programming language."
formatted_text(text,width=30)