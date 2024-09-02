import json
import datetime
import pprint




def main():
    filename = "data/conversations.json"


    # Load Claude JSON Conversations Export
    with open(filename, "r") as f:
        data = json.load(f)
        # count the number of conversations in the data
        print(f"Number of conversations : {len(data)}")
        # list keys (per entry)
        keys = list(data[0].keys())
        print(keys)

        # Print Chat Message Keys (per entry)
        chat_keys = list(data[0]['chat_messages'][0].keys())
        print(chat_keys)



    # for each entry in the data, check to see if it includes a title key
    # if it does, print the title on a line of its own
    # if it doesn't, print a dash on a line of its own
     # print the fields for each data object
    # print the fields for each data object
    # for i, entry in enumerate(data, start=1):
    #     print(f"Entry {i}:")
    #     for field in ['uuid', 'name', 'created_at', 'updated_at']:
    #        print(f"  {field}: {entry[field]}")
#        for key, value in entry.items():
##            print(f"  {key}: {value}")
    #    print()


if __name__ == "__main__":
    main()

