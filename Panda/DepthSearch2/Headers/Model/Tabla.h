#pragma once
#include "Piesa.h"
#include "Pion.h"
#include "Cal.h"
#include "Nebun.h"
#include "Tura.h"
#include "Regina.h"
#include "Rege.h"
#include <string>

class Tabla {
private:
	int howMoves;
	std::string fen;
	std::vector<std::vector<Piesa>> Board;
	std::vector<Piesa> lstPiese;
	std::vector<Piesa> lstPieseAlb;
	std::vector<Piesa> lstPieseNegru;
public:
	Tabla(std::string fen) {
		this->fen = fen;
		extractInfoFromFen();
	}

	std::vector<std::vector<Piesa>> getBoard();
	void setBoard(std::vector<std::vector<Piesa>> board);

	std::string getFen();
	void setFen(std::string fen);

	int getHowMoves();
	void setHowMoves(int howMoves);

	std::vector<Piesa> getLstPiese();
	void setLstPiese(std::vector<Piesa> lst);

	std::vector<Piesa> getLstPieseAlb();
	void setLstPieseAlb(std::vector<Piesa> lst);

	std::vector<Piesa> getLstPieseNegru();
	void setLstPieseNegru(std::vector<Piesa> lst);

	std::vector<std::pair<std::pair<int, int>, Piesa>> getListMoves();
	void extractInfoFromFen();

	//to do
	// verify a move is valid (new function)
	// add on pieces info like isAbsolutePin, en Passant, ifMovedPieceSeen (in extractInfoFromFen)
	//

	bool verifyMoveIsValid(Piesa piece, std::pair<int, int> move);
};