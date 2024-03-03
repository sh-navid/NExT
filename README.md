# NExT
Digital personal assistant

> [!Tip]
> Test tip

```mermaid
flowchart LR

    Audio-->String;
    Video-->String;
    Text-->String;

    String-->Tokenize;
    Tokenize-->Train;
    Train-->Knowledge;

    Train-->D {Decision};

    D {Decision}-->Plugin;
    D {Decision}-->Driver;
    D {Decision}-->Luncher;
    D {Decision}-->Widget;
```

## Plugins
  - Firewall
  - Chatbot

## Drivers 
  - Map

## Lunchers
  - UI
  - Map

# Usefull Links
  - NLP
  - Documentation
    - [Simple](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
    - [Advanced](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables)
