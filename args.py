import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--monitor", type=str, help="optimiser monitor: val_acc(acc), val_loss(loss)", default="acc")
    parser.add_argument('--GPU', type=int, default=0, help='GPU device')
    parser.add_argument('--seed', type=int, default=0, help='random seed')

    parser.add_argument("--use_best_hyperparams", type=int, default=1, help="whether use parameters in best_hyperparameters.yml")
    parser.add_argument("--First_self_loop", type=int, choices=[1, -1,  0], default=0, help="1 is add, -1 is remove, Whether to add self-loops to the graph")

    parser.add_argument("--has_scheduler", type=int, default=1, help="Whether Optimizer has a scheduler")
    parser.add_argument('--patience', type=int, default=400, help='patience to reduce lr,80')
    parser.add_argument('--num_split', type=int, default=20, help='num of run in spite of many splits')
    parser.add_argument('--feat_dim', type=int, default=64, help='feature dimension')
    parser.add_argument('--epoch', type=int, default=10000, help='epoch1500,')
    parser.add_argument('--NotImproved', type=int, default=810, help='consecutively Not Improved, break, 500, 450, 410, 210, 60')
    parser.add_argument('--lr', type=float, default=0.005, help='learning rate')
    parser.add_argument('--l2', type=float, default=5e-4, help='l2 regularizer, 5e-4, 0 is better')


    parser.add_argument("--jk", choices=["max", "cat", 'weighted',  0], default=0)
    parser.add_argument("--inci_norm", choices=["dir", "sym", 'row', 0], default=0)

    parser.add_argument('--net', type=str, default='mlp', help='mlp, Dir-GNN, ParaGCN, SimGAT, ScaleNet, SloopNet, tSNE, RandomNet, HFNet '
                     'Mag, Sig, QuaNet, '
                    'GCN, GAT, SAGE, Cheb, APPNP, GPRGNN, pgnn, mlp, sgc,'
                    'DiGib, DiGub,DiGi3, DiGi4 (1iG, RiG replace DiG)''Sym, 1ym')
    parser.add_argument('--Dataset', type=str, default='telegram/', help='citeseer/ , cora_ml/, dgl/pubmed, telegram/,  WikiCS/, dgl/cora ,film/'
        'WikipediaNetwork/squirrel, WikipediaNetwork/chameleon, WikipediaNetwork/crocodile, WebKB/Cornell, WebKB/Texas,  WebKB/Wisconsin'
        'ogbn-arxiv/, directed-roman-empire/, arxiv-year/, snap-patents/,  malnet/tiny')
    parser.add_argument('--dropout', type=float, default=0.5, help='dropout prob')
    parser.add_argument('--layer', type=int, default=1, help='number of layers (2 or 3), default: 2')

    args = parser.parse_args()

    return args

