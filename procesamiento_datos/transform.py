from data_transformers.trasformer_for_format import trasformer
from data_transformers.mariana_transformer import mariana_trasformer
from data_transformers.serviverde_transformer import serviverde_trasformer

trans = trasformer()

mariana_trans = mariana_trasformer()
trans.tranformer_templete('mariana_merge.csv', 'procesado_mariana.csv', mariana_trans)

serviverde_trans = serviverde_trasformer()
trans.tranformer_templete('serviverde_merge.csv', 'procesado_serviverde.csv', serviverde_trans)