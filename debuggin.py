import klembord
from collections import OrderedDict
#test= klembord.set_with_rich_text('plain text', '<b>plain text</b>')
klembord.init()




clipBoard = klembord.get_with_rich_text()
print(clipBoard)
