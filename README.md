Alunas: Giovanna, Maria, Suelen

# Exercícios Práticos - Segurança da Informação

## Questão 1 - Codificação de Dados: Base64

### Quais propriedades de segurança a Base64 ajuda a proteger?

A Base64 não protege diretamente confidencialidade, integridade ou disponibilidade. Ela é uma técnica de codificação, e não de criptografia. Qualquer pessoa que tenha acesso ao conteúdo codificado pode decodificá-lo facilmente.

Por isso, a Base64 não deve ser utilizada para esconder senhas ou informações sigilosas. Sua função é apenas representar dados em um formato textual compatível com sistemas que trabalham melhor com caracteres comuns.

### Para qual finalidade a Base64 é melhor empregada?

A Base64 é útil para transportar dados binários em meios que trabalham com texto. Ela pode ser usada, por exemplo, para representar imagens, arquivos e outros dados binários em formatos de texto, mensagens e protocolos de comunicação.

---

## Questão 2 - Criptografia Clássica: Cifra de César

### Qual é o tamanho do espaço de chaves?

Considerando o alfabeto inglês com 26 letras, existem 26 deslocamentos possíveis. Um deles é o deslocamento zero, que mantém o texto igual. Por isso, normalmente são consideradas 25 chaves efetivamente diferentes para cifrar uma mensagem.

### Por que um ataque de força bruta é trivial?

O número de possibilidades é muito pequeno. Um atacante pode testar todos os deslocamentos possíveis rapidamente e observar qual resultado forma uma mensagem compreensível. Assim, a Cifra de César não oferece segurança para aplicações atuais.

---

## Questão 3 - Substituição Monoalfabética

### Qual técnica de criptanálise pode ser utilizada?

A substituição monoalfabética é vulnerável à análise de frequência.

Essa técnica observa quantas vezes cada letra aparece no texto cifrado. Como uma mesma letra do texto original é sempre substituída pela mesma letra na cifra, os padrões de frequência continuam existindo.

Em um texto suficientemente grande, é possível comparar as letras mais frequentes da mensagem cifrada com as letras mais comuns do idioma. Também podem ser analisados padrões de palavras, letras repetidas e combinações frequentes. Com isso, a chave pode ser descoberta aos poucos, mesmo que existam muitas combinações possíveis.

---

## Questão 4 - Armazenamento Seguro de Senhas e Criptanálise

### O que são Rainbow Tables?

Rainbow Tables são tabelas previamente calculadas que relacionam possíveis senhas aos seus respectivos hashes. Em vez de calcular várias possibilidades no momento do ataque, o atacante consulta valores já preparados anteriormente.

Se um banco de dados de hashes for vazado e os hashes tiverem sido gerados sem proteção adicional, o atacante pode procurar correspondências nessas tabelas e descobrir senhas que já estejam presentes nelas.

### O que é Salt e como ele protege contra Rainbow Tables?

Salt é um valor aleatório adicionado à senha antes da geração do hash. Dessa forma, duas pessoas que utilizem a mesma senha podem possuir hashes diferentes, desde que os salts sejam diferentes.

O uso de salt dificulta ataques com Rainbow Tables porque uma tabela criada previamente para hashes sem salt deixa de funcionar diretamente. O atacante teria que gerar novas tentativas considerando o salt utilizado em cada senha, aumentando muito o trabalho necessário.
