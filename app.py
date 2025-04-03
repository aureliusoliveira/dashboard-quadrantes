import streamlit as st

st.set_page_config(page_title="Quadrantes da Produtividade", layout="wide")

st.title("📌 Bem-vindo ao Dashboard dos Quadrantes da Produtividade Legislativa")

st.markdown("""
Este painel interativo permite explorar e comparar a atuação dos deputados federais da 57ª legislatura com base em dois critérios principais:

- **Produtividade Legislativa:** Indicador composto que avalia a relevância e os resultados das proposições apresentadas.
- **Gasto CEAP Ajustado:** Valor total das despesas com exercício parlamentar, ajustado para remover passagens aéreas comuns a todos os mandatos.

Os parlamentares são distribuídos em quadrantes conforme seu desempenho em custo e produtividade.

➡️ Use o menu lateral para acessar os quadrantes interativos.
""")
