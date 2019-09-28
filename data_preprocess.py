#%%
import jieba

#%%
src_output = open('question.txt','w',encoding='utf8')
tgt_output = open('target.txt','w',encoding='utf8')
def process(rawfile,src,tgt,init = False):
    with open(rawfile,encoding='utf8') as f:
        cnt = 0
        for line in f.readlines():
            item = line.strip().split('\t')
            if len(item) == 2:
                question = item[0]
                answer = item[1]
                question_seg = " ".join(jieba.cut(question.replace(" ","")))
                answer_seg = " ".join(jieba.cut(answer.replace(" ","")))
                if cnt == 0 and init == True:
                    src.write(question_seg)
                    tgt.write(answer_seg)
                src.write('\n'+question_seg)
                tgt.write('\n'+answer_seg)
process("./clean_chat_corpus/qingyun.tsv",src_output,tgt_output,init=True)
process("./clean_chat_corpus/douban_single_turn.tsv",src_output,tgt_output)
process("./clean_chat_corpus/xiaohuangji.tsv",src_output,tgt_output)
#%%
