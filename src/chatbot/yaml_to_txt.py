import tensorflow as tf
import yaml
import os
import glob

class yaml2txt:

    def yamlfile2txtfile(self, src_file, tar_file=None):
        # create file name
        if not src_file.endswith('.yml'):
            # print("wrong file type")
            raise Exception("wrong file type")
        if tar_file == None:
            tar_file = src_file[0:-4] + ".txt"
            print(tar_file)

        # convert
        with open(src_file, encoding='utf-8') as f:
            temp = yaml.load(f.read())
            # print(temp)
            a = temp['conversations']
        
        with open(tar_file, "w", encoding='utf-8') as f:
            for t in a:
                L = len(t)
                f.write("===\n")
                for i in range(L-1):
                    f.write("Q: " + str(t[i]) + '\n')
                    f.write("A: " + str(t[i+1]) + '\n')

    def yamls2txts(self, src_dir):
        re = src_dir + os.sep + "*.yml"
        # print(re)
        files = glob.glob(re)
        for file in files:
            print(file)
            self.yamlfile2txtfile(file)
