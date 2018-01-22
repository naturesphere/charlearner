from yaml_to_txt import yaml2txt

y2t = yaml2txt()
# y2t.yamlfile2txtfile('22.srt.yml')
#
# y2t.yamls2txts(".")
src_dir = "D:/_Work\python/test/charlearner/src/Data/Corpus/Augment0/MS_OK/20171227/OpenSubtitles2016.fr-ms.ms_1.yml"
print("123456")
y2t.yamls2txts(src_dir)