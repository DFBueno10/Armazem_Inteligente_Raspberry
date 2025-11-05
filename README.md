# 🤖 Sistema de Gavetas Inteligentes com Abertura por Reconhecimento Facial

Projeto de um armazém inteligente, em formato de maletas, cujos pertences são liberados a partir do reconhecimento facial dos usuários.  
Este repositório faz parte do projeto **Armazem_Inteligente_Raspberry**, desenvolvido na disciplina **EEN251 – Microcontroladores e Sistemas Embarcados**, do Instituto Mauá de Tecnologia.

---

## 👨‍💻 Integrantes da Equipe

A equipe é composta por alunos do curso de Engenharia Eletrônica do IMT, responsáveis por todas as etapas de desenvolvimento:

| Nome                       | RA         |
|----------------------------|------------|
| Angelo Pisaniello Junior   | 12.95003-3 |
| Danilo Di Fábio Bueno      | 22.00028-3 |
| Daniel F. Soares           | 22.01298-2 |

---

## 📋 Descrição do Projeto

O projeto consiste em **três maletas inteligentes** em formato de gaveta, cuja liberação é realizada por **reconhecimento facial**, utilizando um **Raspberry Pi 5 (8GB RAM)** e uma **câmera NoIR com lente grande angular**.

Cada maleta é trancada e destrancada por um **micro servo motor MG90S**, acoplado a um **mecanismo de pistão** desenvolvido e impresso em 3D pelo grupo.

Além da automação física, o sistema atualiza em tempo real o **status de abertura das gavetas** (aberta/fechada), por meio de um **dashboard online** desenvolvido na plataforma **Ubidots**, permitindo **monitoramento remoto e inteligente**.

### 🔧 Funcionalidades embarcadas:

- 🧠 Reconhecimento facial com processamento local via Raspberry Pi 5;
- 🔒 Trava física por servo motor + pistão mecânico impresso em PLA;
- 🟢 Sinalização com **LEDs** para status visual;
- 📡 Monitoramento online via **Ubidots**;
- 📷 Visualização local via **display touchscreen de 7”**;
- 📦 Arquitetura modular e expansível.

### 💡 Este sistema pode ser aplicado em:

- **Cofres de hotel**
- **Armários públicos com controle de acesso**
- **Estações de recarga de celular**
- **Espaços de coworking ou armazenamento seguro**
- **Aplicações especiais e críticas para guarda de instrumentação hospitalar**

---


## 📋 Requisitos do Sistema

| ID     | Requisito                                                                                                         | Tipo        |
|--------|-------------------------------------------------------------------------------------------------------------------|-------------|
| SR-01  | O sistema deve ser composto por módulos prontos e de fácil acesso para manutenção e expansão.                     | Obrigatório |
| SR-02  | Controlar de forma independente a abertura das 3 gavetas por meio de autenticação facial.                         | Obrigatório |
| SR-03  | Travar e destravar as gavetas utilizando micro servos.                                                            | Obrigatório |
| SR-04  | Detectar o estado (aberta/fechada) de cada gaveta utilizando sensores de fim de curso.                            | Obrigatório |
| SR-05  | Fornecer feedback visual utilizando LEDs indicadores.                                                             | Obrigatório |
| SR-06  | Ser montado em estrutura mecânica adequada (ex: gaveteiro impresso em 3D ou caixa segura para o mecanismo).       | Obrigatório |
| SR-07  | Permitir futuras expansões, como comunicação com sistemas externos (ex: Wi-Fi ou Bluetooth).                      | Desejável   |
| SR-08  | Implementar modo de bloqueio total em caso de tentativa de acesso não autorizado às gavetas.                      | Desejável   |

## 📝 Lista de Componentes
<img width="917" height="469" alt="image" src="https://github.com/user-attachments/assets/38061ab1-aaba-4260-99e4-1755eeb5070a" />


## 🧩 Diagrama de Blocos
<img width="1000" height="691" alt="image" src="https://github.com/user-attachments/assets/3b99ee60-6b0c-40bf-97e2-d6b8ec3a4d61" />


## 🛠️ Projeto Mecânico das Gavetas
O projeto das peças mecânicas foi desenvolvido utilizando o software **Autodesk Fusion 360**, versão **2601.1.37 x86_64**, com plano **Estudante**. O ambiente de modelagem foi realizado no **Windows 11 Pro 24H2**.

As peças foram concebidas visando **facilidade de fabricação e montagem**, sendo idealizadas para **impressão 3D** utilizando o material **PLA (Ácido Polilático)**.

### 🎯 Motivos para a escolha do PLA:
- Excelente **custo-benefício**.
- **Facilidade de impressão**, mesmo em impressoras 3D domésticas.
- **Boa resistência mecânica** e **rigidez**, adequada para a estrutura das gavetas.
- Material **biodegradável** e com baixo impacto ambiental.
- **Acabamento estético** superior, com superfície lisa e sem necessidade de pós-processamento complexo.

### 🖥️ Por que escolhemos o Autodesk Fusion 360?
- Ferramenta **profissional e amplamente utilizada** na indústria.
- Permite integração completa entre **modelagem 3D**, **simulações** e **geração de arquivos para impressão (STL)**.
- Licença gratuita para **uso educacional**, ideal para o desenvolvimento acadêmico.
- Ambiente intuitivo, com recursos de **parametrização** e **colaboração em nuvem**.

<img width="1242" height="889" alt="image" src="https://github.com/user-attachments/assets/12c5f9d8-5009-4cd5-a411-59635d6fbb28" />

<img width="1246" height="892" alt="image" src="https://github.com/user-attachments/assets/d4f0f9e5-76c9-4eb7-b155-55f02be37698" />

<img width="1280" height="685" alt="image" src="https://github.com/user-attachments/assets/c4e249c2-02d3-419b-aea2-039bd5217a3c" />


### 🔐🗄️ Imagem do Produto Final
<img width="1321" height="1020" alt="image" src="https://github.com/user-attachments/assets/ce5a1057-022b-48f0-bfb4-d5501b6cb09c" />


📊 **Dashboard Online - Monitoramento em Tempo Real**
O sistema de gavetas inteligentes foi integrado à plataforma **Ubidots**, que permite o monitoramento remoto do status de cada gaveta em tempo real. Cada uma das três gavetas envia seu estado (aberta ou fechada) à nuvem, e os dados são exibidos por meio de gráficos circulares e tabelas de valores.

Essa funcionalidade permite expandir o projeto para aplicações práticas com **gestão de ativos**, **controle de acesso remoto**, **sistemas de inventário** e **armários inteligentes**.

<img width="1919" height="908" alt="image" src="https://github.com/user-attachments/assets/9b7a3fd6-6c7c-4bca-9275-4d1b693c768e" />


▶️ **Vídeo Explicativo**

Apresentação prática do projeto com demonstração do funcionamento das gavetas inteligentes, autenticação via reconhecimento facial, travamento/destravamento por micro servo motor, e monitoramento via dashboard online.

🎥 [Clique aqui para assistir ao vídeo explicativo](https://github.com/DFBueno10/Armazem_Inteligente_Raspberry/raw/49148ff480a725034862d3533b315d37d59a1ea6/V%C3%ADdeo/Armazem_Inteligente.mp4)

## 🎥 Vídeo Explicativo

O vídeo abaixo apresenta o funcionamento do sistema de gavetas inteligentes, destacando o reconhecimento facial, acionamento dos servos e atualização em tempo real no dashboard da Ubidots.

▶️ [Clique aqui para assistir ao vídeo (formato .mp4)](https://github.com/DFBueno10/Armazem_Inteligente_Raspberry/raw/49148ff480a725034862d3533b315d37d59a1ea6/V%C3%ADdeo/Armazem_Inteligente.mp4)


[![Assista ao vídeo]([https://img.youtube.com/vi/SEU_VIDEO_ID/maxresdefault.jpg](https://youtu.be/ZRPwrE82Ogo))]([https://www.youtube.com/watch?v=SEU_VIDEO_ID](https://youtu.be/ZRPwrE82Ogo))


## ✅ Conclusão

O projeto desenvolvido integra de forma eficiente três pilares fundamentais da engenharia: hardware, software embarcado e projeto mecânico. A proposta inicial no T1, baseada em um sistema de gavetas inteligentes com autenticação por RFID, evoluiu significativamente ao incorporar tecnologias mais robustas, como o reconhecimento facial com Raspberry Pi 5, atualização em tempo real via dashboard (Ubidots) e melhorias no acionamento mecânico das travas.

A solução apresentada reforça o potencial do sistema para aplicações práticas em ambientes que exigem segurança, rastreabilidade e controle de acesso — como cofres de hotel, armários hospitalares, pontos de recarga de dispositivos e armazéns inteligentes.

O projeto também se destaca pela modularidade, permitindo futuras expansões, como a integração com comunicação Wi-Fi ou Bluetooth, uso de sensores adicionais e controle remoto. A integração com tags RFID específicas para instrumentação cirúrgica abre ainda novas possibilidades na área hospitalar, com foco em rastreamento e automação de inventário.

O trabalho representou um avanço técnico significativo em relação ao primeiro projeto da disciplina, consolidando o aprendizado multidisciplinar dos integrantes e reforçando a importância da prototipação e documentação em projetos reais de engenharia.


> Projeto desenvolvido para a disciplina EEN251 - Microcontroladores e Sistemas Embarcados | Instituto Mauá de Tecnologia.

