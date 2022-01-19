import os
import json

# Validate json array or object
def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True


# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("data"):
    # loop on every file in folders
    for f in files:
        if f.endswith(".json"):
            # flagging if comma is there.
            with open(f'{root}/{f}', 'r') as original_file:
                # traverse to last line
                for line_number, line in enumerate(original_file):
                    pass
            last_line = line

            comma_flag = False
            if last_line.endswith(",\n"):
                comma_flag = True

            with open(f'{root}/{f}', 'r') as original_file:
                if not (original_file.readline().startswith('[')):
                    data = original_file.read()
                    if comma_flag:
                        data = data.rstrip(',\n')
                    print(f'Writing file: {root}/{f}')
                    with open(f'{root}/{f}', 'w') as modified_file:
                        modified_file.write('[\n' + data + ']')
