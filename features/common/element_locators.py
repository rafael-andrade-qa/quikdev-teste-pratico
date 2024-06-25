SELECTORS = {
    "form": {
        "name_input": "//input[@id='inputNome']",
        "price_input": "//input[@id='inputPreco']",
        "expiry_date_input": "//input[@id='inputValidade']",
        "add_button": "//button[normalize-space()='Adicionar']",
    },
    "table": {
        "row": "//tbody[@id='conteudoTabela']/tr",
    },
    "error_message": {
        "name_invalid_feedback_label": "//div[normalize-space()='Nome invalido']",
        "price_invalid_feedback_label": "//div[normalize-space()='Preço invalido']",
        "expiry_date_invalid_feedback_label": "//div[normalize-space()='Validade Invalida']",
    },
}
