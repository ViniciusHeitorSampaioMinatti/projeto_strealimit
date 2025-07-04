import streamlit as st

st.set_page_config(page_title="projeto streamlit", layout="wide")
st.markdown("# Testando o Streamlit")

def main():
    abas = st.tabs([
        "Clientes",
        "Cadastrar cliente",
        "Editar",
        "Deletar",
    ])

    with abas[0]:
        st.title("Clientes")

    with abas[1]:
        st.title("Cadastrar clientes")

        with st.form(key='add_cliente', clear_on_submit=True):
            nome = st.text_input("nome", placeholder="Nome")
            email = st.text_input("Email", placeholder="Email")
            idade = st.number_input("Idade", placeholder="Idade", format="%d", step=1)
            telefone = st.number_input("Telefone", placeholder="Telefone", format="%d", step=1)
            profissao = st.selectbox("selecione a profissão", options=[
                "Desenvolvedor Web", "Analista de  infraestrutura" 
                "DBA Senior", "Tecnico de informatica"
            ])
            btn_cadastrar = st.form_submit_button("Cadastrar cliente")

    with abas[2]:
        st.title("Editar")

    with abas[3]:
        st.title("Deletar")

main()