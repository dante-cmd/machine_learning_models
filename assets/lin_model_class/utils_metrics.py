from sklearn import metrics

def assessment(y, X, model):
    accu = metrics.accuracy_score(y, model.predict(X))
    print(f'The accuracy {accu:.4f}')

    predicted_prob1 = model.predict_proba(X)[:, 1]
    auc = metrics.roc_auc_score(y, predicted_prob1)
    print(f"AUC value is {auc:.4f}")
    print()

def confusion_matrix(y, X, model):
    print('Confusion Matrix')
    cf = metrics.confusion_matrix(y, model.predict(X))
    print(">",cf)
    print('> Columns: predict [0, 1]')
    print('> Rows: outcomes [0, 1]')
    print()

def prob_cond_pred(y,X, model):
    cf = metrics.confusion_matrix(y, model.predict(X))
    cfp = cf/cf.sum(axis=0, keepdims=True)
    prob = cfp.flatten()
    ind = ["P(not committed a crime|low risk)", "P(not committed a crime|high risk)","P(committed a crime|low risk)","P(committed a crime|high risk)"]
    print('Probability Conditioned on Predicts', end = '\n')

    for a, b in zip(ind,prob):
        print(">",a.ljust(35), f'{b:.2%}')
    print()

def prob_cond_out(y,X, model):
    cf = metrics.confusion_matrix(y, model.predict(X))
    cfp = cf/cf.sum(axis=1, keepdims=True)
    prob = cfp.flatten()
    ind = ["P(low risk|not committed a crime)", "P(high risk|not committed a crime)","P(low risk|committed a crime)","P(high risk|committed a crime)"]
    print('Probability Conditioned on Outcomes', end = '\n')

    for a, b in zip(ind,prob):
        print(">",a.ljust(35), f'{b:.2%}')
    print()
    
def print_metrics(y,X, model):
    assessment(y,X, model)
    prob_cond_pred(y,X, model)
    prob_cond_out(y,X, model)
    confusion_matrix(y,X, model)