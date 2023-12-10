import torch
from rouge import Rouge
import torch
from torchtext.data.metrics import bleu_score


#ROUGE score 
def rouge_score(hypothesis, reference):
    rouge = Rouge()
    scores = rouge.get_scores(hypothesis, reference)
    return scores




class SummarizationMetrics:
    def __init__(self):
        self.rouge = Rouge()
    
    def __call__(self, hypothesis, reference):
        rouge_score = self.rouge.get_scores(hypothesis, reference)
       
        return {'rouge': rouge_score}
