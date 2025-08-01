// src/components/Chessboard.jsx
import React from 'react';
import Square from './Square.jsx';

function Chessboard({ board, onSquareClick }) {
  if (!board || board.length === 0) {
    return <div>Loading board...</div>; 
  }

  return (
    <div className="chessboard">
      {board.map((row, rowIndex) => (
        <React.Fragment key={rowIndex}>
          {row.map((piece, colIndex) => (
            <Square
              key={`${rowIndex}-${colIndex}`}
              piece={piece} // piece este acum {type, color} sau null
              isLight={(rowIndex + colIndex) % 2 !== 0}
              onClick={(e) => onSquareClick(rowIndex, colIndex, e)}
            />
          ))}
        </React.Fragment>
      ))}
    </div>
  );
}

export default Chessboard;