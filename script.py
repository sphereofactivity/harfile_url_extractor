import json
from urllib.parse import urlparse


def process_har_file(filepath):
    try:
        # r for read mode and in encoding utf-8 to prevent special characters from affecting how the path to file is read.
        with open(filepath, 'r', encoding='utf-8') as file:
            har_data = json.load(file)

        # unique base urls (https//example.com) will be stored in this set ++ set is used because the order of displayed urls doesn't matter for this purpose.
        unique_base_url = set()

        # checking to see if the base url appears in the set, if it is not in the set then add it to the set.
        for entry in har_data['log']['entries']:
            if 'url' in entry['request']:
                full_url = entry['request']['url']
                parsed_url = urlparse(full_url)

                # netloc to determine the base url (https://example.com/page) - the /page will be cut off and only the network location (https://example.com) will be displayed.
                base_url = parsed_url.scheme + "://" + parsed_url.netloc

                if base_url not in unique_base_url:
                    print(f"Base= URL: {base_url}")
                    unique_base_url.add(base_url)

    except Exception as e:
        print(f"Exception occured: {e}")


def main():
    print(r"""      ___           ___                                  ___           ___                          ___           ___           ___                         ___           ___     
     /\  \         /\  \                                /\__\         /|  |                        /\  \         /\  \         /\__\                       /\  \         /\  \    
     \:\  \       /::\  \                              /:/ _/_       |:|  |           ___         /::\  \       /::\  \       /:/  /          ___         /::\  \       /::\  \   
      \:\  \     /:/\:\__\                            /:/ /\__\      |:|  |          /\__\       /:/\:\__\     /:/\:\  \     /:/  /          /\__\       /:/\:\  \     /:/\:\__\  
  ___  \:\  \   /:/ /:/  /    ___     ___            /:/ /:/ _/_   __|:|__|         /:/  /      /:/ /:/  /    /:/ /::\  \   /:/  /  ___     /:/  /      /:/  \:\  \   /:/ /:/  /  
 /\  \  \:\__\ /:/_/:/__/___ /\  \   /\__\          /:/_/:/ /\__\ /::::\__\_____   /:/__/      /:/_/:/__/___ /:/_/:/\:\__\ /:/__/  /\__\   /:/__/      /:/__/ \:\__\ /:/_/:/__/___
 \:\  \ /:/  / \:\/:::::/  / \:\  \ /:/  /          \:\/:/ /:/  / ~~~~\::::/___/  /::\  \      \:\/:::::/  / \:\/:/  \/__/ \:\  \ /:/  /  /::\  \      \:\  \ /:/  / \:\/:::::/  /
  \:\  /:/  /   \::/~~/~~~~   \:\  /:/  /            \::/_/:/  /      |:|~~|     /:/\:\  \      \::/~~/~~~~   \::/__/       \:\  /:/  /  /:/\:\  \      \:\  /:/  /   \::/~~/~~~~ 
   \:\/:/  /     \:\~~\        \:\/:/  /              \:\/:/  /       |:|  |     \/__\:\  \      \:\~~\        \:\  \        \:\/:/  /   \/__\:\  \      \:\/:/  /     \:\~~\     
    \::/  /       \:\__\        \::/  /                \::/  /        |:|__|          \:\__\      \:\__\        \:\__\        \::/  /         \:\__\      \::/  /       \:\__\    
     \/__/         \/__/         \/__/                  \/__/         |/__/            \/__/       \/__/         \/__/         \/__/           \/__/       \/__/         \/__/""")    
    print("\n \n")
    file_path = input("Add your file path here: ")
    process_har_file(file_path)


if __name__ == "__main__":
    main()
