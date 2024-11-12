# ImageComparator®

Bem-vindo ao **ImageComparator®**, uma ferramenta inovadora de comparação de imagens projetada para facilitar o processo de captura, análise e comparação visual de capturas de tela. Criado com precisão e eficiência em mente, essa ferramenta usa técnicas avançadas de visão computacional para processamento de imagens, permitindo que os usuários destaquem facilmente as diferenças entre duas imagens.
### Ideal para todos os perfis de usuário o <b>ImageComparator®</b> é o seu aplicativo essencial para comparar diferenças sutis entre imagens com alta precisão e confiabilidade!

## 🎉 Recursos

* **Captura e Salva Capturas de Tela**: Capture e salve instantaneamente duas capturas de tela para comparação com um clique de botão.
* **Sensibilidade Ajustável**: Ajuste a sensibilidade para controlar o quão sutis ou pronunciadas as mudanças detectadas devem ser.
* **Destaque de Diferença de Imagem**: Gera automaticamente uma nova imagem com as diferenças detectadas.
* **Interface Amigável**: Projetada com um layout claro e direto, tornando-a acessível a usuários de todos os níveis.
* **Salvar e Acessar Registros**: Um registro interno registra cada processo de captura e comparação, fornecendo um histórico de operações.
* **Acesso Rápido às Imagens Salvas**: Abra as imagens capturadas e a saída da diferença diretamente do aplicativo.
* **Navegação Fácil no GitHub**: Acesse o perfil do desenvolvedor no GitHub diretamente do rodapé do aplicativo.

## 📦 Começando

### Pré-requisitos

1. **Python 3.x**: Certifique-se de ter o Python 3.6 ou superior instalado.
2. **Bibliotecas**: Instale as bibliotecas Python necessárias com o seguinte comando:
```python	
pip install opencv-python pyautogui
```
3. **Ícone**: Coloque seu ícone personalizado (nomeado `image-comparator-02.ico`) no diretório do projeto.

### Executando o Aplicativo

1. Clone o repositório:
```bash
git clone https://github.com/eliezermoraesss/image-comparator
cd image-comparator
```
2. Execute o aplicativo:
```python
python image_comparator.py
```
## 🚀 Uso

1. **Inicie** o aplicativo executando o script.
2. **Capture Imagens**:
   * Clique em **"Capturar Imagem 1"** e **"Capturar Imagem 2"** para fazer capturas de tela que serão salvas automaticamente.
3. **Ajuste a Sensibilidade**: Use o controle deslizante para definir a sensibilidade de detecção para a comparação de imagens.
4. **Comparar**:
   * Clique em **"Comparar Imagens"** para gerar uma nova imagem destacando as diferenças entre as duas capturas de tela.
   * A imagem de diferença é salva e exibida automaticamente.
5. **Revisar e Abrir Imagens Salvas**:
   * Os botões **"Abrir Imagem 1"**, **"Abrir Imagem 2"** e **"Abrir Comparação"** permitem acesso rápido para visualizar as imagens capturadas e comparadas.

## 📝 Estrutura do Código

* **ImageComparatorApp**: A classe principal que define a interface gráfica e a funcionalidade principal.
* **create_layout**: Organiza o layout da interface gráfica, botões e rótulos.
* **capture_image1 & capture_image2**: Captura e salva capturas de tela.
* **compare_images**: Inicia o processo de comparação.
* **find_differences**: Usa o OpenCV para calcular e destacar as diferenças.
* **Log e Notificações**: Registra cada ação na caixa de texto e gera mensagens do sistema.

## 📂 Estrutura de Arquivos
```bash
📦 image-comparator
┣ 📜 image_comparator.py # Código principal do aplicativo
┣ 📜 README.md # Arquivo README
┗ 📜 image-comparator.ico # Ícone personalizado (adicionar à raiz)
```
## 💻 Tecnologias

* **Python**: Linguagem de programação principal.
* **Tkinter**: Biblioteca de interface gráfica.
* **OpenCV**: Biblioteca de processamento de imagens.
* **PyAutoGUI**: Para fazer capturas de tela.

## 🌐 Autor

* **[Eliezer Moraes Silva](https://www.linkedin.com/in/eliezer-moraes-silva-80b68010b/)**

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.

## 🤝 Contribuindo

Se você está interessado em contribuir, sinta-se à vontade para bifurcar o projeto e enviar um pull request. Para mudanças importantes, converse com o autor primeiro.

Com o **ImageComparator®**, você tem uma ferramenta eficiente e confiável para detectar mudanças entre duas imagens em uma interface simplificada e amigável.

### Use sem moderação! 🚀