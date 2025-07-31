
import streamlit as st
import pandas as pd

# Dados simulados
dados = {
    "Produto": [
        "Arroz agulhinha tipo 1 - 5kg", "Feijão preto - 1kg", "Açúcar refinado - 1kg",
        "Café em pó - 500g", "Leite integral - 1L", "Óleo de soja - 900ml",
        "Carne bovina de 1ª - kg", "Tomate - kg"
    ],
    "Preço": [21.90, 6.79, 3.99, 8.49, 4.29, 5.89, 34.90, 6.49],
    "Mercado": [
        "Guanabara", "Prezunic", "Economia", "Carrefour",
        "Supermarket", "Mundial", "Guanabara", "Atacadão"
    ],
    "Validade": [
        "01/08/2025", "02/08/2025", "03/08/2025", "01/08/2025",
        "03/08/2025", "31/07/2025", "02/08/2025", "01/08/2025"
    ],
    "Link do Encarte": [
        "https://encarte.guanabara.com.br",
        "https://encarte.prezunic.com.br",
        "https://encarte.economia.com.br",
        "https://encarte.carrefour.com.br",
        "https://encarte.supermarket.com.br",
        "https://encarte.mundial.com.br",
        "https://encarte.guanabara.com.br",
        "https://encarte.atacadao.com.br"
    ]
}

df = pd.DataFrame(dados)

st.title("Radar de Ofertas - Cesta Básica")

busca = st.text_input("🔍 Pesquise um produto da cesta básica:")

if busca:
    resultado = df[df["Produto"].str.contains(busca, case=False)]
    if resultado.empty:
        st.warning("Nenhum produto encontrado.")
    else:
        for index, row in resultado.iterrows():
            st.subheader(row["Produto"])
            st.write(f"💲 **Preço:** R$ {row['Preço']}")
            st.write(f"🏪 **Mercado:** {row['Mercado']}")
            st.write(f"📅 **Validade da Oferta:** {row['Validade']}")
            st.markdown(f"[🔗 Ver Encarte]({row['Link do Encarte']})")
else:
    st.write("Digite o nome de um produto para ver os preços nos mercados da sua região.")
