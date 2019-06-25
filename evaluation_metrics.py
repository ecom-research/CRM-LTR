import numpy as np
import os
import pandas as pd
from subprocess import PIPE, Popen

def _format_data_trec_eval(qids_test, y_pred_test, y_test, trec_eval_path):
    #Formats data for trec_eval script and dumps gold.txt and submission.txt files to the disk
  
    N = len(y_pred_test)
    
    df_submission = pd.DataFrame(index=np.arange(N), columns=['qid', 'iter', 'docno', 'rank', 'sim', 'run_id'])
    df_submission['qid'] = qids_test
    df_submission['iter'] = 0
    df_submission['docno'] = np.arange(N)
    df_submission['rank'] = 0
    df_submission['sim'] = y_pred_test
    df_submission['run_id'] = 'nnet'
    df_submission.sort_values(by = ['qid', 'docno'], inplace = True)
    df_submission.to_csv(os.path.join(trec_eval_path, 'submission.txt'), header=False, index=False, sep=' ')

    df_gold = pd.DataFrame(index=np.arange(N), columns=['qid', 'iter', 'docno', 'rel'])
    df_gold['qid'] = qids_test
    df_gold['iter'] = 0
    df_gold['docno'] = np.arange(N)
    df_gold['rel'] = y_test
    df_gold.sort_values(by = ['qid', 'docno'], inplace = True)
    df_gold.to_csv(os.path.join(trec_eval_path, 'gold.txt'), header=False, index=False, sep=' ')

def get_trec_eval_metrics(qids, y_pred, y_true, trec_eval_path):
    """
    Calls trec_eval script and returns ltr metrics
    Parameters
    ----------
    qids: query ids of the test data
    y_pred: array of binary predictions of the model
    y_true: array of ground truth binary predictions
    trec_eval_path: path to the trec_eval folder on the system
    """
    
    _format_data_trec_eval(qids, y_pred, y_true, trec_eval_path)
    p = Popen([os.path.join(trec_eval_path, "trec_eval"), os.path.join(trec_eval_path, "gold.txt"), os.path.join(trec_eval_path, "submission.txt")], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    
    map_score = float(output.decode("utf-8").split('\n')[5].split('\t')[-1])
    mrr = float(output.decode("utf-8").split('\n')[9].split('\t')[-1])
    p_5 = float(output.decode("utf-8").split('\n')[21].split('\t')[-1])
    p_10 = float(output.decode("utf-8").split('\n')[22].split('\t')[-1])                 
    
    p = Popen([os.path.join(trec_eval_path, "trec_eval"), "-m", "ndcg_cut", os.path.join(trec_eval_path, "gold.txt"), os.path.join(trec_eval_path, "submission.txt")], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    ndcg_5 = float(output.decode("utf-8").split('\n')[0].split('\t')[-1])
    ndcg_10 = float(output.decode("utf-8").split('\n')[1].split('\t')[-1])
    
    return map_score, mrr, p_5, p_10, ndcg_5, ndcg_10