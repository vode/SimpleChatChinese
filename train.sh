onmt-build-vocab --size 50000 --save_vocab src-vocab.txt question.txt
onmt-build-vocab --size 50000 --save_vocab tgt-vocab.txt target.txt
onmt-main train --model_type NMTSmall --auto_config --config train.yml