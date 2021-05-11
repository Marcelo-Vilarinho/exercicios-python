codigo_produto, qtd_produto, vlr_produto = input().split()
codigo_segundo_produto, qtd_segundo_produto, vlr_segundo_produto = input().split()

codigo_produto = int(codigo_produto)
qtd_produto = float(qtd_produto)
vlr_produto = float(vlr_produto)

codigo_segundo_produto = int(codigo_segundo_produto)
qtd_segundo_produto = float(qtd_segundo_produto)
vlr_segundo_produto = float(vlr_segundo_produto)

vlr_pagar = ((qtd_produto * vlr_produto)) + ((qtd_segundo_produto * vlr_segundo_produto))

print('VALOR A PAGAR: R$ {:.2f}'.format(vlr_pagar))