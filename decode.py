#from asyncio.subprocess import SubprocessStreamProtocol
import json
#import sys
#import os
import datetime




def main():
    filename = "single.json"



    with open(filename, "r") as f:
        data = f.read()

    data = json.loads(data)
    # count the number of entries in the data
    print(f"Number of entries : {len(data)}")
    # for each entry in the data, check to see if it includes a title key
    # if it does, print the title on a line of its own
    # if it doesn't, print a dash on a line of its own
    for entry in data:
        print(f"Title : {entry['title']}")
        # decode create_time timestamp
        created = datetime.datetime.fromtimestamp(entry["create_time"])
        print(f"Created : {created.strftime('%Y-%m-%d %H:%M:%S')}")
        updated = datetime.datetime.fromtimestamp(entry["update_time"])
        print(f"Updated : {updated.strftime('%Y-%m-%d %H:%M:%S')}")

        # dump the entry except for "mapping" key
        for key, value in entry.items():
            if key != "mapping":
                print(key, value)
        print()

        # print the mapping keys for each entry
        for key, value in entry["mapping"].items():
            print(f"key : {key} - parent : {value.get('parent')} - children : {value.get('children')}")  # noqa: E501
            if value.get("parent") is None:
                root = key
        print(f"Root : {root}")

        # Build a tree from the mapping keys
        tree = {}
        # iterate over the mapping keys and build the tree, stopping if children = None
        def build_tree(node):
            children = entry["mapping"][node].get("children")
            if children is None:
                return node
            else:
                tree[node] = [build_tree(child) for child in children]
                return node
        build_tree(root)
        

        # print the tree in a human readable format
        def print_tree(node, level=0):
            print("  " * level + node)
            # print the author and text of the node, if they exist
            message = entry["mapping"][node]["message"]
            if message is not None:
                author = message.get("author")
                if author is not None:
                    print("  " * level + "    Author : ", author.get("role"))
                text = message.get("content")
                if text is not None:
                    # truncate text if it is too long
                    output = " ".join(text.get("parts"))
                    print("  " * level + "    Length : ", len(output))
                    if len(output) > 80:
                        print("  " * level + "    Text1 : ", output[:80], "...")
                    else:
                        print("  " * level + "    Text2 : ", output)


            # recursively call the print_tree function to print the children of the node
            if node in tree:
                for child in tree[node]:
                    print_tree(child, level + 1)
                    
        print_tree(root)




if __name__ == "__main__":
    main()

