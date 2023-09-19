def compare_command():
    # CSV shortcuts list
    csv_file_path = "shortcuts.csv"
    with open(csv_file_path, newline="") as csvfile:
        shortcutListRaw = list(csv.reader(csvfile))
        shortcutList = [item[0] for item in shortcutListRaw]
    print("The following shortcuts are present of the CSV file: ")
    print(shortcutList)
    match_shortcut_csv = []
    match_shortcut_conditional_csv = False
    for item in shortcutList:
        if item in ShortcutFinal:
            match_shortcut_csv.append(item)
            match_shortcut_conditional_csv = True
            print(
                "There is a match! The "
                + match_shortcut_csv[0]
                + " shortcut has been detected on the CSV file"
            )

    # .docx files name list
    folder_path = "./Data/"
    docx_files = []
    files = os.listdir(folder_path)
    for file in files:
        if file.endswith(".docx"):
            docx_files_ext = os.path.splitext(file)[0]
            docx_files.append(docx_files_ext)
    print("The following .docx files are present on the data folder: ")
    print(docx_files)

    match_shortcut_docx = []
    match_shortcut_conditional_docx = False
    for i in docx_files:
        if i in ShortcutFinal:
            print(i)
            match_shortcut_docx.append(i)
            match_shortcut_conditional_docx = True
            print(
                "There is a match! The "
                + match_shortcut_docx[0]
                + " shortcut has been detected on the data folder"
            )

    if match_shortcut_conditional_csv and match_shortcut_conditional_docx:
        # Replace 'your_document.docx' with the path to your .docx file
        docx_path = os.path.abspath(f"./Data/{ShortcutFinal}.docx")
        # Initialize a COM object for Microsoft Word
        word = win32com.client.Dispatch("Word.Application")
        # Open the .docx file
        doc = word.Documents.Open(docx_path)
        # Select the entire document
        doc.Content.WholeStory
        # Copy the selected content to the clipboard
        doc.Content.Copy()
        # Close the document without saving changes
        doc.Close(False)
        # Quit Microsoft Word
        word.Quit()
        print("Content copied to clipboard using pywin32.")