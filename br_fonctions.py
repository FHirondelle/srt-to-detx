HEADER = "header.txt"

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

    h_debut = int(time[:2])
    ms_debut = int(time[9:12])

    h_fin = int(time[-12:-10])
    ms_fin = int(time[26:])

    h_debut += 1
    h_fin += 1
    im_debut = ms_debut // 40
    im_fin = ms_fin // 40

    time_debut_detx = "0" + str(h_debut) + time[2:8] + ":" + str(im_debut)
    time_fin_detx = "0" + str(h_fin) + time[-10:-4] + ":" + str(im_fin)

    return time_debut_detx, time_fin_detx

def format_line(time_d, time_f, line):
    return f"""\t\t<line role="default" track="0">\n\t\t\t<lipsync timecode="{time_d}" type="in_open"/>\n\t\t\t<text>{line}</text>\n\t\t\t<lipsync timecode="{time_f}" type="out_open"/>\n\t\t</line>\n"""
