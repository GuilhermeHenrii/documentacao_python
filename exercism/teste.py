def exchangeable_value(budget, exchange_rate, spread, denomination):
    porcentagem = (spread * exchange_rate) / 100
    print(porcentagem)
    taxa_total = exchange_rate + porcentagem
    print(taxa_total)
    cambio = budget + ((budget * taxa_total) / 100)
    print(cambio)
    valor_apos_cambio = int(cambio // denomination)
    print(valor_apos_cambio)

exchangeable_value(127.25, 1.20, 10, 20)


