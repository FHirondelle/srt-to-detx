HEADER = "srt-to-detx/fichiers/header.txt"

def traitement(srtfile):
    
    srt = open(srtfile)

    srt_parse = parse(srt)

    with open(HEADER) as head:
        br_text = head.read()

    for time, line in srt_parse:
        time_deb, time_fin = timecode_convert(time)
        br_text += format_line(time_deb, time_fin, line)

    br_text += """\t</body>\n\n</detx>"""
    print(br_text)

    srt.close()

    return br_text



def parse(srt):

    subs = []
    controle = 0
    sub_number = -1
    text = ""

    for line in srt:
        if controle == 0:
            sub_number = int(line)
            controle = 1
        elif controle == 1:
            time = line[:-2]
            controle = 2
        else:
            try:
                if int(line) == sub_number + 1:
                    text = text.replace("\n", " ")
                    text = text.strip()
                    subs.append((time, text))
                    text = ""
                    sub_number += 1
                    controle = 1
                else:
                    text += line
                    text += " "
            except ValueError:
                text += line
                text += " "
    return subs


def timecode_convert(time):

    convert_im = [str(i) if i >= 10 else "0"+str(i) for i in range(25)]

    h_debut = int(time[:2])
    ms_debut = int(time[9:12])

    h_fin = int(time[17:19])
    ms_fin = int(time[26:])

    h_debut += 1
    h_fin += 1
    im_debut = ms_debut // 40
    im_fin = ms_fin // 40

    time_debut_detx = "0" + str(h_debut) + time[2:8] + ":" + convert_im[im_debut]
    time_fin_detx = "0" + str(h_fin) + time[19:25] + ":" + convert_im[im_fin]

    return time_debut_detx, time_fin_detx

def format_line(time_d, time_f, line):
    return f"""\t\t<line role="default" track="0">\n\t\t\t<lipsync timecode="{time_d}" type="in_open"/>\n\t\t\t<text>{line}</text>\n\t\t\t<lipsync timecode="{time_f}" type="out_open"/>\n\t\t</line>\n"""
