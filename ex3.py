import json

# Exemplo de JSON com faturamento mensal
faturamento_json = '''
{
    "faturamento_diario": [200, 0, 150, 300, 0, 0, 100, 50, 400, 0, 0, 250, 100, 0, 200]
}
'''

dados = json.loads(faturamento_json)
faturamento = [valor for valor in dados["faturamento_diario"] if valor > 0]  # Ignorar dias sem faturamento

menor = min(faturamento)
maior = max(faturamento)
media = sum(faturamento) / len(faturamento)
dias_acima_media = sum(1 for valor in faturamento if valor > media)

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
