import unittest

from transformers import LlamaTokenizerFast

from tests._tokenizer_common import TokenizerTesterMixin

import logging

logging.basicConfig(level=logging.DEBUG)


class GPT2TokenizerTest(TokenizerTesterMixin, unittest.TestCase):

    tokenizer_class = LlamaTokenizerFast
    pretrained_name = "saibo/llama-1B"

    def setUp(self):
        super().setUp()