import re

def sanitize_html(input_text):
 
    sanitized_text = re.sub(r'<script[^>]*>.*?</script>', '', input_text, flags=re.IGNORECASE)
    
    sanitized_text = re.sub(r'<script[^>]*>', '', sanitized_text, flags=re.IGNORECASE)

    sanitized_text = re.sub(r'.*?</script[^>]*>', '', sanitized_text, flags=re.IGNORECASE)
    
    sanitized_text = re.sub(r'(<img\s+[^>]*\bon\w+=").*?"(\s*/?>)', r'\1"\2', sanitized_text, flags=re.IGNORECASE)

    return sanitized_text

with open('input.txt', 'r') as file:
    input_text = file.read()

output_text = sanitize_html(input_text)

with open('output.txt', 'w') as file:
    file.write(output_text)
