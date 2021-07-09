from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch




def get_summary(text):
    model_name = 'google/pegasus-cnn_dailymail'
    tokenizer = PegasusTokenizer.from_pretrained(model_name)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = PegasusForConditionalGeneration.from_pretrained(model_name)
    try:
        print(f'using {device}')
        torch.cuda.empty_cache()
        model.to(device)
        torch.cuda.empty_cache()
        batch = tokenizer(text, truncation=True, padding='longest', return_tensors="pt").to(device)
        torch.cuda.empty_cache()
        translated = model.generate(**batch, min_length=150, max_length=250)
        tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
        torch.cuda.empty_cache()
        return tgt_text
    except RuntimeError:
        device = 'cpu'
        print(f'using {device}')
        model.to(device)
        batch = tokenizer(text, truncation=True, padding='longest', return_tensors="pt").to(device)
        translated = model.generate(**batch, min_length=150, max_length=250)
        tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
        return tgt_text
