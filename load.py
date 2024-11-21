from transformers import T5ForConditionalGeneration, T5Tokenizer


model = T5ForConditionalGeneration.from_pretrained('NlpHUST/t5-small-vi-summarization')
tokenizer = T5Tokenizer.from_pretrained('NlpHUST/t5-small-vi-summarization')

save_directory = "./model"


model.save_pretrained(save_directory)
tokenizer.save_pretrained(save_directory)