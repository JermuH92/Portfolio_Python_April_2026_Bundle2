def parse_markdown_to_html(raw_text):
    current_nodes = [{"type": "text", "value": raw_text}]
    current_nodes = split_nodes_delimiter(current_nodes, "**", "bold")
    current_nodes = split_nodes_delimiter(current_nodes, "*", "italic")
    current_nodes = split_nodes_delimiter(current_nodes, "`", "code")

    return generate_html(current_nodes)

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


def generate_html(current_nodes):
    html_output = ""

    for token in current_nodes:
        if token["type"] == "bold":
            html_output += "<b>" + token["value"] + "</b>"
        
        elif token["type"] == "italic":
            html_output += "<i>" + token["value"] + "</i>"
        
        elif token["type"] == "code":
            html_output += "<codespan>" + token["value"] + "</codespan>"

        else:
            html_output += token["value"]
    
    return html_output



test_text2 = "This **paragraph** tests if *italic* and bold chaining works in the `code`."

final_html = parse_markdown_to_html(test_text2)

print("HTML ready output: ", final_html)
