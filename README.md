# NExT
Digital personal assistant

![](./assets/logo.png)

## Platforms
- [ ] Desktop
  - [ ] Windows
  - [x] Linux
  - [ ] Mac
- [ ] Web
- [ ] Mobile
  - [ ] Android
  - [ ] iOS

```mermaid
flowchart LR

A1[Text]  -->| | B(String)
A2[Video] -->| | B(String)
A3[Audio] -->| | B(String)

B -->| | T(Tokenize)

T --> L[ML engine]
L --> M[Models]

M --> I
T --> I[Identifier]

I --> C{Decision}
C -->| | D1[Luncher]
C -->| | D2[Widget]
C -->| | D3[Plugin]
C -->| | D4[Driver]
```

## Engines
  - Chatbot
  - Tokenizer
  - Visualizer

## Plugins
  - Firewall

## Drivers 
  - [ ] Map
  - [ ] Player
  - [ ] Contacts
  - [ ] Notes
  - [ ] Calculator
  - [ ] Calendar

# Usefull Links
  - NLP
  - Documentation
    - [Simple](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
    - [Advanced](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables)
    - [Mermaid](https://github.com/mermaid-js/mermaid)
