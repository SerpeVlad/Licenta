import React from 'react';

// Am definit un obiect direct în componentă.
// Acesta mapează obiectul de la chess.js la simbolul Unicode corect.
// Structura: { 'culoare': { 'tip_piesa': 'simbol' } }
const PIECE_SYMBOLS = {
  w: { // White pieces
    p: '♟',
    r: '♜',
    n: '♞',
    b: '♝',
    q: '♛',
    k: '♚'
  },
  b: { // Black pieces
    p: '♙',
    r: '♖',
    n: '♘',
    b: '♗',
    q: '♕',
    k: '♔'
  }
};

/**
 * Componenta pentru un singur pătrat de pe tabla de șah.
 * @param {object} props - Proprietățile componentei.
 * @param {object|null} props.piece - Obiectul piesei de la chess.js (ex: { type: 'p', color: 'w' }) sau null.
 * @param {boolean} props.isLight - True dacă pătratul este de culoare deschisă.
 * @param {function} props.onClick - Funcția care se apelează la click.
 */
function Square({ piece, isLight, onClick }) {
  // Determină clasa CSS pentru culoarea pătratului
  const squareColorClass = isLight ? 'light' : 'dark';

  // Determină simbolul piesei pentru afișare.
  // Dacă 'piece' este un obiect valid, caută simbolul corespunzător.
  // Dacă 'piece' este null, simbolul este un string gol.
  const pieceSymbol = piece ? PIECE_SYMBOLS[piece.color][piece.type] : '';

  return (
    <div 
      className={`square ${squareColorClass}`} 
      onClick={onClick}
    >
      <span className="piece">
        {pieceSymbol}
      </span>
    </div>
  );
}

export default Square;