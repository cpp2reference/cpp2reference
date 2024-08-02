from pathlib import Path
import os.path
import json
import copy
import requests

def read_file_as_json(filename):
    with open(filename) as file:
        return json.loads(file.read())   

def get_cxx_compiler_settings(path, defaultSettings):
    custom_filename = path.with_suffix('.json')  # Replaces '.cpp2' extension with '.json'
    if not os.path.exists(custom_filename):
        return defaultSettings
    else:
        return read_file_as_json(custom_filename)

def make_include_filename(path):
    path_str = str(path)
    path_str = path_str.removeprefix('../src/')
    path_str = path_str.removeprefix('..\\src\\')
    path_str = path_str.removesuffix('.cpp2')
    path_str = path_str + '.html'
    return path_str

if __name__ == "__main__":
    # Read the clientState template file for the Compiler Explorer API
    template_json = read_file_as_json("client_state_template.html")

    # Read the default C++ compiler settings for the code examples
    #   These can be overwritten on a case-by-case basis
    default_cxx_settings_json = read_file_as_json("../src/default.json")

    processed_count = 0

    # Recursively process all .cpp2 files in the `src` directory
    #   For each file, if there is no corresponding include .html file, then
    #   generate a Compiler Explorer shortlink for that Cpp2 source code
    #   and write the shortlink url into the include .html file.
    paths = Path("../src").rglob('*.cpp2')
    for path in paths:
        # Get the corresponding filename for the include .html file
        # If it already exists then we'll skip processing this Cpp2 source
        include_filename = make_include_filename(path)

        if not os.path.exists(include_filename):
            print(path)
            with open(file=str(path), mode='r', encoding='utf8') as cpp2_file:
                # Read the Cpp2 source code
                cpp2_source = cpp2_file.read()

                # Look for custom C++ compiler settings
                cxx_settings_json = get_cxx_compiler_settings(path, default_cxx_settings_json)

                # Create a new clientState JSON object and insert the Cpp2 source
                client_state = copy.deepcopy(template_json)
                client_state["sessions"][0]["source"] = cpp2_source
                client_state["trees"][0]["files"][0]["content"] = cpp2_source

                # Insert the C++ compiler settings to use
                client_state["trees"][0]["cmakeArgs"] = cxx_settings_json["cmakeArgs"]
                client_state["trees"][0]["compilers"][0]["id"] = cxx_settings_json["compiler_id"]
                client_state["trees"][0]["executors"][0]["compiler"]["id"] = cxx_settings_json["compiler_id"]

                # Create the CE shortlink for the clientState
                res = requests.post("https://godbolt.org/api/shortener", json = client_state)
                if res.status_code != 200:
                    print("Error from Compiler Explorer shortener API: " + res)
                    exit(-1)

                # Get the CE shortlink from the result
                res_json = res.json()
                ce_url   = res_json["url"]

                # Make sure intermediate dirs exist for the destination .html file path
                dest_file_path = Path(include_filename)
                dest_file_path.parent.mkdir(exist_ok=True, parents=True)

                # Write the shortlink into the include .html file
                with open(include_filename, 'w') as inc_file:
                    content = "{% assign url = '" + ce_url + "' %}"
                    inc_file.write(content)
                    processed_count += 1
    
    print(f"Files processed: {processed_count}")