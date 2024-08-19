import json
import sys
import os
import datetime




def main():
    if len(sys.argv) != 2:
        print("Usage: {} <file>".format(sys.argv[0]))
        sys.exit(1)

    if not os.path.exists(sys.argv[1]):
        print("Error: File '{}' not found".format(sys.argv[1]))
        sys.exit(1)

    # Do some sanity checks on the file and dump the name of the file, size, and MAC times
    print("File: {}".format(sys.argv[1]))
    print("Size: {} bytes".format(os.path.getsize(sys.argv[1])))
    print("MAC times: {}".format(os.stat(sys.argv[1]).st_mtime))


    ## TODO - add additional checks
    # 1. Check that the file is a JSON file
    # 2. Check that the JSON file is a list
    # 3. Check that each entry in the list is a dictionary
    # 4. Check that each dictionary has a "title" key
    # 5. Check that the "title" key is a string
    # 6. Check that the dictionary has a "create_time" key
    # 7. Check that the "create_time" key is an integer or float
    # 8. Check that the dictionary has an "update_time" key
    # 9. Check that the "update_time" key is an integer or float
    # 10. Check that the dictionary has a "mapping" key


    with open(sys.argv[1], "r") as f:
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
        print(f"Created : {created.strftime("%Y-%m-%d %H:%M:%S")}")
        updated = datetime.datetime.fromtimestamp(entry["update_time"])
        print(f"Updated : {updated.strftime("%Y-%m-%d %H:%M:%S")}")

        # dump the entry except for "mapping" key
        for key, value in entry.items():
            if key != "mapping":
                print(key, value)
        print()

        # print the mapping keys for each entry
        for key, value in entry["mapping"].items():
            print(f"key : {key} - parent : {value.get('parent')} - children : {value.get('children')}")
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
        #print(tree)

        # print the tree in a human readable format
        def print_tree(node, level=0):
            print("  " * level + node)
            # dump the keys of the node
#            for key, value in entry["mapping"][node].items():
#                if key != "children":
#                    print(f"    {key}")
            # print the author and text of the node, if they exist
            message = entry["mapping"][node]["message"]
            if message is not None:
#                print(f"    Message : {message}")
                author = message.get("author")
                if author is not None:
                    print("  " * level + "    Author : ", author.get("role"))
                text = message.get("content")
                if text is not None:
                    print("  " * level + "    Text : ", text.get("parts"))
#            else:
#                print("    Text : None")
#                print("    Raw : ", entry["mapping"][node])
            # dump node data
            #print(entry["mapping"][node])
            # dump keys of the node
#            for key, value in entry["mapping"][node].items():
#                if key != "children":
#                    print(f"    {key}")


            # recursively call the print_tree function to print the children of the node
            if node in tree:
                for child in tree[node]:
                    print_tree(child, level + 1)

#            if node is not None:
#                # print the node data
#                author = entry["mapping"][node].get("author").get("role")
#                text = entry["mapping"][node].get("content").get("parts")
#                print(f"Author : {author}")
#                print(f"Text : {text}")
#                
                    
        print_tree(root)




if __name__ == "__main__":
    main()

