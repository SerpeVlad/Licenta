// src/components/PieceSelector.js
import React from 'react';
import { PIECES, AVAILABLE_PIECES } from '../pieces'; // La fel, mergem un folder în sus

function PieceSelector({ onSelect, onRemove, top, left }) {
  return (
    <div className="piece-selector" style={{ top: `${top}px`, left: `${left}px` }}>
      {AVAILABLE_PIECES.map(pieceKey => (
        <div key={pieceKey} className="piece-option" onClick={() => onSelect(pieceKey)}>
          {PIECES[pieceKey]}
        </div>
      ))}
      <div className="piece-option remove" onClick={onRemove}>
        Gol
      </div>
    </div>
  );
}

export default PieceSelector;