from yaml_to_txt import yaml2txt

y2t = yaml2txt()
# y2t.yamlfile2txtfile('22.srt.yml')
#
# y2t.yamls2txts(".")
# src_dir = "D:\\_Work\\python\\corpus\\FR_OK\\20171227"
src_dir = "D:\\_Work\\python\\corpus\\FR_OK\\20180102"
y2t.yamls2txts(src_dir)
