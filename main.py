import klembord
from collections import OrderedDict

# test= klembord.set_with_rich_text('plain text', '<b>plain text</b>')
klembord.init()

# This is a comment

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


def compare_command():
    pass


if __name__ == "__main__":
    input_sorter()
