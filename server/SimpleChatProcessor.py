import os
from datapreprocess import preprocess
import train_eval
from config import Config


class SimpleChatProcessor(object):
    def __init__(self):
        opt = Config()
        searcher, sos, eos, unknown, word2ix, ix2word = train_eval.test(opt)
        self.searcher = searcher
        self.sos = sos
        self.eos = eos
        self.unknown = unknown
        self.word2ix = word2ix
        self.ix2word = ix2word
        self.opt = opt
        if not os.path.isfile(opt.corpus_data_path):
            preprocess()

    def process(self, input):
        output_words = train_eval.output_answer(input, self.searcher, self.sos, self.eos, self.unknown, self.opt,
                                                self.word2ix, self.ix2word)
        return output_words
