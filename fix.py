import os

old_text = "web_user"
new_text = "root"

text_extensions = ('.js', '.html', '.css', '.cfg', '.json', '.txt')

total_replacements = 0

for filename in os.listdir('.'):
    if os.path.isdir(filename):
        continue
    if not filename.lower().endswith(text_extensions):
        continue  # skip .wasm, .zip, images, etc — binary files

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            file_data = file.read()

        if old_text in file_data:
            new_data = file_data.replace(old_text, new_text)
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(new_data)
            count = file_data.count(old_text)
            total_replacements += count
            print(f"Fixed {count} items in: {filename}")

    except (UnicodeDecodeError, PermissionError):
        pass

print(f"\nDone! Replaced {total_replacements} total items.")