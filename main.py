import klembord
from collections import OrderedDict
from csv import reader, writer
from  os import listdir, path
from win32com.client import Dispatch

klembord.init()


def input_sorter():
    clipBoard = klembord.get_with_rich_text()[1]
    just_html_string = clipBoard.split("<!--StartFragment-->")[-1] + ">"  # or <body>

    # clipBoard = f'office.com/mail/inbox/id/AAQkADQyNzUyNGY2LTMyM2QtNDg1My04NTQ5LTM1NWZmYWRmYTQyMQAQAIrA5w4LmEbdm0JPdRpmTEI%3D\n<html>\n<body>\n<!--StartFragment--><br class="Apple-interchange-newline"><hr tabindex="-1" style="color: rgb(0, 0, 0); font-family: &quot;Segoe UI Web (West European)&quot;, &quot;Segoe UI&quot;, -apple-system, BlinkMacSystemFont, Roboto, &quot;Helvetica Neue&quot;, sans-serif; font-size: 12px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline-block; width: 588px;"><div id="divRplyFwdMsg" dir="ltr" style="border: 0px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-variant-numeric: inherit; font-variant-east-asian: inherit; font-variant-alternates: inherit; font-weight: 400; font-stretch: inherit; font-size: 12px; line-height: inherit; font-family: &quot;Segoe UI Web (West European)&quot;, &quot;Segoe UI&quot;, -apple-system, BlinkMacSystemFont, Roboto, &quot;Helvetica Neue&quot;, sans-serif; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: rgb(0, 0, 0); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><font face="Calibri, sans-serif" style="font-size: 11pt; color: rgb(0, 0, 0);"><b>From:</b><span> </span>Urena, Leonardo [EMR/SYSS/PWS/GUAC] &lt;leonardo.urena@emerson.com&gt;<br><b>Sent:</b><span> </span>Thursday, June 15, 2023 7:47 PM<br><b>To:</b><span> </span>Urena, Leonardo [EMR/SYSS/PWS/GUAC] &lt;leonardo.urena@emerson.com&gt;<br><b>Subject:</b><span> </span>Re: idk</font><div style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"> </div></div><div dir="ltr" style="border: 0px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-variant-numeric: inherit; font-variant-east-asian: inherit; font-variant-alternates: inherit; font-weight: 400; font-stretch: inherit; font-size: 12px; line-height: inherit; font-family: &quot;Segoe UI Web (West European)&quot;, &quot;Segoe UI&quot;, -apple-system, BlinkMacSystemFont, Roboto, &quot;Helvetica Neue&quot;, sans-serif; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: rgb(0, 0, 0); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="x_elementToProof" style="border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 11pt; line-height: inherit; font-family: Calibri, Arial, Helvetica, sans-serif; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: rgb(0, 0, 0);">this is just a TEST1</div><div id="x_appendonsend" style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"></div><hr tabindex="-1" style="display: inline-block; width: 588px;"><div id="x_divRplyFwdMsg" dir="ltr" style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><font face="Calibri, sans-serif" style="font-size: 11pt; color: rgb(0, 0, 0);"><b>From:</b><span> </span>Urena, Leonardo [EMR/SYSS/PWS/GUAC] &lt;leonardo.urena@emerson.com&gt;<br><b>Sent:</b><span> </span>Thursday, June 15, 2023 7:46 PM<br><b>To:</b><span> </span>Urena, Leonardo [EMR/SYSS/PWS/GUAC] &lt;leonardo.urena@emerson.com&gt;<br><b>Subject:</b><span> </span>idk</font><div style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"> </div></div><div dir="ltr" style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><div class="x_x_WordSection1" style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><p class="x_x_MsoNormal x_x_elementToProof" style="margin: 0in; font-size: 11pt; font-family: Calibri, sans-serif;">test0</p><p class="x_x_MsoNormal" style="margin: 0in; font-size: 11pt; font-family: Calibri, sans-serif;"><span style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><span style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><b><span style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: rgb(31, 73, 125);"> </span></b></span></span></p><p class="x_x_MsoNormal" style="margin: 0in; font-size: 11pt; font-family: Calibri, sans-serif;"><span style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><span style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><b><span style="border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 8pt; line-height: inherit; font-family: Arial, sans-serif; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: rgb(31, 73, 125);">Leonardo Urena Nikolova</span></b></span></span><span style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><span style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><span style="border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 8pt; line-height: inherit; font-family: Arial, sans-serif; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: rgb(31, 73, 125);"><span> </span>| Cybersecurity Engineer | Power &amp; Water Solutions<br><b>Emerson Automation Solutions</b></span></span></span><span style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><b><span style="border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 8pt; line-height: inherit; font-family: Arial, sans-serif; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: rgb(31, 73, 125);"></span></b></span></p><span style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"></span><p class="x_x_MsoNormal" style="margin: 0in; font-size: 11pt; font-family: Calibri, sans-serif;"> </p></div></div></div'
    # just_html_string = clipBoard.split('<!--StartFragment-->')[-1]+'>' #or <body>

    # print(just_html_string)
    parts = just_html_string.split("From:")
    parts_inversed = list(reversed(parts))

    new_list = []

    # """
    for x in parts_inversed:
        # print(x[0:2])
        if x[0:2] == "</":
            x = x[4:]
            # print (x, "\n \n \n")
        if "</" not in x[-6:]:
            x = x[:-7] + x[-6:].replace("<", "</")

        # print(x, "\n \n \n")
        new_list.append(x)
    # """

    # print(new_list)
    parts_inversed = list(
        map(
            lambda x: "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━<br> From:" + x,
            new_list[:-1],
        )
    ) + list(new_list[-1])

    inverse_string = "".join(parts_inversed)

    print(inverse_string)

    # """
    content = OrderedDict()
    content["HTML Format"] = klembord.wrap_html(inverse_string)
    test1 = klembord.set(content)
    # """

def levenshtein_distance(s1, s2):
    """
    Compute the Levenshtein distance between two strings.
    """
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2 + 1]
        for i1, c1 in enumerate(s1):
            if c1.lower() == c2.lower():
                distances_.append(distances[i1])
            else:
                distances_.append(
                    1 + min((distances[i1], distances[i1 + 1], distances_[-1]))
                )
        distances = distances_
    return distances[-1]

def string_similarity(s1, strings_list, threshold=100):
    """
    Compute the similarity between s1 and each string in strings_list.
    Return True/False based on similarity criteria and the string with the highest similarity.
    """
    max_similarity = 0
    most_similar_string = None

    for s in strings_list:
        # Calculate the Levenshtein distance
        distance = levenshtein_distance(s1, s)
        # Calculate similarity percentage
        similarity = (1 - distance / max(len(s1), len(s))) * 100
        # Update max_similarity and most_similar_string
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_string = s

    return max_similarity >= threshold, most_similar_string

def compare_command(input_user):
    csv_file_path = "./Data/shortcuts.csv"
    with open(csv_file_path, newline="") as csvfile:
        shortcutListRaw = list(reader(csvfile))
        shortcutList = [item[0] for item in shortcutListRaw]
    match_shortcut_csv = []
    match_shortcut_conditional_csv = False
    for item in shortcutList: 
        if item in input_user and len(item) == len(input_user):
            match_shortcut_csv.append(item)
            match_shortcut_conditional_csv = True
            
    folder_path = "./Data/"
    docx_files = []
    files = listdir(folder_path)
    for file in files:
        if file.endswith(".docx"):
            docx_files_ext = path.splitext(file)[0]
            docx_files.append(docx_files_ext)

    match_shortcut_docx = []
    match_shortcut_conditional_docx = False
    for i in docx_files:
        if (i in input_user and len(i) == len(input_user)):
            print(i)
            match_shortcut_docx.append(i)
            match_shortcut_conditional_docx = True

    if  match_shortcut_conditional_csv and match_shortcut_conditional_docx:
        docx_path = path.abspath(f"./Data/{input_user}.docx")
        word = Dispatch("Word.Application")
        doc = word.Documents.Open(docx_path)
        doc.Content.WholeStory
        doc.Content.Copy()
        doc.Close(False)
    else:
        for looking_for_error_file in docx_files:
            if looking_for_error_file == "noShortcutFound":
                docx_path = path.abspath(f"./Data/noShortcutFound.docx")
                word = Dispatch("Word.Application")
                doc = word.Documents.Open(docx_path)
                doc.Content.Text = "No shortcut was found on the shortcuts.csv file or on the Data folder(.docx). List of available shortcuts on .csv file:  \n"
                # Read and insert data from the CSV file into the document line by line
                with open(csv_file_path, newline='') as csvfile:
                    csv_reader = reader(csvfile)
                    for row in csv_reader:
                        line_text = ', '.join(row) # Convert the CSV row to a string
                        doc.Content.InsertAfter(line_text + '\n') # Insert the line and add a newline
                doc.Save()
                doc.Content.WholeStory
                doc.Content.Copy()
                doc.Close(False)
                print("Content copied to clipboard using pywin32.")

if __name__ == "__main__":
    stringClipboardShortcut = klembord.get_with_rich_text()[0]
    stringClipboardShortcutSplit = stringClipboardShortcut.split(" ")
    Shortcut = "".join(stringClipboardShortcutSplit)
    ShortcutSize = len(Shortcut)
    input_user = Shortcut.split("\x00")[0]
    if ShortcutSize < 15:
        compare_command(input_user)  
    else:
        input_sorter()