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


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for token in old_nodes:
        if token["type"] != "text":
            new_nodes.append(token)
            continue

        current_text = token["value"]
        split_text = current_text.split(delimiter)

        for index, value in enumerate(split_text):
            if value == "":
                continue

            if index % 2 == 0:
                new_nodes.append({"type": "text", "value": value})
            else:
                new_nodes.append({"type": text_type, "value": value})
    
    return new_nodes


def generate_html(tokens):
    html_output = ""

    for token in tokens:
        if token["type"] == "bold":
            html_output += "<b>" + token["value"] + "</b>"
        
        elif token["type"] == "italic":
            html_output += "<i>" + token["value"] + "</i>"

        else:
            html_output += token["value"]
    
    return html_output


# test_text = "Hey **Jere**, are you ready to **code** today?"
test_text2 = "This **paragraph** tests if *italic* and bold chaining works in the code."

step_one_tokens = tokenize_text(test_text2)
print("Step one (Bolds) found:", step_one_tokens)

step_two_tokens = split_nodes_delimiter(step_one_tokens, "*", "italic")
print("Step two (Cursives) found:", step_two_tokens)

final_html = generate_html(step_two_tokens)
print("HTML ready output: ", final_html)
