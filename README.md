# Armazem_Inteligente_Raspberry
Projeto de um armazém inteligente cujos pertences são liberados a partir do reconhecimento facial dos usuários.
# Sistema de Gavetas Inteligentes com Abertura por Reconhecimento Facial

## Descrição Geral
Este projeto foi desenvolvido como parte da disciplina **EEN251 - Microcontroladores e Sistemas Embarcados** do Instituto Mauá de Tecnologia.

## 👨‍💻 Integrantes da Equipe

| Nome                     | RA           |
|--------------------------|--------------|
| Angelo Pisaniello Junior | 12.95003-3   |
| Danilo Di Fábio Bueno    | 22.00028-3   |
| Daniel F. Soares         | 22.01298-2   |


## Descrição do Projeto

O projeto consiste em **três maletas inteligentes** em formato de gaveta, cuja liberação é realizada por **reconhecimento facial** utilizando um **Raspberry Pi 5 (8GB RAM)** e uma **câmera NoIR com lente grande angular**. Cada maleta é trancada e destrancada por um **micro servo motor MG90S** acoplado a um **mecanismo de pistão**, projetado e impresso em 3D pelo grupo.

Além da automação física, o sistema atualiza em tempo real o **status das gavetas (aberta/fechada)** em um **dashboard online** desenvolvido na plataforma **Ubidots**, proporcionando um monitoramento remoto e inteligente.

### 🔧 Funcionalidades embarcadas:

- 🧠 Reconhecimento facial com processamento local via Raspberry Pi 5;
- 🔒 Trava física por servo motor + pistão mecânico impresso em PLA;
- 🟢 Sinalização com **LEDs** para status visual e sonoro;
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
| SR-03  | Travar e destravar as gavetas utilizando micro servos de 12V.                                                     | Obrigatório |
| SR-04  | Detectar o estado (aberta/fechada) de cada gaveta utilizando sensores de fim de curso.                            | Obrigatório |
| SR-05  | Fornecer feedback visual utilizando LEDs indicadores.                                                             | Obrigatório |
| SR-06  | Fornecer feedback visual por meio de um display local.                                                            | Obrigatório |
| SR-07  | Exibir no display as informações de status do reconhecimento facial e abertura das gavetas.                       | Obrigatório |
| SR-08  | Ser alimentado por fonte de 12V com corrente suficiente para acionamento simultâneo dos 3 micro servos.           | Obrigatório |
| SR-09  | Ser montado em estrutura mecânica adequada (ex: gaveteiro impresso em 3D ou caixa segura para o mecanismo).       | Obrigatório |
| SR-10  | Garantir proteção contra sobreaquecimento dos micro servos.                                                       | Obrigatório |
| SR-11  | Permitir futuras expansões, como comunicação com sistemas externos (ex: Wi-Fi ou Bluetooth).                      | Desejável   |
| SR-12  | Implementar modo de bloqueio total em caso de tentativa de acesso não autorizado às gavetas.                      | Desejável   |
| SR-13  | Integrar sistema de controle por meio de tags RFID para rastreabilidade de instrumentação cirúrgica.              | Desejável   |


## 📝 Lista de Componentes

<img width="917" height="469" alt="image" src="https://github.com/user-attachments/assets/9992eaeb-c0f3-489f-b8ab-44f368a1710d" />


## Diagrama de Blocos


## 📥 Esquemáticos do Circuito Eletrônico

Os diagramas do circuito eletrônico do projeto foram desenvolvidos utilizando o software **KiCad EDA 9.0.2**.


Os esquemáticos incluem todos os componentes principais do sistema: Raspberry Pi Pico, RFID, LEDs de sinalização, drivers MOSFET, sensores ópticos, entre outros.



## 📷 Visualização do Circuito Montado


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

- [Arquivo do Projeto do Fusion 360](https://github.com/angelopisaniello/cofre-rfid-pico/blob/8d926f475f4df262f432c6a18744f179cbe58f7a/Projeto%20Mec%C3%A2nico/Angelo%20v4%20v16%20v1.f3d)



## Vídeo Explicativo

- [Link do Youtube](https://youtu.be/eFmRIbqSjfY

## ✅ Conclusão

O projeto apresentado integra hardware, software embarcado e projeto mecânico para demonstrar um sistema de controle de gavetas inteligentes com autenticação por RFID. A solução proposta tem aplicações práticas em segurança e automação, e poderá ser expandida para novas funcionalidades como controle remoto via rede e sensores adicionais.

> Projeto desenvolvido para a disciplina EEN251 - Microcontroladores e Sistemas Embarcados | Instituto Mauá de Tecnologia.

