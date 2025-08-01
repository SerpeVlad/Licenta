// src/App.jsx

import React, { useState, useEffect } from 'react';
import { Chess } from 'chess.js'; // Asigură-te că ai rulat 'npm install chess.js'
import Chessboard from './components/Chessboard.jsx';
import PieceSelector from './components/PieceSelector.jsx';
import './App.css';

// Funcție ajutătoare pentru a converti [r, c] în notație algebrică ('e4')
const toAlgebraic = (row, col) => {
  const file = String.fromCharCode(97 + col); // 0 -> 'a', 1 -> 'b', ...
  const rank = 8 - row; // 0 -> 8, 1 -> 7, ...
  return `${file}${rank}`;
};

function App() {
  // --- STATE MANAGEMENT ---
  const [game, setGame] = useState(new Chess());
  const [board, setBoard] = useState(game.board());
  const [gameMode, setGameMode] = useState('play');
  const [fromSquare, setFromSquare] = useState(null);
  const [editorSquare, setEditorSquare] = useState(null);
  const [fenInput, setFenInput] = useState(game.fen());

  // Sincronizăm tabla vizuală și input-ul FEN de fiecare dată când obiectul 'game' se schimbă
  useEffect(() => {
    setBoard(game.board());
    setFenInput(game.fen());
  }, [game]);

  // --- LOGIC HANDLERS (definite corect în interiorul componentei) ---

  const handleSquareClick = (row, col, event) => {
    const algebraicPos = toAlgebraic(row, col);
    if (gameMode === 'play') {
      handlePlayModeClick(algebraicPos);
    } else {
      handleEditModeClick(row, col, event);
    }
  };
  
  const handlePlayModeClick = (square) => {
    if (!fromSquare) {
      const moves = game.moves({ square: square, verbose: true });
      if (moves.length > 0) {
        setFromSquare(square);
      }
    } else {
      const move = { from: fromSquare, to: square, promotion: 'q' };
      try {
        const gameCopy = new Chess(game.fen());
        const result = gameCopy.move(move);
        if (result) {
          setGame(gameCopy);
        }
      } catch (err) {
        console.log("Mutare invalidă:", err.message);
      } finally {
        setFromSquare(null);
      }
    }
  };

  const handleEditModeClick = (row, col, event) => {
    const rect = event.currentTarget.getBoundingClientRect();
    const top = rect.top > 200 ? rect.top - 120 : rect.bottom + 10;
    const left = rect.left > 100 ? rect.left - 50 : rect.left;
    setEditorSquare({ row, col, top, left });
  };
  
  const handlePieceSelect = (piece) => {
    if (!editorSquare) return;
    const { row, col } = editorSquare;
    const algebraicPos = toAlgebraic(row, col);
    const gameCopy = new Chess(game.fen());
    gameCopy.put({ type: piece.toLowerCase(), color: piece === piece.toLowerCase() ? 'w' : 'b' }, algebraicPos);
    setGame(gameCopy);
    setEditorSquare(null);
  };

  const handleRemovePiece = () => {
    if (!editorSquare) return;
    const { row, col } = editorSquare;
    const algebraicPos = toAlgebraic(row, col);
    const gameCopy = new Chess(game.fen());
    gameCopy.remove(algebraicPos);
    setGame(gameCopy);
    setEditorSquare(null);
  };
  
  const toggleGameMode = () => {
    setGameMode(gameMode === 'play' ? 'edit' : 'play');
    setFromSquare(null);
    setEditorSquare(null);
  };

  const handleSaveToClipboard = () => {
    navigator.clipboard.writeText(game.fen())
      .then(() => alert('Poziția (FEN) a fost copiată în clipboard!'))
      .catch(err => console.error('Eroare la copiere:', err));
  };

  const handleLoadFromFen = () => {
    try {
      const newGame = new Chess(fenInput);
      setGame(newGame);
    } catch (err) {
      alert('FEN invalid! Vă rugăm verificați string-ul.');
      setFenInput(game.fen()); // Resetăm la FEN-ul valid
    }
  };

  const handleFenInputChange = (event) => {
    setFenInput(event.target.value);
  };

  // --- RENDER ---
  const playerTurn = game.turn() === 'w' ? 'White' : 'Black';

  return (
    <div className="app-layout">
      <div className="game-area">
        <div className="game-info">
          <h1>Chess Engine</h1>
          <div className="controls">
            <div className="control-group">
              <label>Game Mode</label>
              <button onClick={toggleGameMode} className="control-button">
                {gameMode === 'play' ? 'Play' : 'Edit'}
              </button>
            </div>
            <div className="info-item">
              <span>Player to Move:</span>
              <span className={`player-turn ${game.turn() === 'w' ? 'white' : 'black'}`}>
                {playerTurn}
              </span>
            </div>
          </div>
        </div>
        
        <Chessboard 
          board={board} 
          onSquareClick={handleSquareClick} 
        />

        <div className="fen-manager">
          <label htmlFor="fen-input">Forsyth-Edwards Notation (FEN)</label>
          <div className="fen-controls">
            <input 
              id="fen-input"
              type="text" 
              value={fenInput}
              onChange={handleFenInputChange}
              placeholder="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
            />
            <button onClick={handleLoadFromFen}>Load</button>
            <button onClick={handleSaveToClipboard}>Save</button>
          </div>
        </div>

        {gameMode === 'edit' && editorSquare && (
          <PieceSelector
            onSelect={handlePieceSelect}
            onRemove={handleRemovePiece}
            top={editorSquare.top}
            left={editorSquare.left}
          />
        )}
      </div>

      <div className="sidebar">
        <h2>Best Moves</h2>
        <ul className="moves-list">
          {game.isGameOver() && <li className="game-over">Game Over!</li>}
          <li className="placeholder">Engine is idle...</li>
        </ul>
      </div>
    </div>
  );
}

export default App;