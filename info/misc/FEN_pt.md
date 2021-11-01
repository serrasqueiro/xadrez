<!-- -*- coding: iso-8859-1 -*- -->

# FEN format - Forsyth-Edwards Notation
Tradução de [FEN](https://github.com/serrasqueiro/xadrez/blob/master/info/misc/FEN.md).md (_Markdown_).
@@@

Referências: [References](https://github.com/serrasqueiro/xadrez/blob/master/info/misc/FEN.md#References).

## Purpose/ Propósito
Uma linha de texto FEN define uma posição particular do jogo, usando apenas caracteres ASCII inválidos.
É designado por registo FEN (no inglês, _FEC record_).

## Definition
Um registo FEN contém seis campos. O separador entre os campos é um espaço.
Os campos são:

1. Posição das peças (na perspectiva das brancas). Cada linha é descrita, começando na linha 8, e finalizando na linha 1; em cada linha, os conteúdos de cada quadrado são descritos, coluna a coluna, desde a coluna "**a**" à coluna "**h**".
   - Segue-se a notação _standard_ algébrica, no inglês _Standard Algebraic Notation_ (*SAN*), cada peça é identificado por uma única letra, tirado do nome inglês das peças:
     * pawn = "P", **peão**
     * knight = "N",  **cavalo**
     * bishop = "B",  **bispo**
     * rook = "R",  **torre**
     * queen = "Q",  **rainha**
     * and king = "K",  **rei**
   - As peças brancas são designadas com letras maiusculas(`PNBRQK`),
   - as peças pretas são designadas com letras minúsculas (`pnbrqk`).
   - os quadrados vazios são denotados com um digito, de 1 a 8, para referir o número de espaços vazios.
   - Mais importante, "/" (_slash_/ ou barra), separa as várias linhas. 8 linhas ao todo.
1. A _cor activa_. "w" deixa claro que o próximo jogador a jogar é das brancas (do inglês, **w**hite),
   - "b", do inglês, **b**lack, ao contrário, designa que o próximo a jogar é das pretas.
1. Possibilidade de roque. Se nenhum dos lados pode efectuar roque, é "-";
   - caso contrário, uma a quatro letras designam, para cada um dos jogadores, as possibilidades de roque:
   - "K" (brancas podem dar roque do lado do rei, K=**K**ing),
   - "Q" (brancas podem dar roque do lado da rainha, Q=**q**ueen),
   - "k" (pretas podem dar roque do lado do rei),
   - "q" (pretas podem dar roque do lado da rainha).
   - Uma jogada que temporariamente evite que o jogador possa dar roque não invalida esta notação.
1. Qual o quadrado é que pode oferecer _en passant_ . Se não existir quadrado _en passant_ , mostra-se "-".
   - Ver também [/3/]
1. Halfmove clock: o numero de meias-jogadas desde que se capturou, ou peão em avanço, usado para a regra dos 50-movimentos.
1. Fullmove number: o numero de jogadas. As jogadas começam em 1, e é incrementado a cada vez que as pretas jogam.

## Exemplos

1. _Main board_ -- tabuleiro inicial:
   - [lichess link](https://lichess.org/editor/rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR_w_KQkq_-_0_1)
     * FEN: `rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1`
     * (sample: [here](https://lichess.org/@/hclm/tv))

1. _Game, end of a game, white check-mates blacks_ -- fim de jogo, as brancas dão cheque-mate às pretas:
   - [link lichess](https://lichess.org/editor?fen=5Rk1%2F2p1P1pp%2F1p6%2F2n1q3%2F8%2F1b6%2FPP4PP%2F7K+b+-+-+0+29)
     * FEN: `5Rk1/2p1P1pp/1p6/2n1q3/8/1b6/PP4PP/7K b - - 0 29`

1. _Game, end of a game due to time forfeit (white wins at fullmove 27)_ -- fim de jogo devido a tempo excedido (as brancas ganham na jogada 27)
   - ![chess game](https://lichess1.org/game/export/gif/MsWQnkKY.gif "Chess game at Lichess.org")
     * FEN: `3R1b1k/pp4r1/2p4p/4QPn1/4N3/6P1/PPP3PK/4q3 b - - 8 27`
     * jogo Raw PGN [aqui](https://lichess.org/game/export/MsWQnkKY?evals=0&clocks=0)
     * jogo Raw PGN with clocks, [aqui](https://lichess.org/game/export/MsWQnkKY?evals=0&clocks=1)
     * jogo _Annotated PGN_, [aqui](https://lichess.org/game/export/MsWQnkKY?literate=1)
     * posição final, exemplo, [aqui](https://lichess.org/editor?fen=3R1b1k%2Fpp4r1%2F2p4p%2F4QPn1%2F4N3%2F6P1%2FPPP3PK%2F4q3+b+-+-+8+27)

## Referências

* /1/ [PGN_standard_1994-03-12.txt](https://ia802908.us.archive.org/26/items/pgn-standard-1994-03-12/PGN_standard_1994-03-12.txt)
* [/2/]: https://github.com/serrasqueiro/xadrez/tree/master/info/misc/PGN_standard_1994-03-12.txt    "PGN_standard"
 /2/: _Local copy of_ [PGN_standard] -- cópia local [/2/]
* [/3/]: https://github.com/serrasqueiro/xadrez/tree/master/info/misc/PGN_standard_1994-03-12.txt    "PGN_standard en_passant"
 /3/: PGN standard, _en passant_ -- section 16.2.3.4
* /10/ about Markdown, and how to make links in Markdown: [aqui](https://daringfireball.net/projects/markdown/syntax#link)
* /11/ sobre este repositório: [xadrez](https://github.com/serrasqueiro/xadrez/)
