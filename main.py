import klembord
from collections import OrderedDict
import csv
import os
import win32com.client


# test= klembord.set_with_rich_text('plain text', '<b>plain text</b>')
klembord.init()


def input_sorter():
    clipBoard = klembord.get_with_rich_text()[1]
    just_html_string = clipBoard.split("<!--StartFragment-->")[-1] + ">"  # or <body>

    # clipBoard = f'office.com/mail/inbox/id/AAQkADQyNzUyNGY2LTMyM2QtNDg1My04NTQ5LTM1NWZmYWRmYTQyMQAQAIrA5w4LmEbdm0JPdRpmTEI%3D\n<html>\n<body>\n<!--StartFragment--><br class="Apple-interchange-newline"><hr tabindex="-1" style="color: rgb(0, 0, 0); font-family: &quot;Segoe UI Web (West European)&quot;, &quot;Segoe UI&quot;, -apple-system, BlinkMacSystemFont, Roboto, &quot;Helvetica Neue&quot;, sans-serif; font-size: 12px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline-block; width: 588px;"><div id="divRplyFwdMsg" dir="ltr" style="border: 0px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-variant-numeric: inherit; font-variant-east-asian: inherit; font-variant-alternates: inherit; font-weight: 400; font-stretch: inherit; font-size: 12px; line-height: inherit; font-family: &quot;Segoe UI Web (West European)&quot;, &quot;Segoe UI&quot;, -apple-system, BlinkMacSystemFont, Roboto, &quot;Helvetica Neue&quot;, sans-serif; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: rgb(0, 0, 0); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><font face="Calibri, sans-serif" style="font-size: 11pt; color: rgb(0, 0, 0);"><b>From:</b><span> </span>Urena, Leonardo [EMR/SYSS/PWS/GUAC] &lt;leonardo.urena@emerson.com&gt;<br><b>Sent:</b><span> </span>Thursday, June 15, 2023 7:47 PM<br><b>To:</b><span> </span>Urena, Leonardo [EMR/SYSS/PWS/GUAC] &lt;leonardo.urena@emerson.com&gt;<br><b>Subject:</b><span> </span>Re: idk</font><div style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"> </div></div><div dir="ltr" style="border: 0px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-variant-numeric: inherit; font-variant-east-asian: inherit; font-variant-alternates: inherit; font-weight: 400; font-stretch: inherit; font-size: 12px; line-height: inherit; font-family: &quot;Segoe UI Web (West European)&quot;, &quot;Segoe UI&quot;, -apple-system, BlinkMacSystemFont, Roboto, &quot;Helvetica Neue&quot;, sans-serif; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: rgb(0, 0, 0); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="x_elementToProof" style="border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 11pt; line-height: inherit; font-family: Calibri, Arial, Helvetica, sans-serif; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: rgb(0, 0, 0);">this is just a TEST1</div><div id="x_appendonsend" style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"></div><hr tabindex="-1" style="display: inline-block; width: 588px;"><div id="x_divRplyFwdMsg" dir="ltr" style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><font face="Calibri, sans-serif" style="font-size: 11pt; color: rgb(0, 0, 0);"><b>From:</b><span> </span>Urena, Leonardo [EMR/SYSS/PWS/GUAC] &lt;leonardo.urena@emerson.com&gt;<br><b>Sent:</b><span> </span>Thursday, June 15, 2023 7:46 PM<br><b>To:</b><span> </span>Urena, Leonardo [EMR/SYSS/PWS/GUAC] &lt;leonardo.urena@emerson.com&gt;<br><b>Subject:</b><span> </span>idk</font><div style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"> </div></div><div dir="ltr" style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><div class="x_x_WordSection1" style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><p class="x_x_MsoNormal x_x_elementToProof" style="margin: 0in; font-size: 11pt; font-family: Calibri, sans-serif;">test0</p><p class="x_x_MsoNormal" style="margin: 0in; font-size: 11pt; font-family: Calibri, sans-serif;"><span style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><span style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><b><span style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: rgb(31, 73, 125);"> </span></b></span></span></p><p class="x_x_MsoNormal" style="margin: 0in; font-size: 11pt; font-family: Calibri, sans-serif;"><span style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><span style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><b><span style="border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 8pt; line-height: inherit; font-family: Arial, sans-serif; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: rgb(31, 73, 125);">Leonardo Urena Nikolova</span></b></span></span><span style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><span style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><span style="border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 8pt; line-height: inherit; font-family: Arial, sans-serif; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: rgb(31, 73, 125);"><span> </span>| Cybersecurity Engineer | Power &amp; Water Solutions<br><b>Emerson Automation Solutions</b></span></span></span><span style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"><b><span style="border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 8pt; line-height: inherit; font-family: Arial, sans-serif; font-optical-sizing: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: rgb(31, 73, 125);"></span></b></span></p><span style="border: 0px; font: inherit; margin: 0px; padding: 0px; vertical-align: baseline; color: inherit;"></span><p class="x_x_MsoNormal" style="margin: 0in; font-size: 11pt; font-family: Calibri, sans-serif;"> </p></div></div></div'
    # just_html_string = clipBoard.split('<!--StartFragment-->')[-1]+'>' #or <body>
    #
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


def string_similarity(s1, strings_list, threshold=90):
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


# Test


def compare_command(input_user):
    # CSV shortcuts list
    csv_file_path = "./Data/shortcuts.csv"
    with open(csv_file_path, newline="") as csvfile:
        shortcutListRaw = list(csv.reader(csvfile))
        shortcutList = [item[0] for item in shortcutListRaw]
    print(f"The following shortcuts are present of the CSV file: {shortcutList}")

    match_shortcut_conditional_csv, match_shortcut_csv = string_similarity(
        input_user, shortcutList, 80
    )

    # initial
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

    match_shortcut_conditional_docx = False

    for docx in docx_files:
        if (docx in match_shortcut_csv) and (
            match_shortcut_conditional_csv
        ):  # falta validar este input tambien
            print(docx)
            match_shortcut_docx = docx
            match_shortcut_conditional_docx = True
            print(
                f"There is a match! The {match_shortcut_docx}.docx file has been detected on the data folder"
            )
            break

    if match_shortcut_conditional_csv and match_shortcut_conditional_docx:
        # Replace 'your_document.docx' with the path to your .docx file
        docx_path = os.path.abspath(f"./Data/{match_shortcut_docx}.docx")
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
        # word.Quit()
        print("Content copied to clipboard using pywin32.")


if __name__ == "__main__":
    # Input shortcut
    stringClipboardShortcut = klembord.get_with_rich_text()[0]
    stringClipboardShortcutSplit = stringClipboardShortcut.split(" ")
    # print(stringClipboardShortcutSplit)
    Shortcut = "".join(stringClipboardShortcutSplit)
    ShortcutSize = len(Shortcut)
    input_user = Shortcut.split("\x00")[0]
    print(input_user)
    if ShortcutSize < 15:
        compare_command(input_user)
    else:
        input_sorter()


# sru shortcut
# sdfds
# initial
