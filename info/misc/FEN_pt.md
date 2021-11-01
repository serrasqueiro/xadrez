<!-- -*- coding: iso-8859-1 -*- -->

# FEN format - Forsyth-Edwards Notation
Tradu��o de [FEN](https://github.com/serrasqueiro/xadrez/blob/master/info/misc/FEN.md).md (_Markdown_).
@@@

Refer�ncias: [References](https://github.com/serrasqueiro/xadrez/blob/master/info/misc/FEN.md#References).

## Purpose/ Prop�sito
Uma linha de texto FEN define uma posi��o particular do jogo, usando apenas caracteres ASCII inv�lidos.
� designado por registo FEN (no ingl�s, _FEC record_).

## Definition
Um registo FEN cont�m seis campos. O separador entre os campos � um espa�o.
Os campos s�o:

1. Posi��o das pe�as (na perspectiva das brancas). Cada linha � descrita, come�ando na linha 8, e finalizando na linha 1; em cada linha, os conte�dos de cada quadrado s�o descritos, coluna a coluna, desde a coluna "**a**" � coluna "**h**".
   - Segue-se a nota��o _standard_ alg�brica, no ingl�s _Standard Algebraic Notation_ (*SAN*), cada pe�a � identificado por uma �nica letra, tirado do nome ingl�s das pe�as:
     * pawn = "P", **pe�o**
     * knight = "N",  **cavalo**
     * bishop = "B",  **bispo**
     * rook = "R",  **torre**
     * queen = "Q",  **rainha**
     * and king = "K",  **rei**
   - As pe�as brancas s�o designadas com letras maiusculas(`PNBRQK`),
   - as pe�as pretas s�o designadas com letras min�sculas (`pnbrqk`).
   - os quadrados vazios s�o denotados com um digito, de 1 a 8, para referir o n�mero de espa�os vazios.
   - Mais importante, "/" (_slash_/ ou barra), separa as v�rias linhas. 8 linhas ao todo.
1. A _cor activa_. "w" deixa claro que o pr�ximo jogador a jogar � das brancas (do ingl�s, **w**hite),
   - "b", do ingl�s, **b**lack, ao contr�rio, designa que o pr�ximo a jogar � das pretas.
1. Possibilidade de roque. Se nenhum dos lados pode efectuar roque, � "-";
   - caso contr�rio, uma a quatro letras designam, para cada um dos jogadores, as possibilidades de roque:
   - "K" (brancas podem dar roque do lado do rei, K=**K**ing),
   - "Q" (brancas podem dar roque do lado da rainha, Q=**q**ueen),
   - "k" (pretas podem dar roque do lado do rei),
   - "q" (pretas podem dar roque do lado da rainha).
   - Uma jogada que temporariamente evite que o jogador possa dar roque n�o invalida esta nota��o.
1. Qual o quadrado � que pode oferecer _en passant_ . Se n�o existir quadrado _en passant_ , mostra-se "-".
   - Ver tamb�m [/3/]
1. Halfmove clock: o numero de meias-jogadas desde que se capturou, ou pe�o em avan�o, usado para a regra dos 50-movimentos.
1. Fullmove number: o numero de jogadas. As jogadas come�am em 1, e � incrementado a cada vez que as pretas jogam.

## Exemplos

1. _Main board_ -- tabuleiro inicial:
   - [lichess link](https://lichess.org/editor/rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR_w_KQkq_-_0_1)
     * FEN: `rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1`
     * (sample: [here](https://lichess.org/@/hclm/tv))

1. _Game, end of a game, white check-mates blacks_ -- fim de jogo, as brancas d�o cheque-mate �s pretas:
   - [link lichess](https://lichess.org/editor?fen=5Rk1%2F2p1P1pp%2F1p6%2F2n1q3%2F8%2F1b6%2FPP4PP%2F7K+b+-+-+0+29)
     * FEN: `5Rk1/2p1P1pp/1p6/2n1q3/8/1b6/PP4PP/7K b - - 0 29`

1. _Game, end of a game due to time forfeit (white wins at fullmove 27)_ -- fim de jogo devido a tempo excedido (as brancas ganham na jogada 27)
   - ![chess game](https://lichess1.org/game/export/gif/MsWQnkKY.gif "Chess game at Lichess.org")
     * FEN: `3R1b1k/pp4r1/2p4p/4QPn1/4N3/6P1/PPP3PK/4q3 b - - 8 27`
     * jogo Raw PGN [aqui](https://lichess.org/game/export/MsWQnkKY?evals=0&clocks=0)
     * jogo Raw PGN with clocks, [aqui](https://lichess.org/game/export/MsWQnkKY?evals=0&clocks=1)
     * jogo _Annotated PGN_, [aqui](https://lichess.org/game/export/MsWQnkKY?literate=1)
     * posi��o final, exemplo, [aqui](https://lichess.org/editor?fen=3R1b1k%2Fpp4r1%2F2p4p%2F4QPn1%2F4N3%2F6P1%2FPPP3PK%2F4q3+b+-+-+8+27)

## Refer�ncias

* /1/ [PGN_standard_1994-03-12.txt](https://ia802908.us.archive.org/26/items/pgn-standard-1994-03-12/PGN_standard_1994-03-12.txt)
* [/2/]: https://github.com/serrasqueiro/xadrez/tree/master/info/misc/PGN_standard_1994-03-12.txt    "PGN_standard"
 /2/: _Local copy of_ [PGN_standard] -- c�pia local [/2/]
* [/3/]: https://github.com/serrasqueiro/xadrez/tree/master/info/misc/PGN_standard_1994-03-12.txt    "PGN_standard en_passant"
 /3/: PGN standard, _en passant_ -- section 16.2.3.4
* /10/ about Markdown, and how to make links in Markdown: [aqui](https://daringfireball.net/projects/markdown/syntax#link)
* /11/ sobre este reposit�rio: [xadrez](https://github.com/serrasqueiro/xadrez/)
