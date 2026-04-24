# ===========================
# FUNCTIONAL MARKDOWN PARSER (comments for future reference)
# ===========================

def parse_markdown_to_html(raw_text):
    # Start with one large "text node" that contains all raw text.
    current_nodes = [{"type": "text", "value": raw_text}]

    # Pipe the nodes one at a time through different separators.
    # Each function returns a new, fine-tuned list of nodes.
    current_nodes = split_nodes_delimiter(current_nodes, "**", "bold")
    current_nodes = split_nodes_delimiter(current_nodes, "*", "italic")
    current_nodes = split_nodes_delimiter(current_nodes, "`", "code")

    # Turns fine tuned nodes list into HTML
    return generate_html(current_nodes)

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    """
    This function receives list of nodes and slices them by type
    into smaller parts by the given delimiter. This is a pure
    function by concept, as it doesn't change the original list,
    but rather builds and returns completely new one.
    """
    new_nodes = []

    for token in old_nodes:
        # If node is already processed (not just "text"),
        # move it to a new list as is.

        if token["type"] != "text":
            new_nodes.append(token)
            continue

        # Split the string on it's separator    
        current_text = token["value"]
        split_text = current_text.split(delimiter)

        for index, value in enumerate(split_text):
            # Skips empty parts, in case separators are one after another.
            if value == "":
                continue

            # Abstract Syntax Tree
            # Due to the split-functon all even indexes are regular
            # text outside their separators, and odd ones
            # are special text inside the separators    
            if index % 2 == 0:
                new_nodes.append({"type": "text", "value": value})
            else:
                new_nodes.append({"type": text_type, "value": value})
    
    return new_nodes


def generate_html(current_nodes):

    """
    This function goes through the syntax tree ja combines it
    back into a string, adding the correct HTML tags based on
    the node type.
    """
    html_output = ""

    for token in current_nodes:
        if token["type"] == "bold":
            html_output += "<b>" + token["value"] + "</b>"
        
        elif token["type"] == "italic":
            html_output += "<i>" + token["value"] + "</i>"
        
        elif token["type"] == "code":
            html_output += "<code>" + token["value"] + "</code>"

        else:
            html_output += token["value"]
    
    return html_output

############ TESTING ############

test_text2 = "This **paragraph** tests if *italic* and bold chaining works in the `code`."

final_html = parse_markdown_to_html(test_text2)

print("HTML ready output: ", final_html)
