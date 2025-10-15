from br_fonctions import *

srtfile = "test.srt"
detxfile = "test.detx"

srt = open(srtfile)
detx = open(detxfile, 'w')

srt_parse = parse(srt)

with open(HEADER) as head:
    br_text = head.read()

for time, line in srt_parse:
    time_deb, time_fin = timecode_convert(time)
    br_text += format_line(time_deb, time_fin, line)

br_text += """\t</body>\n\n</detx>"""

detx.write(br_text)

srt.close()
detx.close()
