def tokenize_text(raw_text):
    tokens = []
  
    bold_split = raw_text.split('**')

    for index, value in enumerate(bold_split):
        if value == "":
            continue

        if index % 2 != 0:
            tokens.append({"type": "bold", "value": value})
        else:
            tokens.append({"type": "text", "value": value})

    return tokens

def generate_html(tokens):
    html_output = ""

    for token in tokens:
        if token["type"] == "bold":
            html_output += "<b>" + token["value"] + "</b>"
        else:
            html_output += token["value"]
    
    return html_output




test_text = "Hey **Jere**, are you ready to **code** today?"

extracted_tokens = tokenize_text(test_text)
print("Tokens:", extracted_tokens)

final_result = generate_html(extracted_tokens)
print("HTML ready output: ", final_result)
