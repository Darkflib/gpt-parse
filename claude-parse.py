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
        print("Debug Data: Keys per Entry/Keys per Chat_messages")
        # list keys (per entry)
        keys = list(data[0].keys())
        print(keys)

        # Print Chat Message Keys (per entry)
        chat_keys = list(data[0]['chat_messages'][0].keys())
        print(chat_keys)
        tz_format = '%Y-%m-%dT%H:%M:%S.%fZ'
        for i, entry in enumerate(data, start=1):
    #       for field in ['uuid', 'name', 'created_at', 'updated_at']:
    #           print(f"  {field}: {entry[field]}")
            print(f"{i} Title : {entry['name']} [{entry['uuid']}]")

            # Timestamp Code taken from Darkflib
            # decode create_time timestamp
            created = datetime.datetime.strptime(entry["created_at"], tz_format)
            print(f"Created : {created.strftime('%Y-%m-%d %H:%M:%S')}")
            updated = datetime.datetime.strptime(entry["updated_at"], tz_format)
            print(f"Updated : {updated.strftime('%Y-%m-%d %H:%M:%S')}")


            # Function for parsing chat_messages
            print_conversation(entry['chat_messages'], tz_format)
        print()

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

def print_conversation(chat_messages, tz_format):
    for message in chat_messages:
        created_at = datetime.datetime.strptime(message['created_at'], tz_format)
        created_at_str = created_at.strftime('%Y-%m-%d %H:%M:%S')
        print(f"{created_at_str} - {message['sender']}: {message['text']}")
        if message['attachments']:
            print("  Attachments:")
            for attachment in message['attachments']:
                print(f"    - {attachment}")
        if message['files']:
            print("  Files:")
            for file in message['files']:
                print(f"    - {file}")
        print()



if __name__ == "__main__":
    main()

